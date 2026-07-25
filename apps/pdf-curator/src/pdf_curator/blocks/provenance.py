"""Provenance-preserving block operations."""

from __future__ import annotations

from pdf_curator.models import Block, BlockType


def merge_adjacent_blocks(left: Block, right: Block, *, separator: str = " ") -> Block:
    pages = left.require_provenance().union(right.require_provenance())
    block_type = left.type if left.type == right.type else BlockType.PARAGRAPH
    return Block(
        id=f"{left.id}+{right.id}",
        type=block_type,
        text=f"{left.text.rstrip()}{separator}{right.text.lstrip()}",
        pages=pages,
        source_ids=[*left.source_ids, *right.source_ids],
        confidence=min(
            value for value in (left.confidence, right.confidence) if value is not None
        )
        if left.confidence is not None or right.confidence is not None
        else None,
        attrs={**left.attrs, **right.attrs},
    )
