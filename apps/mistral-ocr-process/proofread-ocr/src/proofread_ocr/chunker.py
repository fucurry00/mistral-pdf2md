"""Phase 2: Chunk document into bounded segments with overlap."""

from __future__ import annotations

import re
from pathlib import Path

from .models import ChunkManifest, ChunkMeta


def estimate_tokens(text: str) -> int:
    """Estimate token count using character-based heuristic.

    CJK-heavy text: ~3 chars/token. Latin text: ~4 chars/token.
    """
    if not text:
        return 0
    sample = text[:1000]
    cjk_count = sum(1 for c in sample if "\u4e00" <= c <= "\u9fff" or "\u3040" <= c <= "\u30ff")
    ratio = cjk_count / max(len(sample), 1)
    chars_per_token = 3 if ratio > 0.3 else 4
    return len(text) // chars_per_token


def _find_heading_boundaries(lines: list[str]) -> list[tuple[int, int]]:
    """Find line indices of ## and ### headings with their priority.

    Returns list of (line_index, priority) where priority 1 = ##, 2 = ###.
    """
    boundaries = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("## ") and not stripped.startswith("### "):
            boundaries.append((i, 1))
        elif stripped.startswith("### "):
            boundaries.append((i, 2))
    return boundaries


def _find_theorem_boundaries(lines: list[str]) -> list[int]:
    """Find blank lines between theorem-like blocks as fallback boundaries."""
    theorem_re = re.compile(
        r"^\*?\*?(?:Definition|Theorem|Proposition|Lemma|Corollary|Proof|Remark)\b",
        re.IGNORECASE,
    )
    boundaries = []
    for i, line in enumerate(lines):
        if (
            line.strip() == ""
            and i + 1 < len(lines)
            and theorem_re.match(lines[i + 1].strip())
        ):
            boundaries.append(i)
    return boundaries


def _extract_section_title(lines: list[str]) -> str:
    """Extract the first heading from a set of lines."""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## ") or stripped.startswith("### "):
            return stripped.lstrip("#").strip()
    return "(untitled)"


def chunk_document(
    text: str,
    chunk_size_tokens: int = 20000,
    overlap_lines: int = 5,
    source_name: str = "input.md",
) -> tuple[list[str], ChunkManifest]:
    """Split a Markdown document into chunks with overlap markers.

    Returns:
        Tuple of (list of chunk file contents as strings, ChunkManifest).
    """
    lines = text.splitlines(keepends=True)
    if not lines:
        return [], ChunkManifest(
            source=source_name, total_chunks=0,
            chunk_size_target=chunk_size_tokens, overlap_lines=overlap_lines,
        )

    # Safety margin: target 90% of budget
    budget = int(chunk_size_tokens * 0.9)

    # Find all section boundaries
    sections = _split_into_sections(lines, budget)

    # Build chunks by accumulating sections up to budget
    raw_chunks = _accumulate_sections(sections, budget)

    # Apply overlap and metadata
    chunk_contents = []
    chunk_metas = []

    for i, (chunk_lines, line_start, line_end) in enumerate(raw_chunks):
        chunk_id = f"{i + 1:03d}"
        section_title = _extract_section_title(chunk_lines)

        prev_section = ""
        next_section = ""
        if i > 0:
            prev_section = _extract_section_title(raw_chunks[i - 1][0])
        if i + 1 < len(raw_chunks):
            next_section = _extract_section_title(raw_chunks[i + 1][0])

        # Build chunk content with metadata and overlap markers
        content_parts = []

        # Chunk metadata
        content_parts.append(
            f"<!-- CHUNK_META\n"
            f"chunk_id: {chunk_id}\n"
            f'section: "{section_title}"\n'
            f'prev_section: "{prev_section}"\n'
            f'next_section: "{next_section}"\n'
            f"total_chunks: {len(raw_chunks)}\n"
            f"-->\n"
        )

        # Before overlap
        if i > 0 and overlap_lines > 0:
            prev_lines = raw_chunks[i - 1][0]
            overlap_before = prev_lines[-overlap_lines:]
            content_parts.append("<!-- OVERLAP_START -->\n")
            content_parts.append("".join(overlap_before))
            content_parts.append("\n<!-- OVERLAP_END -->\n\n")

        # Main body
        content_parts.append("".join(chunk_lines))

        # After overlap
        if i + 1 < len(raw_chunks) and overlap_lines > 0:
            next_lines = raw_chunks[i + 1][0]
            overlap_after = next_lines[:overlap_lines]
            content_parts.append("\n<!-- OVERLAP_START -->\n")
            content_parts.append("".join(overlap_after))
            content_parts.append("\n<!-- OVERLAP_END -->\n")

        chunk_text = "".join(content_parts)
        chunk_contents.append(chunk_text)

        chunk_metas.append(ChunkMeta(
            id=chunk_id,
            section=section_title,
            prev_section=prev_section,
            next_section=next_section,
            line_start=line_start + 1,  # 1-indexed
            line_end=line_end + 1,
            estimated_tokens=estimate_tokens("".join(chunk_lines)),
        ))

    manifest = ChunkManifest(
        source=source_name,
        total_chunks=len(chunk_contents),
        chunk_size_target=chunk_size_tokens,
        overlap_lines=overlap_lines,
        chunks=chunk_metas,
    )

    return chunk_contents, manifest


def _split_into_sections(
    lines: list[str], budget: int
) -> list[tuple[list[str], int, int]]:
    """Split lines into sections at heading boundaries.

    Each section is (lines, start_line_index, end_line_index).
    If a section exceeds budget, try finer splitting.
    """
    heading_bounds = _find_heading_boundaries(lines)

    # Build sections from heading boundaries
    if not heading_bounds:
        # No headings at all: treat entire document as one section
        return [(lines, 0, len(lines) - 1)]

    sections: list[tuple[list[str], int, int]] = []

    # Collect boundary line indices (only priority-1 first)
    p1_indices = [idx for idx, pri in heading_bounds if pri == 1]
    p2_indices = [idx for idx, pri in heading_bounds if pri == 2]

    # Use ## boundaries first
    split_indices = sorted(p1_indices) if p1_indices else sorted(p2_indices)

    prev = 0
    for idx in split_indices:
        if idx > prev:
            section_lines = lines[prev:idx]
            sections.append((section_lines, prev, idx - 1))
        prev = idx

    # Last section
    if prev < len(lines):
        sections.append((lines[prev:], prev, len(lines) - 1))

    # Check if any section is too large; if so, try finer splitting
    refined: list[tuple[list[str], int, int]] = []
    for section_lines, start, end in sections:
        section_text = "".join(section_lines)
        if estimate_tokens(section_text) > budget:
            sub_sections = _subsplit_section(section_lines, start, budget, p2_indices)
            refined.extend(sub_sections)
        else:
            refined.append((section_lines, start, end))

    return refined


def _subsplit_section(
    section_lines: list[str],
    global_start: int,
    budget: int,
    p2_indices: list[int],
) -> list[tuple[list[str], int, int]]:
    """Try splitting a large section at ### boundaries or theorem boundaries."""
    # Find ### boundaries within this section
    local_p2 = [idx - global_start for idx in p2_indices
                 if global_start <= idx < global_start + len(section_lines)]

    if local_p2:
        return _split_at_indices(section_lines, global_start, local_p2, budget)

    # Fallback: theorem boundaries
    theorem_bounds = _find_theorem_boundaries(section_lines)
    if theorem_bounds:
        return _split_at_indices(section_lines, global_start, theorem_bounds, budget)

    # Last resort: just return the oversized section as-is
    return [(section_lines, global_start, global_start + len(section_lines) - 1)]


def _split_at_indices(
    section_lines: list[str],
    global_start: int,
    local_indices: list[int],
    budget: int,
) -> list[tuple[list[str], int, int]]:
    """Split section_lines at given local indices."""
    parts: list[tuple[list[str], int, int]] = []
    prev = 0
    for idx in sorted(local_indices):
        if idx > prev:
            part_lines = section_lines[prev:idx]
            parts.append((part_lines, global_start + prev, global_start + idx - 1))
        prev = idx

    if prev < len(section_lines):
        end = global_start + len(section_lines) - 1
        parts.append((section_lines[prev:], global_start + prev, end))

    return parts


def _accumulate_sections(
    sections: list[tuple[list[str], int, int]], budget: int
) -> list[tuple[list[str], int, int]]:
    """Greedily accumulate sections into chunks under the token budget."""
    if not sections:
        return []

    chunks: list[tuple[list[str], int, int]] = []
    current_lines: list[str] = []
    current_start = sections[0][1]
    current_tokens = 0

    for section_lines, start, end in sections:
        section_text = "".join(section_lines)
        section_tokens = estimate_tokens(section_text)

        if current_tokens + section_tokens > budget and current_lines:
            # Flush current chunk
            chunks.append((current_lines, current_start, start - 1))
            current_lines = list(section_lines)
            current_start = start
            current_tokens = section_tokens
        else:
            current_lines.extend(section_lines)
            current_tokens += section_tokens

    if current_lines:
        last_end = sections[-1][2]
        chunks.append((current_lines, current_start, last_end))

    return chunks


def write_chunks(
    chunk_contents: list[str],
    manifest: ChunkManifest,
    chunks_dir: Path,
) -> None:
    """Write chunk files and manifest to disk."""
    chunks_dir.mkdir(parents=True, exist_ok=True)

    for i, content in enumerate(chunk_contents):
        chunk_id = f"{i + 1:03d}"
        chunk_path = chunks_dir / f"chunk_{chunk_id}.md"
        chunk_path.write_text(content, encoding="utf-8")

    manifest.save(chunks_dir / "chunk_manifest.json")
