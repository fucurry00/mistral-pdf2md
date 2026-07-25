"""Split normalized OCR pages without losing page provenance."""

from __future__ import annotations

import re

from pdf_curator.blocks.classify import classify_text
from pdf_curator.models import Block, BlockType, OcrPage, PageRange


def _confidence(page: OcrPage) -> float | None:
    if not page.confidence:
        return None
    value = page.confidence.get("average_page_confidence_score")
    return float(value) if isinstance(value, (int, float)) else None


def _segments(markdown: str) -> list[str]:
    segments: list[str] = []
    paragraph: list[str] = []
    table: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            segments.append("\n".join(paragraph).strip())
            paragraph.clear()

    def flush_table() -> None:
        if table:
            segments.append("\n".join(table).strip())
            table.clear()

    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_table()
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            table.append(stripped)
            continue
        flush_table()
        standalone = bool(
            re.match(r"^#{1,6}\s+", stripped)
            or re.match(r"^(?:[-*+] |\d+[.)] )", stripped)
            or stripped.startswith("![")
            or re.match(r"^\[tbl-", stripped, re.IGNORECASE)
        )
        if standalone:
            flush_paragraph()
            segments.append(stripped)
        else:
            paragraph.append(line.rstrip())
    flush_paragraph()
    flush_table()
    return segments


def split_pages_into_blocks(pages: list[OcrPage]) -> list[Block]:
    blocks: list[Block] = []
    counter = 1
    for page in pages:
        page_range = PageRange(page.index, page.index)
        candidates: list[tuple[str, str]] = []
        if page.header:
            candidates.append((page.header, "header"))
        page_segments = _segments(page.markdown)
        for index, segment in enumerate(page_segments):
            if index == 0:
                position = "first"
            elif index == len(page_segments) - 1:
                position = "last"
            else:
                position = "body"
            candidates.append((segment, position))
        if page.footer:
            candidates.append((page.footer, "footer"))

        known_table_placeholders = "\n".join(text for text, _ in candidates)
        for table_index, _table in enumerate(page.tables):
            marker = f"[tbl-{table_index}"
            if marker not in known_table_placeholders:
                candidates.append((f"[Table on source page {page.index}]", "body"))

        for text, position in candidates:
            block_type = classify_text(text, position=position)
            attrs: dict[str, object] = {"position": position}
            if block_type is BlockType.TABLE:
                attrs["broken"] = text.startswith("[tbl-") or text.startswith("[Table on source")
            if block_type is BlockType.FIGURE_CAPTION:
                attrs["has_image_placeholder"] = "![" in text
            if re.search(r"(?:\$\$|\\\[|\[formula\])", text, re.IGNORECASE):
                attrs["visual_type"] = "formula"
                attrs["low_confidence"] = (_confidence(page) or 0.0) < 0.8
            blocks.append(
                Block(
                    id=f"b{counter:05d}",
                    type=block_type,
                    text=text,
                    pages=page_range,
                    source_ids=[f"page-{page.index}"],
                    confidence=_confidence(page),
                    attrs=attrs,
                )
            )
            counter += 1
    return blocks
