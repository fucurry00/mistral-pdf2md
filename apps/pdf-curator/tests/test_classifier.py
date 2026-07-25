from pdf_curator.blocks.classify import classify_text
from pdf_curator.blocks.split import split_pages_into_blocks
from pdf_curator.models import BlockType
from pdf_curator.models import OcrPage


def test_markdown_taxonomy_classification():
    assert classify_text("# Title") is BlockType.TITLE
    assert classify_text("## Heading") is BlockType.HEADING
    assert classify_text("- item") is BlockType.LIST_ITEM
    assert classify_text("1. item") is BlockType.LIST_ITEM
    assert classify_text("| a | b |\n| - | - |") is BlockType.TABLE
    assert classify_text("![x](img.png)") is BlockType.FIGURE_CAPTION
    assert classify_text("Figure 2: Result") is BlockType.FIGURE_CAPTION


def test_boundary_noise_and_unknown_classification():
    assert classify_text("12", position="last") is BlockType.PAGE_NUMBER
    assert (
        classify_text("Course", position="header", repeated_texts={"course"})
        is BlockType.HEADER_FOOTER
    )
    assert classify_text("§") is BlockType.UNKNOWN


def test_consecutive_markdown_table_rows_stay_in_one_block():
    blocks = split_pages_into_blocks(
        [OcrPage(1, "| a | b |\n| --- | --- |\n| 1 | 2 |")]
    )
    assert len(blocks) == 1
    assert blocks[0].type is BlockType.TABLE
    assert blocks[0].text.count("\n") == 2
