"""Phase 4: Merge proofread chunks and generate reports."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from .models import ChunkManifest, DiffEntry, ProofreadResult

_OVERLAP_RE = re.compile(
    r"<!-- OVERLAP_START -->\n.*?<!-- OVERLAP_END -->\n?",
    re.DOTALL,
)
_CHUNK_META_RE = re.compile(
    r"<!-- CHUNK_META\n.*?-->\n?",
    re.DOTALL,
)
_FIXED_RE = re.compile(
    r"<!-- FIXED: (.+?) → (.+?) \| (.+?) -->"
)
_UNCERTAIN_RE = re.compile(
    r"<!-- UNCERTAIN: (.+?) → (.+?) \| (.+?) -->"
)
_LATEX_BLOCK_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_LATEX_ENV_RE = re.compile(r"\\begin\{(\w+)\}|\\end\{(\w+)\}")


def validate_latex(text: str) -> list[str]:
    """Check for unmatched $ delimiters and \\begin/\\end pairs."""
    warnings: list[str] = []

    # Check inline $ balance
    stripped = _LATEX_BLOCK_RE.sub("", text)
    dollar_count = len(re.findall(r"(?<!\$)\$(?!\$)", stripped))
    if dollar_count % 2 != 0:
        warnings.append(f"Unmatched inline $ delimiter (found {dollar_count} single $)")

    # Check \\begin/\\end pairs
    env_stack: list[str] = []
    for m in _LATEX_ENV_RE.finditer(text):
        if m.group(1):  # \begin
            env_stack.append(m.group(1))
        else:  # \end
            env_name = m.group(2)
            if env_stack and env_stack[-1] == env_name:
                env_stack.pop()
            else:
                warnings.append(f"Unmatched \\end{{{env_name}}}")
    for env in env_stack:
        warnings.append(f"Unclosed \\begin{{{env}}}")

    return warnings


def _strip_markers(text: str) -> str:
    """Remove overlap and chunk metadata markers from text."""
    text = _OVERLAP_RE.sub("", text)
    text = _CHUNK_META_RE.sub("", text)
    return text


def _extract_annotations(text: str) -> list[DiffEntry]:
    """Extract FIXED and UNCERTAIN annotations from proofread text."""
    entries: list[DiffEntry] = []

    # Try to determine section from nearby headings
    lines = text.splitlines()
    current_section = ""

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## ") or stripped.startswith("### "):
            current_section = stripped.lstrip("#").strip()

        for m in _FIXED_RE.finditer(line):
            entries.append(DiffEntry(
                section=current_section,
                original=m.group(1),
                corrected=m.group(2),
                reason=m.group(3),
                confidence="FIXED",
            ))

        for m in _UNCERTAIN_RE.finditer(line):
            entries.append(DiffEntry(
                section=current_section,
                original=m.group(1),
                corrected=m.group(2),
                reason=m.group(3),
                confidence="UNCERTAIN",
            ))

    return entries


def _strip_all_annotations(text: str) -> str:
    """Remove all FIXED and UNCERTAIN annotation comments."""
    text = _FIXED_RE.sub("", text)
    text = _UNCERTAIN_RE.sub("", text)
    # Clean up any double spaces left behind
    text = re.sub(r"  +", " ", text)
    return text


def _build_frontmatter(
    source: str,
    model: str,
    fixed_count: int,
    uncertain_count: int,
) -> str:
    """Generate YAML frontmatter for the output document."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return (
        f"---\n"
        f'source_format: "PDF (OCR → Markdown)"\n'
        f'ocr_engine: "mistral-ocr"\n'
        f'proofread_model: "{model}"\n'
        f'proofread_date: "{now}"\n'
        f'pipeline_version: "0.1.0"\n'
        f"total_fixes: {fixed_count}\n"
        f"uncertain_fixes: {uncertain_count}\n"
        f"---\n\n"
    )


def _build_diff_report(
    entries: list[DiffEntry],
    source: str,
) -> str:
    """Generate the diff report markdown."""
    now = datetime.now(timezone.utc).isoformat()
    fixed = [e for e in entries if e.confidence == "FIXED"]
    uncertain = [e for e in entries if e.confidence == "UNCERTAIN"]

    lines = [
        f"# 校正 Diff レポート\n\n",
        f"生成日時: {now}\n",
        f"入力ファイル: {source}\n",
        f"総修正数: {len(entries)} (確定: {len(fixed)}, 要確認: {len(uncertain)})\n\n",
    ]

    if fixed:
        lines.append("## 確定修正 (FIXED)\n\n")
        lines.append("| # | セクション | 原文 | 修正後 | 理由 |\n")
        lines.append("| --- | ---------- | --- | --- | --- |\n")
        for i, e in enumerate(fixed, 1):
            lines.append(f"| {i} | {e.section} | `{e.original}` | `{e.corrected}` | {e.reason} |\n")
        lines.append("\n")

    if uncertain:
        lines.append("## 要確認 (UNCERTAIN)\n\n")
        lines.append("| # | セクション | 原文 | 修正案 | 理由 |\n")
        lines.append("| --- | ---------- | --- | --- | --- |\n")
        for i, e in enumerate(uncertain, 1):
            lines.append(f"| {i} | {e.section} | `{e.original}` | `{e.corrected}` | {e.reason} |\n")
        lines.append("\n")

    if not entries:
        lines.append("修正箇所はありませんでした。\n")

    return "".join(lines)


def _build_stats(
    source: str,
    model: str,
    manifest: ChunkManifest,
    results: list[ProofreadResult],
    entries: list[DiffEntry],
    context_duration: float | None = None,
) -> dict:
    """Build the stats.json data."""
    succeeded = [r for r in results if r.success]
    failed = [r for r in results if not r.success]
    total_duration = sum(r.duration_sec for r in results)
    total_tokens_in = sum(r.tokens_in or 0 for r in results)
    total_tokens_out = sum(r.tokens_out or 0 for r in results)

    fixed = [e for e in entries if e.confidence == "FIXED"]
    uncertain = [e for e in entries if e.confidence == "UNCERTAIN"]

    stats = {
        "source": source,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "phases": {
            "context_extraction": {
                "duration_sec": context_duration or 0,
            },
            "chunking": {
                "total_chunks": manifest.total_chunks,
                "avg_chunk_tokens": (
                    sum(c.estimated_tokens for c in manifest.chunks) // max(manifest.total_chunks, 1)
                ),
            },
            "proofreading": {
                "succeeded": len(succeeded),
                "failed": len(failed),
                "total_duration_sec": round(total_duration, 1),
                "total_tokens": {
                    "input": total_tokens_in,
                    "output": total_tokens_out,
                },
            },
            "merge": {
                "total_fixes": len(fixed),
                "total_uncertain": len(uncertain),
            },
        },
    }
    return stats


def merge_results(
    manifest: ChunkManifest,
    results_dir: Path,
    chunks_dir: Path,
    output_path: Path,
    model: str = "gemini-3-flash-preview",
    strip_annotations: bool = False,
    results: list[ProofreadResult] | None = None,
    context_duration: float | None = None,
) -> tuple[Path, Path, Path]:
    """Merge proofread chunks into final output with reports.

    Returns paths to (output.md, diff_report.md, stats.json).
    """
    output_dir = output_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    merged_parts: list[str] = []
    all_entries: list[DiffEntry] = []

    # Load results if not provided
    if results is None:
        results = []
        for meta in manifest.chunks:
            result_path = results_dir / f"chunk_{meta.id}.json"
            if result_path.exists():
                results.append(ProofreadResult.load(result_path))
            else:
                results.append(ProofreadResult(
                    chunk_id=meta.id, success=False, error="Result file not found",
                ))

    # Build result lookup
    result_map = {r.chunk_id: r for r in results}

    for meta in manifest.chunks:
        result = result_map.get(meta.id)

        if result and result.success and result.output_text:
            text = result.output_text
        else:
            # Fallback: use original chunk
            chunk_path = chunks_dir / f"chunk_{meta.id}.md"
            if chunk_path.exists():
                text = chunk_path.read_text(encoding="utf-8")
            else:
                text = ""

        # Extract annotations before stripping markers
        all_entries.extend(_extract_annotations(text))

        # Strip overlap and metadata markers
        text = _strip_markers(text)

        if strip_annotations:
            text = _strip_all_annotations(text)

        merged_parts.append(text.strip())

    # Combine
    merged_text = "\n\n".join(part for part in merged_parts if part)

    # LaTeX validation
    latex_warnings = validate_latex(merged_text)

    # Add frontmatter
    fixed_count = len([e for e in all_entries if e.confidence == "FIXED"])
    uncertain_count = len([e for e in all_entries if e.confidence == "UNCERTAIN"])
    frontmatter = _build_frontmatter(manifest.source, model, fixed_count, uncertain_count)
    final_text = frontmatter + merged_text

    # Write outputs
    output_path.write_text(final_text, encoding="utf-8")

    diff_report_path = output_dir / "diff_report.md"
    diff_report = _build_diff_report(all_entries, manifest.source)
    if latex_warnings:
        diff_report += "\n## LaTeX Warnings\n\n"
        for w in latex_warnings:
            diff_report += f"- {w}\n"
    diff_report_path.write_text(diff_report, encoding="utf-8")

    stats_path = output_dir / "stats.json"
    stats = _build_stats(
        manifest.source, model, manifest, results, all_entries, context_duration,
    )
    stats_path.write_text(
        json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8",
    )

    return output_path, diff_report_path, stats_path
