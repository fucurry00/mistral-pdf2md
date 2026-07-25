import pytest

from pdf_curator.editing.gate import evaluate_proposal
from pdf_curator.models import (
    Block,
    BlockType,
    EditProposal,
    EditTrigger,
    GateStatus,
    MutationType,
    PageRange,
)


@pytest.fixture
def block():
    return Block(
        "b1",
        BlockType.PARAGRAPH,
        "A recieve error\nneeds repair. item Important body text.",
        PageRange(1, 1),
    )


def proposal(mutation, before, after, **kwargs):
    return EditProposal(mutation, "b1", before, after, **kwargs)


def test_mutation_channels_are_exactly_the_three_consensus_triggers():
    assert {trigger.value for trigger in EditTrigger} == {
        "auto_prepass",
        "edit",
        "replace_all",
    }


def test_missing_before_and_content_add_are_rejected(block):
    missing = evaluate_proposal(proposal(MutationType.OCR_CHAR_FIX, "absent", "fixed"), block)
    assert missing.status is GateStatus.REJECTED
    assert "absent" in missing.reason

    addition = evaluate_proposal(
        proposal(
            MutationType.CONTENT_ADD,
            "Important body text.",
            "Important body text. New prose.",
        ),
        block,
    )
    assert addition.status is GateStatus.REJECTED


def test_system_provenance_annotations_are_separate_from_content_add(block):
    decision = evaluate_proposal(
        proposal(
            MutationType.PROVENANCE_ANNOTATION,
            "",
            "Source: PDF p.1-2",
            scope="system",
        ),
        block,
    )
    assert decision.status is GateStatus.ACCEPTED


def test_prepass_deletion_requires_internal_evidence(block):
    forged = proposal(
        MutationType.HEADER_FOOTER_REMOVE,
        block.text,
        "",
        trigger=EditTrigger.AUTO_PREPASS,
    )
    assert evaluate_proposal(forged, block).status is GateStatus.REJECTED
    block.attrs["prepass_evidence"] = {
        "mutation": MutationType.HEADER_FOOTER_REMOVE.value
    }
    assert evaluate_proposal(forged, block).status is GateStatus.ACCEPTED


@pytest.mark.parametrize(
    ("mutation", "before", "after"),
    [
        (MutationType.LINEBREAK_REPAIR, "needs repair.", "needs\nrepair."),
        (MutationType.LIST_RESTORE, "item", "- item"),
        (MutationType.OCR_CHAR_FIX, "recieve", "receive"),
    ],
)
def test_safe_local_mutations_are_accepted(block, mutation, before, after):
    decision = evaluate_proposal(proposal(mutation, before, after), block)
    assert decision.status is GateStatus.ACCEPTED


def test_bulk_ocr_fix_requires_replace_all_trigger(block):
    edit = proposal(MutationType.BULK_OCR_FIX, "recieve", "receive")
    assert evaluate_proposal(edit, block).status is GateStatus.ISOLATED
    replace_all = proposal(
        MutationType.BULK_OCR_FIX,
        "recieve",
        "receive",
        trigger=EditTrigger.REPLACE_ALL,
    )
    assert evaluate_proposal(replace_all, block).status is GateStatus.ACCEPTED


def test_linebreak_repair_cannot_merge_distinct_words(block):
    block.text = "foo bar"
    decision = evaluate_proposal(
        proposal(MutationType.LINEBREAK_REPAIR, "foo bar", "foobar"), block
    )
    assert decision.status is GateStatus.REJECTED


@pytest.mark.parametrize(
    "mutation",
    [
        MutationType.PARAGRAPH_RESTRUCTURE,
        MutationType.CONTENT_DELETE,
    ],
)
def test_grey_zone_mutations_are_isolated(block, mutation):
    decision = evaluate_proposal(
        proposal(mutation, "Important body text.", "Important text."), block
    )
    assert decision.status is GateStatus.ISOLATED


@pytest.mark.parametrize("mutation", [MutationType.SUMMARIZE, MutationType.PARAPHRASE])
def test_meaning_changing_mutations_are_rejected_and_confidence_is_irrelevant(block, mutation):
    decision = evaluate_proposal(
        proposal(mutation, "Important body text.", "Short version", rationale="confidence=1.0"),
        block,
    )
    assert decision.status is GateStatus.REJECTED
