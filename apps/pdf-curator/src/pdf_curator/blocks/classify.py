"""Conservative Markdown block classification."""

from __future__ import annotations

import re
from collections.abc import Collection

from pdf_curator.models import BlockType

_LIST_RE = re.compile(r"^\s*(?:[-*+] |\d+[.)] )")
_PAGE_RE = re.compile(r"^\s*(?:p(?:age)?\.?\s*)?\d{1,4}\s*$", re.IGNORECASE)
_TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_IMAGE_RE = re.compile(r"!\[[^]]*]\([^)]+\)")
_TABLE_LINK_RE = re.compile(r"\[tbl-[^]]+]\([^)]+\)", re.IGNORECASE)
_CAPTION_RE = re.compile(r"^\s*(?:fig(?:ure)?\.?|図)\s*\d*[:.：\s]", re.IGNORECASE)


def normalize_repeated_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def classify_text(
    text: str,
    *,
    position: str | None = None,
    repeated_texts: Collection[str] = (),
) -> BlockType:
    stripped = text.strip()
    normalized = normalize_repeated_text(stripped)
    if not stripped:
        return BlockType.UNKNOWN
    if normalized in repeated_texts and position in {"header", "footer", "first", "last"}:
        return BlockType.HEADER_FOOTER
    if _PAGE_RE.fullmatch(stripped) and position in {"first", "last", "header", "footer"}:
        return BlockType.PAGE_NUMBER
    if stripped.startswith("# "):
        return BlockType.TITLE
    if re.match(r"^#{2,6}\s+", stripped):
        return BlockType.HEADING
    if _LIST_RE.match(stripped):
        return BlockType.LIST_ITEM
    if _TABLE_LINK_RE.search(stripped) or all(
        _TABLE_ROW_RE.match(line) for line in stripped.splitlines() if line.strip()
    ):
        return BlockType.TABLE
    if _IMAGE_RE.search(stripped) or _CAPTION_RE.match(stripped):
        return BlockType.FIGURE_CAPTION
    if len(stripped) <= 2 and not stripped.isalnum():
        return BlockType.UNKNOWN
    if re.search(r"[\w\u3040-\u30ff\u3400-\u9fff]", stripped):
        return BlockType.PARAGRAPH
    return BlockType.UNKNOWN


def is_separator(text: str) -> bool:
    return bool(re.fullmatch(r"\s*(?:[-_*]\s*){3,}", text))
