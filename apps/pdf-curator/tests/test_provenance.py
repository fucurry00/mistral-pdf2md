import json
from pathlib import Path

import pytest

from pdf_curator.blocks.provenance import merge_adjacent_blocks
from pdf_curator.blocks.split import split_pages_into_blocks
from pdf_curator.errors import ValidationError
from pdf_curator.models import Block, BlockType, DocumentModel, OcrPage, PageRange
from pdf_curator.pipeline import run_pipeline
from pdf_curator.render.markdown import render_curated_markdown

FIXTURES = Path(__file__).parent / "fixtures"


def test_split_and_merge_preserve_page_ranges():
    blocks = split_pages_into_blocks([OcrPage(1, "First\n\nSecond")])
    assert all(block.pages == PageRange(1, 1) for block in blocks)
    merged = merge_adjacent_blocks(
        Block("a", BlockType.PARAGRAPH, "cross", PageRange(1, 1)),
        Block("b", BlockType.PARAGRAPH, "page", PageRange(2, 2)),
    )
    assert merged.pages == PageRange(1, 2)
    assert merged.text == "cross page"


def test_renderer_rejects_hand_authored_section_index():
    document = DocumentModel(
        "source.pdf",
        1,
        [],
        [Block("b", BlockType.HEADING, "## Correct", PageRange(1, 1))],
    )
    with pytest.raises(ValidationError, match="section_index"):
        render_curated_markdown(
            document,
            section_index_override=[{"id": "s001", "heading": "Wrong", "pages": "2"}],
        )


def test_page_mixing_golden_fixture(tmp_path):
    result = run_pipeline(
        FIXTURES / "simple.pdf",
        tmp_path,
        from_ocr_json=FIXTURES / "page_mixing_ocr.json",
    )
    text = result.curated_path.read_text()
    assert "Source: PDF p.1" in text
    assert "<!-- PDF p.1 -->" in text
    assert "ALPHA-PAGE-ONE-SENTINEL" in text
    assert "Source: PDF p.2" in text
    assert "<!-- PDF p.2 -->" in text
    assert "BETA-PAGE-TWO-SENTINEL" in text
    metadata = json.loads(text.split("---", 2)[1])
    assert [entry["pages"] for entry in metadata["section_index"]] == ["1", "2"]
