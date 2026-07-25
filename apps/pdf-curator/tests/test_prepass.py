from pdf_curator.blocks.prepass import propose_prepass
from pdf_curator.editing.orchestrator import process_proposals
from pdf_curator.models import Block, BlockType, DocumentModel, GateStatus, PageRange


def _block(identifier, text, page, position="body", block_type=BlockType.PARAGRAPH):
    return Block(
        identifier,
        block_type,
        text,
        PageRange(page, page),
        attrs={"position": position},
    )


def test_repeated_edges_and_page_numbers_pass_gate_before_exclusion():
    blocks = [
        _block("h1", "Shared footer", 1, "footer"),
        _block("h2", "Shared footer", 2, "footer"),
        _block("h3", "Shared footer", 3, "footer"),
        _block("single", "Keep this", 1, "header"),
        _block("number", "2", 2, "last", BlockType.PAGE_NUMBER),
        _block("body", "The value 2026 is meaningful.", 2),
    ]
    document = DocumentModel("source.pdf", 3, [], blocks)
    proposals = propose_prepass(blocks, page_count=3)
    decisions, applied = process_proposals(document, proposals)
    assert {block.id for block in document.active_blocks()} == {"single", "body"}
    assert len(proposals) == len(decisions) == len(applied) == 4
    assert all(decision.status is GateStatus.ACCEPTED for decision in decisions)
    assert all(diff["trigger"] == "auto_prepass" for diff in applied)


def test_single_edge_occurrence_and_body_number_are_retained():
    blocks = [
        _block("single", "One-off header", 1, "header"),
        _block("body", "42", 1, "body"),
    ]
    assert propose_prepass(blocks, page_count=3) == []
    assert all(not block.attrs.get("excluded") for block in blocks)
