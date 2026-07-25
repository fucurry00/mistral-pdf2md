"""Apply only accepted gate decisions to referenced blocks."""

from __future__ import annotations

from pdf_curator.models import (
    Block,
    BlockType,
    EditTrigger,
    GateDecision,
    GateStatus,
    MutationType,
)


def apply_decision(decision: GateDecision, block: Block) -> dict[str, str] | None:
    if decision.status is not GateStatus.ACCEPTED:
        return None
    proposal = decision.proposal
    before = block.text
    if proposal.type is MutationType.PROVENANCE_ANNOTATION:
        annotations = block.attrs.setdefault("provenance_annotations", [])
        if proposal.after not in annotations:
            annotations.append(proposal.after)
        return {
            "block_id": block.id,
            "mutation": proposal.type.value,
            "trigger": proposal.trigger.value,
            "before": "",
            "after": proposal.after,
        }
    if proposal.type in {
        MutationType.HEADER_FOOTER_REMOVE,
        MutationType.PAGE_NUMBER_REMOVE,
    }:
        block.attrs["excluded"] = True
        block.attrs["excluded_by"] = proposal.type.value
        block.type = (
            BlockType.HEADER_FOOTER
            if proposal.type is MutationType.HEADER_FOOTER_REMOVE
            else BlockType.PAGE_NUMBER
        )
        after = ""
    elif proposal.type is MutationType.BULK_OCR_FIX or proposal.trigger is EditTrigger.REPLACE_ALL:
        block.text = block.text.replace(proposal.before, proposal.after)
        after = block.text
    else:
        block.text = block.text.replace(proposal.before, proposal.after, 1)
        after = block.text
    return {
        "block_id": block.id,
        "mutation": proposal.type.value,
        "trigger": proposal.trigger.value,
        "before": before,
        "after": after,
    }
