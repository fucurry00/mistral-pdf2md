import json
from pathlib import Path

import pytest

from pdf_curator.errors import ValidationError
from pdf_curator.models import EditProposal, MutationType
from pdf_curator.pipeline import _enforce_success_metrics, run_pipeline

FIXTURES = Path(__file__).parent / "fixtures"


class StaticProposalClient:
    def __init__(self, proposals):
        self.proposals = proposals

    def propose(self, blocks):
        return list(self.proposals)


class MutatingProposalClient:
    def propose(self, blocks):
        blocks[0].text = "attempted direct rewrite"
        return []


def _assert_sentinel_sources(text, expected):
    source = None
    observed = {}
    for line in text.splitlines():
        if line.startswith("Source: PDF p."):
            source = line.removeprefix("Source: PDF p.")
        for phrase in expected:
            if phrase in line:
                observed[phrase] = source
    assert observed == {phrase: str(page) for phrase, page in expected.items()}


@pytest.mark.parametrize(
    "fixture",
    ["simple_ocr.json", "dense_ocr.json", "mixed_visual_ocr.json"],
)
def test_offline_fixture_pipeline(fixture, tmp_path):
    result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path / fixture,
        from_ocr_json=FIXTURES / fixture,
        debug=True,
    )
    text = result.curated_path.read_text()
    metadata = json.loads(text.split("---", 2)[1])
    assert "Source: PDF p." in text
    if metadata["page_count"] > 1:
        assert "<!-- PDF p." in text
    assert metadata["processing_summary"]["gate"]["accepted_content_add"] == 0
    assert metadata["processing_summary"]["global_planning"]["chunks"] >= 1
    assert metadata["processing_summary"]["source_content_word_retention"] >= 0.7


def test_unsafe_and_missing_before_proposals_do_not_change_source(tmp_path):
    raw = json.loads((FIXTURES / "simple_ocr.json").read_text())
    raw["edit_proposals"] = [{"type": "content_add", "after": "ignored raw path"}]
    proposals = [
        EditProposal(
            MutationType.CONTENT_ADD,
            "b00003",
            "Core ideas remain faithful to the source.",
            "Core ideas remain faithful to the source. Invented explanation.",
        ),
        EditProposal(
            MutationType.OCR_CHAR_FIX,
            "b00003",
            "missing source text",
            "fixed text",
        ),
    ]
    fixture = tmp_path / "unsafe.json"
    fixture.write_text(json.dumps(raw))
    result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path / "output",
        from_ocr_json=fixture,
        debug=True,
        proposal_client=StaticProposalClient(proposals),
    )
    text = result.curated_path.read_text()
    assert "Invented explanation" not in text
    decisions = json.loads((result.debug_dir / "gate_decisions.json").read_text())
    client_decisions = [
        decision
        for decision in decisions
        if decision["proposal"]["block_id"] == "b00003"
        and decision["proposal"]["type"] in {"content_add", "ocr_char_fix"}
    ]
    assert [decision["status"] for decision in client_decisions] == [
        "rejected",
        "rejected",
    ]
    applied = json.loads((result.debug_dir / "applied_diffs.json").read_text())
    assert not any(
        diff["mutation"] in {"content_add", "ocr_char_fix"} for diff in applied
    )
    assert "ignored raw path" not in text


def test_default_noop_ignores_ocr_json_edit_proposals_and_clients_receive_copies(
    tmp_path,
):
    raw = json.loads((FIXTURES / "simple_ocr.json").read_text())
    raw["edit_proposals"] = [
        {"type": "content_add", "after": "raw proposal must stay inert"}
    ]
    fixture = tmp_path / "raw-proposals.json"
    fixture.write_text(json.dumps(raw))

    default_result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path / "default",
        from_ocr_json=fixture,
    )
    assert "raw proposal must stay inert" not in default_result.curated_path.read_text()
    assert default_result.document.processing_summary["llm_editing"] == "NoOpProposalClient"

    mutating_result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path / "copy-boundary",
        from_ocr_json=fixture,
        proposal_client=MutatingProposalClient(),
    )
    assert "attempted direct rewrite" not in mutating_result.curated_path.read_text()


def test_ambiguous_deletion_is_warned_and_content_is_retained(tmp_path):
    raw = json.loads((FIXTURES / "simple_ocr.json").read_text())
    proposals = [
        EditProposal(
            MutationType.CONTENT_DELETE,
            "b00003",
            "Core ideas remain faithful to the source.",
            "",
        )
    ]
    fixture = tmp_path / "deletion.json"
    fixture.write_text(json.dumps(raw))
    result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path / "output",
        from_ocr_json=fixture,
        debug=True,
        proposal_client=StaticProposalClient(proposals),
    )
    assert "Core ideas remain faithful to the source." in result.curated_path.read_text()
    warnings = json.loads((result.debug_dir / "warnings.json").read_text())
    assert any(warning.get("type") == "isolated_edit" for warning in warnings)


def test_wrong_page_sentinel_is_rejected_by_test_owned_golden_assertion(tmp_path):
    raw = json.loads((FIXTURES / "page_mixing_ocr.json").read_text())
    raw["pages"][0]["markdown"], raw["pages"][1]["markdown"] = (
        raw["pages"][1]["markdown"],
        raw["pages"][0]["markdown"],
    )
    fixture = tmp_path / "wrong-page.json"
    fixture.write_text(json.dumps(raw))
    output = tmp_path / "output"
    result = run_pipeline(FIXTURES / "simple.pdf", output, from_ocr_json=fixture)
    with pytest.raises(AssertionError):
        _assert_sentinel_sources(
            result.curated_path.read_text(),
            {"ALPHA-PAGE-ONE-SENTINEL": 1, "BETA-PAGE-TWO-SENTINEL": 2},
        )


def test_success_metric_floors_fail_closed():
    with pytest.raises(ValidationError, match="retention"):
        _enforce_success_metrics(
            retention=0.69,
            minimum_retention=0.7,
            accepted_content_add=0,
        )
    with pytest.raises(ValidationError, match="content_add"):
        _enforce_success_metrics(
            retention=1.0,
            minimum_retention=0.7,
            accepted_content_add=1,
        )
