import json
from pathlib import Path

from pdf_curator.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


def test_fixture_mode_needs_no_api_key_and_writes_curated(tmp_path, monkeypatch):
    monkeypatch.delenv("MISTRAL_API_KEY", raising=False)
    output = tmp_path / "output"
    exit_code = main(
        [
            str(FIXTURES / "simple.pdf"),
            str(output),
            "--from-ocr-json",
            str(FIXTURES / "simple_ocr.json"),
        ]
    )
    assert exit_code == 0
    assert (output / "curated.md").is_file()


def test_missing_input_returns_nonzero(tmp_path, capsys):
    exit_code = main(
        [
            str(tmp_path / "missing.pdf"),
            str(tmp_path / "output"),
            "--from-ocr-json",
            str(FIXTURES / "simple_ocr.json"),
        ]
    )
    assert exit_code == 1
    assert "does not exist" in capsys.readouterr().err


def test_page_selection_is_reflected_in_metadata_and_sources(tmp_path):
    output = tmp_path / "selected"
    assert (
        main(
            [
                str(FIXTURES / "simple.pdf"),
                str(output),
                "--from-ocr-json",
                str(FIXTURES / "simple_ocr.json"),
                "--pages",
                "2",
            ]
        )
        == 0
    )
    text = (output / "curated.md").read_text()
    metadata = json.loads(text.split("---", 2)[1])
    assert metadata["page_count"] == 1
    assert metadata["section_index"][0]["pages"] == "2"
    assert "Source: PDF p.2" in text


def test_debug_flag_creates_debug_directory(tmp_path):
    output = tmp_path / "debugged"
    assert (
        main(
            [
                str(FIXTURES / "simple.pdf"),
                str(output),
                "--from-ocr-json",
                str(FIXTURES / "simple_ocr.json"),
                "--debug",
            ]
        )
        == 0
    )
    assert (output / "debug").is_dir()


def test_invalid_retention_floor_returns_nonzero(tmp_path, capsys):
    output = tmp_path / "invalid-floor"
    exit_code = main(
        [
            str(FIXTURES / "simple.pdf"),
            str(output),
            "--from-ocr-json",
            str(FIXTURES / "simple_ocr.json"),
            "--min-content-retention",
            "1.1",
        ]
    )
    assert exit_code == 1
    assert "between 0 and 1" in capsys.readouterr().err
    assert (output / "debug" / "warnings.json").is_file()
