import pytest

from pdf_curator.errors import ValidationError
from pdf_curator.models import Block, BlockType, DocumentModel, PageRange


def test_page_range_validation_and_union():
    with pytest.raises(ValidationError):
        PageRange(0, 1)
    with pytest.raises(ValidationError):
        PageRange(3, 2)
    assert PageRange(2, 3).union(PageRange(1, 5)) == PageRange(1, 5)


def test_document_provenance_fails_closed():
    with pytest.raises(ValidationError, match="requires page provenance"):
        Block("missing", BlockType.PARAGRAPH, "lost", None)

    valid = Block("b1", BlockType.PARAGRAPH, "source", PageRange(1, 1))
    document = DocumentModel("source.pdf", 1, [], [valid])
    document.validate_provenance()

    corrupted = Block("b2", BlockType.UNKNOWN, "lost", PageRange(1, 1))
    corrupted.pages = None
    document.blocks.append(corrupted)
    with pytest.raises(ValidationError, match="missing page provenance"):
        document.validate_provenance()
