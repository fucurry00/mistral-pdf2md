from pdf_curator.editing.planning import build_global_plan, reconcile_document
from pdf_curator.editing.orchestrator import process_proposals
from pdf_curator.models import Block, BlockType, DocumentModel, GateStatus, PageRange


def test_global_plan_reconciliation_applies_safe_repairs_through_gate():
    blocks = [
        Block("h1", BlockType.TITLE, "# Title", PageRange(1, 1)),
        Block("p1", BlockType.PARAGRAPH, "Same seam", PageRange(1, 1)),
        Block("h2", BlockType.HEADING, "### Deep heading", PageRange(2, 2)),
        Block("p2", BlockType.PARAGRAPH, "Same seam", PageRange(2, 2)),
    ]
    document = DocumentModel("source.pdf", 2, [], blocks)
    plan = build_global_plan(document)
    assert len(plan.outline) == 2
    assert [chunk.pages for chunk in plan.chunks] == ["1", "2"]
    before = [block.text for block in blocks]
    reconciliation = reconcile_document(document, plan)
    assert [block.text for block in blocks] == before
    decisions, applied = process_proposals(document, reconciliation.proposals)
    assert all(decision.status is GateStatus.ACCEPTED for decision in decisions)
    assert blocks[2].text == "## Deep heading"
    assert any(diff["mutation"] == "provenance_annotation" for diff in applied)
