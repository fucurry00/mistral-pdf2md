import json

import pytest

from pdf_curator.editing.orchestrator import process_proposals
from pdf_curator.editing.planning import build_global_plan, reconcile_document
from pdf_curator.errors import ValidationError
from pdf_curator.models import Block, BlockType, DocumentModel, PageRange
from pdf_curator.render.markdown import render_curated_markdown


def test_renderer_emits_required_metadata_sources_and_pointer_fallbacks():
    blocks = [
        Block("title", BlockType.TITLE, "# Lecture", PageRange(1, 1)),
        Block("body", BlockType.PARAGRAPH, "Author terminology stays.", PageRange(1, 1)),
        Block(
            "figure",
            BlockType.FIGURE_CAPTION,
            "Figure 1: Exact caption",
            PageRange(2, 2),
        ),
        Block(
            "table",
            BlockType.TABLE,
            "[tbl-0.html](tbl-0.html)",
            PageRange(2, 2),
            attrs={"broken": True},
        ),
        Block(
            "formula",
            BlockType.PARAGRAPH,
            "E = mc?",
            PageRange(2, 2),
            attrs={"visual_type": "formula", "low_confidence": True},
        ),
    ]
    document = DocumentModel(
        "source.pdf",
        2,
        [],
        blocks,
        processing_summary={"gate": {"accepted_content_add": 0}},
    )
    with pytest.raises(ValidationError, match="gated provenance annotation"):
        render_curated_markdown(document)
    reconciliation = reconcile_document(document, build_global_plan(document))
    process_proposals(document, reconciliation.proposals)
    text = render_curated_markdown(document)
    metadata = json.loads(text.split("---", 2)[1])
    required = {
        "title",
        "source_pdf",
        "page_count",
        "section_index",
        "glossary",
        "processing_summary",
        "warnings",
    }
    assert required <= metadata.keys()
    assert metadata["instructor"] == "uncertain"
    assert "Source: PDF p.1-2" in text
    assert "<!-- PDF p.1 -->" in text
    assert "<!-- PDF p.2 -->" in text
    assert "Figure 1: Exact caption\n\n[Figure on PDF p.2]" in text
    assert "[Table on PDF p.2]" in text
    assert "[Formula on PDF p.2]" in text
    assert "AI Note" not in text
    assert "Author terminology stays." in text
