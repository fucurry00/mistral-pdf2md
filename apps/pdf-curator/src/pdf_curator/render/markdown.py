"""Render source-referenced Markdown from block page tags."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pdf_curator.errors import ValidationError
from pdf_curator.models import (
    Block,
    BlockType,
    DocumentModel,
    EMITTED_BLOCK_TYPES,
    PageRange,
)
from pdf_curator.render.frontmatter import render_frontmatter

@dataclass(slots=True)
class Section:
    id: str
    heading: str
    blocks: list[Block]
    pages: PageRange


def _heading_text(block: Block) -> str:
    return re.sub(r"^#{1,6}\s+", "", block.text).strip()


def build_sections(blocks: list[Block]) -> list[Section]:
    emitted = [
        block
        for block in blocks
        if block.type in EMITTED_BLOCK_TYPES and not block.attrs.get("excluded")
    ]
    sections: list[Section] = []
    current: list[Block] = []
    heading = "Document content"

    def flush() -> None:
        nonlocal current, heading
        if not current:
            return
        pages = current[0].require_provenance()
        for block in current[1:]:
            pages = pages.union(block.require_provenance())
        sections.append(
            Section(id=f"s{len(sections) + 1:03d}", heading=heading, blocks=current, pages=pages)
        )
        current = []

    for block in emitted:
        if block.type in {BlockType.TITLE, BlockType.HEADING}:
            flush()
            heading = _heading_text(block) or "Untitled section"
        current.append(block)
    flush()
    return sections


def section_index(sections: list[Section]) -> list[dict[str, Any]]:
    return [
        {
            "id": section.id,
            "heading": section.heading,
            "pages": section.pages.label(),
        }
        for section in sections
    ]


def _render_block(block: Block) -> str:
    page = block.require_provenance().label()
    if block.attrs.get("visual_type") == "formula" and block.attrs.get("low_confidence"):
        return f"[Formula on PDF p.{page}]"
    if block.type is BlockType.TABLE and block.attrs.get("broken"):
        return f"[Table on PDF p.{page}]"
    if block.type is BlockType.FIGURE_CAPTION:
        caption_lines = [line for line in block.text.splitlines() if "![" not in line]
        caption = "\n".join(caption_lines).strip()
        pointer = f"[Figure on PDF p.{page}]"
        return f"{caption}\n\n{pointer}" if caption else pointer
    return block.text.strip()


def _render_body(sections: list[Section]) -> str:
    lines: list[str] = []
    previous_page: int | None = None
    for section in sections:
        first = section.blocks[0]
        if first.type not in {BlockType.TITLE, BlockType.HEADING}:
            lines.append(f"## {section.heading}")
        else:
            lines.append(first.text.strip())
        source_line = f"Source: PDF p.{section.pages.label()}"
        if source_line not in first.attrs.get("provenance_annotations", []):
            raise ValidationError(
                f"section {section.id} is missing gated provenance annotation"
            )
        lines.append(source_line)
        lines.append("")
        start_index = 1 if first.type in {BlockType.TITLE, BlockType.HEADING} else 0
        for index, block in enumerate(section.blocks):
            pages = block.require_provenance()
            if previous_page != pages.start:
                page_marker = f"<!-- PDF p.{pages.start} -->"
                if page_marker not in block.attrs.get("provenance_annotations", []):
                    raise ValidationError(
                        f"block {block.id} is missing gated page provenance annotation"
                    )
                lines.append(page_marker)
                lines.append("")
            if index >= start_index:
                lines.append(_render_block(block))
                lines.append("")
            previous_page = pages.end
    return "\n".join(lines).rstrip() + "\n"


def _source_ranges(body: str) -> list[str]:
    return re.findall(r"^Source: PDF p\.(\d+(?:-\d+)?)$", body, re.MULTILINE)


def render_curated_markdown(
    document: DocumentModel,
    *,
    section_index_override: list[dict[str, Any]] | None = None,
) -> str:
    document.validate_provenance()
    sections = build_sections(document.blocks)
    if not sections:
        raise ValidationError("document has no provenance-bearing content blocks to emit")
    derived_index = section_index(sections)
    chosen_index = section_index_override if section_index_override is not None else derived_index
    if chosen_index != derived_index:
        raise ValidationError("section_index does not match block-derived body sources")

    body = _render_body(sections)
    if _source_ranges(body) != [entry["pages"] for entry in derived_index]:
        raise ValidationError("rendered Source lines disagree with section_index")

    first_title = next(
        (_heading_text(block) for block in document.blocks if block.type is BlockType.TITLE),
        None,
    )
    metadata = {
        "title": document.metadata.get("title") or first_title or Path(document.source_pdf).stem,
        "source_pdf": document.source_pdf,
        "page_count": document.page_count,
        "course_name": document.metadata.get("course_name", "uncertain"),
        "lecture_name": document.metadata.get("lecture_name", "uncertain"),
        "instructor": document.metadata.get("instructor", "uncertain"),
        "date": document.metadata.get("date", "uncertain"),
        "term": document.metadata.get("term", "uncertain"),
        "section_index": derived_index,
        "glossary": document.metadata.get("glossary", {}),
        "processing_summary": document.processing_summary,
        "warnings": document.warnings,
    }
    return f"{render_frontmatter(metadata)}\n\n{body}"
