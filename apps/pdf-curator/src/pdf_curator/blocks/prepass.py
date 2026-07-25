"""Generate deterministic pre-pass proposals without mutating source blocks."""

from __future__ import annotations

from collections import Counter
from math import ceil

from pdf_curator.blocks.classify import is_separator, normalize_repeated_text
from pdf_curator.models import Block, BlockType, EditProposal, EditTrigger, MutationType


def propose_prepass(
    blocks: list[Block],
    *,
    page_count: int,
    repeated_threshold: float = 0.6,
) -> list[EditProposal]:
    edge_blocks = [
        block
        for block in blocks
        if block.attrs.get("position") in {"header", "footer", "first", "last"}
    ]
    occurrences: Counter[str] = Counter()
    seen_by_page: set[tuple[str, int]] = set()
    for block in edge_blocks:
        pages = block.require_provenance()
        key = normalize_repeated_text(block.text)
        page_key = (key, pages.start)
        if key and page_key not in seen_by_page:
            occurrences[key] += 1
            seen_by_page.add(page_key)
    minimum_pages = max(2, ceil(page_count * repeated_threshold))
    repeated = {text for text, count in occurrences.items() if count >= minimum_pages}

    proposals: list[EditProposal] = []
    for block in blocks:
        normalized = normalize_repeated_text(block.text)
        mutation: MutationType | None = None
        reason = ""
        if (
            normalized in repeated
            and block.type not in {BlockType.TITLE, BlockType.HEADING}
            and block.attrs.get("position")
            in {"header", "footer", "first", "last"}
        ):
            mutation = MutationType.HEADER_FOOTER_REMOVE
            reason = f"repeated on at least {minimum_pages} pages"
        elif block.type is BlockType.PAGE_NUMBER:
            mutation = MutationType.PAGE_NUMBER_REMOVE
            reason = "standalone page number at page boundary"
        elif is_separator(block.text):
            mutation = MutationType.HEADER_FOOTER_REMOVE
            reason = "safe ornamental separator pattern"

        if mutation is not None:
            block.attrs["prepass_evidence"] = {
                "mutation": mutation.value,
                "reason": reason,
            }
            proposals.append(
                EditProposal(
                    type=mutation,
                    block_id=block.id,
                    before=block.text,
                    after="",
                    rationale=reason,
                    scope="document",
                    trigger=EditTrigger.AUTO_PREPASS,
                )
            )
    return proposals
