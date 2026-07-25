import json
from pathlib import Path

import pytest

from pdf_curator.errors import ValidationError
from pdf_curator.pipeline import run_pipeline

FIXTURES = Path(__file__).parent / "fixtures"
EXPECTED = {
    "ocr_raw.json",
    "pages.json",
    "blocks.json",
    "edit_candidates.json",
    "gate_decisions.json",
    "applied_diffs.json",
    "warnings.json",
}


def test_debug_writes_all_trace_files(tmp_path):
    result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path,
        from_ocr_json=FIXTURES / "simple_ocr.json",
        debug=True,
    )
    assert result.debug_dir is not None
    assert {path.name for path in result.debug_dir.iterdir()} == EXPECTED
    for path in result.debug_dir.iterdir():
        json.loads(path.read_text())
    blocks = json.loads((result.debug_dir / "blocks.json").read_text())
    assert all(block["id"] and block["pages"] for block in blocks)


def test_failed_validation_writes_debug_without_flag(tmp_path):
    invalid = tmp_path / "invalid.json"
    invalid.write_text('{"pages": [{"index": 0}]}')
    output = tmp_path / "output"
    with pytest.raises(ValidationError):
        run_pipeline(FIXTURES / "simple.pdf", output, from_ocr_json=invalid)
    assert {path.name for path in (output / "debug").iterdir()} == EXPECTED
