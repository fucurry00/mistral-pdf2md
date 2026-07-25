"""Sequential v1 proposal orchestration through one gate."""

from __future__ import annotations

from collections.abc import Iterable

from pdf_curator.editing.apply import apply_decision
from pdf_curator.editing.gate import evaluate_proposal
from pdf_curator.models import DocumentModel, EditProposal, GateDecision, GateStatus


def process_proposals(
    document: DocumentModel,
    proposals: Iterable[EditProposal],
) -> tuple[list[GateDecision], list[dict[str, str]]]:
    decisions: list[GateDecision] = []
    applied: list[dict[str, str]] = []
    for proposal in proposals:
        block = document.block_by_id(proposal.block_id)
        decision = evaluate_proposal(proposal, block)
        decisions.append(decision)
        if block is not None:
            diff = apply_decision(decision, block)
            if diff is not None:
                applied.append(diff)
        if decision.status is GateStatus.ISOLATED:
            document.warnings.append(
                {
                    "type": "isolated_edit",
                    "block_id": proposal.block_id,
                    "mutation": proposal.type.value,
                    "reason": decision.reason,
                }
            )
    return decisions, applied
