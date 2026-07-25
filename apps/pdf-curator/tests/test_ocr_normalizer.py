from types import SimpleNamespace

import pytest

from pdf_curator.errors import ValidationError
from pdf_curator.ocr.response_normalizer import normalize_ocr_response


def test_normalizer_accepts_dict_response_and_preserves_fields():
    pages = normalize_ocr_response(
        {
            "pages": [
                {
                    "index": 0,
                    "markdown": "text",
                    "images": [{"id": "image"}],
                    "dimensions": {"width": 10},
                }
            ]
        }
    )
    assert pages[0].index == 1
    assert pages[0].markdown == "text"
    assert pages[0].images == [{"id": "image"}]
    assert pages[0].dimensions == {"width": 10}


def test_normalizer_accepts_object_response_and_text_fallback():
    response = SimpleNamespace(
        pages=[
            SimpleNamespace(
                index=1,
                text="object text",
                images=[],
                tables=[],
                dimensions=SimpleNamespace(width=20),
                confidence_scores=None,
                header=None,
                footer=None,
            )
        ]
    )
    page = normalize_ocr_response(response)[0]
    assert page.index == 2
    assert page.markdown == "object text"
    assert page.dimensions == {"width": 20}


def test_normalizer_rejects_page_without_content_or_metadata():
    with pytest.raises(ValidationError, match="neither markdown/text"):
        normalize_ocr_response({"pages": [{"index": 0}]})
