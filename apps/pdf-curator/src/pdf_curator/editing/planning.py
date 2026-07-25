"""Read-only global planning and reconciliation views for the v1 pipeline."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from pdf_curator.models import (
    Block,
    BlockType,
    DocumentModel,
    EMITTED_BLOCK_TYPES,
    EditProposal,
    EditTrigger,
    MutationType,
)


@dataclass(frozen=True, slots=True)
class Chunk:
    id: str
    block_ids: tuple[str, ...]
    pages: str


@dataclass(frozen=True, slots=True)
class GlobalPlan:
    outline: tuple[dict[str, Any], ...]
    glossary: dict[str, Any]
    noise_candidates: tuple[str, ...]
    chunks: tuple[Chunk, ...]


@dataclass(frozen=True, slots=True)
class ReconciliationResult:
    proposals: tuple[EditProposal, ...]
    warnings: tuple[dict[str, Any], ...]


def build_chunks(blocks: list[Block]) -> tuple[Chunk, ...]:
    groups: list[list[Block]] = []
    current: list[Block] = []
    for block in blocks:
        if block.attrs.get("excluded") or block.type not in EMITTED_BLOCK_TYPES:
            continue
        if block.type in {BlockType.TITLE, BlockType.HEADING} and current:
            groups.append(current)
            current = []
        current.append(block)
    if current:
        groups.append(current)

    chunks: list[Chunk] = []
    for index, group in enumerate(groups, 1):
        pages = group[0].require_provenance()
        for block in group[1:]:
            pages = pages.union(block.require_provenance())
        chunks.append(
            Chunk(
                id=f"chunk-{index:03d}",
                block_ids=tuple(block.id for block in group),
                pages=pages.label(),
            )
        )
    return tuple(chunks)


def build_global_plan(document: DocumentModel) -> GlobalPlan:
    document.validate_provenance()
    outline = tuple(
        {
            "block_id": block.id,
            "heading": re.sub(r"^#{1,6}\s+", "", block.text).strip(),
            "pages": block.require_provenance().label(),
        }
        for block in document.blocks
        if block.type in {BlockType.TITLE, BlockType.HEADING}
        and not block.attrs.get("excluded")
    )
    return GlobalPlan(
        outline=outline,
        glossary=dict(document.metadata.get("glossary", {})),
        noise_candidates=tuple(
            block.id for block in document.blocks if block.type is BlockType.UNKNOWN
        ),
        chunks=build_chunks(document.blocks),
    )


def reconcile_document(
    document: DocumentModel, plan: GlobalPlan
) -> ReconciliationResult:
    """Propose safe seam repairs and warn on ambiguous cross-chunk issues."""

    document.validate_provenance()
    proposals: list[EditProposal] = []
    warnings: list[dict[str, Any]] = []
    previous_heading_level: int | None = None
    for item in plan.outline:
        block = document.block_by_id(item["block_id"])
        if block is None:
            warnings.append(
                {"type": "missing_outline_block", "block_id": item["block_id"]}
            )
            continue
        match = re.match(r"^(#{1,6})\s+(.+)$", block.text, re.DOTALL)
        if match:
            level = len(match.group(1))
            if previous_heading_level is not None and level > previous_heading_level + 1:
                target_level = previous_heading_level + 1
                proposals.append(
                    EditProposal(
                        type=MutationType.HEADING_LEVEL_NORMALIZE,
                        block_id=block.id,
                        before=block.text,
                        after=f"{'#' * target_level} {match.group(2)}",
                        rationale="normalize heading level across chunk seam",
                        scope="reconciliation",
                        trigger=EditTrigger.EDIT,
                    )
                )
                level = target_level
            previous_heading_level = level

    for chunk in plan.chunks:
        if not chunk.block_ids:
            continue
        proposals.append(
            EditProposal(
                type=MutationType.PROVENANCE_ANNOTATION,
                block_id=chunk.block_ids[0],
                before="",
                after=f"Source: PDF p.{chunk.pages}",
                rationale="derive section source from block page tags",
                scope="system",
                trigger=EditTrigger.EDIT,
            )
        )

    seen_pages: set[int] = set()
    for block in document.emitted_blocks():
        page = block.require_provenance().start
        if page in seen_pages:
            continue
        seen_pages.add(page)
        proposals.append(
            EditProposal(
                type=MutationType.PROVENANCE_ANNOTATION,
                block_id=block.id,
                before="",
                after=f"<!-- PDF p.{page} -->",
                rationale="derive page boundary from block page tags",
                scope="system",
                trigger=EditTrigger.EDIT,
            )
        )

    emitted_blocks = document.emitted_blocks()
    for left, right in zip(emitted_blocks, emitted_blocks[1:]):
        if (
            left.text.strip()
            and left.text.strip() == right.text.strip()
            and left.require_provenance() != right.require_provenance()
        ):
            warnings.append(
                {
                    "type": "possible_chunk_seam_duplicate",
                    "block_ids": [left.id, right.id],
                    "pages": left.require_provenance()
                    .union(right.require_provenance())
                    .label(),
                }
            )
    return ReconciliationResult(tuple(proposals), tuple(warnings))
