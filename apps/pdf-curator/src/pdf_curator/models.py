"""Typed internal model and provenance invariants."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from pdf_curator.errors import ValidationError


class BlockType(StrEnum):
    TITLE = "title"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST_ITEM = "list_item"
    TABLE = "table"
    FIGURE_CAPTION = "figure_caption"
    HEADER_FOOTER = "header_footer"
    PAGE_NUMBER = "page_number"
    UNKNOWN = "unknown"


EMITTED_BLOCK_TYPES = frozenset(
    {
        BlockType.TITLE,
        BlockType.HEADING,
        BlockType.PARAGRAPH,
        BlockType.LIST_ITEM,
        BlockType.TABLE,
        BlockType.FIGURE_CAPTION,
    }
)


class MutationType(StrEnum):
    HEADER_FOOTER_REMOVE = "header_footer_remove"
    PAGE_NUMBER_REMOVE = "page_number_remove"
    LINEBREAK_REPAIR = "linebreak_repair"
    LIST_RESTORE = "list_restore"
    OCR_CHAR_FIX = "ocr_char_fix"
    BULK_OCR_FIX = "bulk_ocr_fix"
    PARAGRAPH_RESTRUCTURE = "paragraph_restructure"
    CONTENT_DELETE = "content_delete"
    CONTENT_ADD = "content_add"
    SUMMARIZE = "summarize"
    PARAPHRASE = "paraphrase"
    HEADING_LEVEL_NORMALIZE = "heading_level_normalize"
    PROVENANCE_ANNOTATION = "provenance_annotation"


class EditTrigger(StrEnum):
    AUTO_PREPASS = "auto_prepass"
    EDIT = "edit"
    REPLACE_ALL = "replace_all"


class GateStatus(StrEnum):
    ACCEPTED = "accepted"
    ISOLATED = "isolated"
    REJECTED = "rejected"


@dataclass(frozen=True, slots=True)
class PageRange:
    start: int
    end: int

    def __post_init__(self) -> None:
        if self.start <= 0 or self.end <= 0:
            raise ValidationError("page numbers must be positive")
        if self.end < self.start:
            raise ValidationError("page range end cannot precede start")

    def union(self, other: PageRange) -> PageRange:
        return PageRange(min(self.start, other.start), max(self.end, other.end))

    def label(self) -> str:
        return str(self.start) if self.start == self.end else f"{self.start}-{self.end}"


@dataclass(slots=True)
class OcrPage:
    index: int
    markdown: str
    dimensions: dict[str, Any] | None = None
    confidence: dict[str, Any] | None = None
    images: list[Any] = field(default_factory=list)
    tables: list[Any] = field(default_factory=list)
    header: str | None = None
    footer: str | None = None

    def __post_init__(self) -> None:
        if self.index <= 0:
            raise ValidationError("normalized OCR page index must be positive")


@dataclass(slots=True)
class Block:
    id: str
    type: BlockType
    text: str
    pages: PageRange | None
    source_ids: list[str] = field(default_factory=list)
    confidence: float | None = None
    attrs: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.type in EMITTED_BLOCK_TYPES and self.pages is None:
            raise ValidationError(f"emitted block {self.id!r} requires page provenance")

    def require_provenance(self) -> PageRange:
        if self.pages is None:
            raise ValidationError(f"block {self.id!r} is missing page provenance")
        return self.pages


@dataclass(slots=True)
class EditProposal:
    type: MutationType
    block_id: str
    before: str
    after: str
    rationale: str = ""
    scope: str = "single"
    trigger: EditTrigger = EditTrigger.EDIT


@dataclass(slots=True)
class GateDecision:
    status: GateStatus
    proposal: EditProposal
    reason: str
    diff_stats: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class DocumentModel:
    source_pdf: str
    page_count: int
    pages: list[OcrPage]
    blocks: list[Block]
    warnings: list[dict[str, Any] | str] = field(default_factory=list)
    processing_summary: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate_provenance(self) -> None:
        for block in self.blocks:
            block.require_provenance()

    def block_by_id(self, block_id: str) -> Block | None:
        return next((block for block in self.blocks if block.id == block_id), None)

    def active_blocks(self) -> list[Block]:
        return [block for block in self.blocks if not block.attrs.get("excluded")]

    def emitted_blocks(self) -> list[Block]:
        return [
            block
            for block in self.blocks
            if block.type in EMITTED_BLOCK_TYPES and not block.attrs.get("excluded")
        ]
