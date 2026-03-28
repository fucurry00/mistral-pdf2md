"""Tests for the chunker module."""

from pathlib import Path

from proofread_ocr.chunker import (
    chunk_document,
    estimate_tokens,
)


FIXTURES = Path(__file__).parent / "fixtures"


class TestEstimateTokens:
    def test_empty_string(self):
        assert estimate_tokens("") == 0

    def test_english_text(self):
        text = "hello world " * 100  # 1200 chars
        tokens = estimate_tokens(text)
        assert tokens == 1200 // 4  # English: 4 chars/token

    def test_japanese_text(self):
        text = "数学的な関数の定義" * 50  # 450 chars, heavily CJK
        tokens = estimate_tokens(text)
        assert tokens == len(text) // 3  # CJK: 3 chars/token


class TestChunkDocument:
    def test_empty_document(self):
        chunks, manifest = chunk_document("")
        assert len(chunks) == 0
        assert manifest.total_chunks == 0

    def test_single_section_fits_in_budget(self):
        text = "## Section 1\n\nSome content here.\n"
        chunks, manifest = chunk_document(text, chunk_size_tokens=1000)
        assert manifest.total_chunks == 1
        assert "Section 1" in manifest.chunks[0].section

    def test_multiple_sections_split(self):
        # Create sections that each exceed 50 tokens when combined
        section1 = "## Section 1\n\n" + "word " * 100 + "\n"
        section2 = "## Section 2\n\n" + "word " * 100 + "\n"
        section3 = "## Section 3\n\n" + "word " * 100 + "\n"
        text = section1 + section2 + section3
        # Budget too small to fit all three
        chunks, manifest = chunk_document(text, chunk_size_tokens=200)
        assert manifest.total_chunks >= 2

    def test_overlap_markers_present(self):
        section1 = "## Section 1\n\n" + "word " * 100 + "\n"
        section2 = "## Section 2\n\n" + "word " * 100 + "\n"
        text = section1 + section2
        chunks, manifest = chunk_document(text, chunk_size_tokens=200, overlap_lines=3)
        if manifest.total_chunks >= 2:
            # Second chunk should have before-overlap
            assert "<!-- OVERLAP_START -->" in chunks[1]
            assert "<!-- OVERLAP_END -->" in chunks[1]
            # First chunk should have after-overlap
            assert "<!-- OVERLAP_START -->" in chunks[0]

    def test_chunk_meta_present(self):
        text = "## Section 1\n\nContent\n"
        chunks, manifest = chunk_document(text)
        assert "<!-- CHUNK_META" in chunks[0]
        assert 'chunk_id: 001' in chunks[0]

    def test_no_headings_single_chunk(self):
        text = "Just plain text without any headings.\n" * 10
        chunks, manifest = chunk_document(text, chunk_size_tokens=10000)
        assert manifest.total_chunks == 1

    def test_manifest_metadata(self):
        text = "## S1\n\nContent1\n\n## S2\n\nContent2\n"
        _, manifest = chunk_document(
            text, chunk_size_tokens=5000, overlap_lines=3, source_name="test.md",
        )
        assert manifest.source == "test.md"
        assert manifest.chunk_size_target == 5000
        assert manifest.overlap_lines == 3

    def test_subsection_fallback(self):
        # One large ## section with ### subsections
        text = "## Big Section\n\n"
        text += "### Sub A\n\n" + "word " * 200 + "\n\n"
        text += "### Sub B\n\n" + "word " * 200 + "\n\n"
        text += "### Sub C\n\n" + "word " * 200 + "\n"
        # Budget too small for the whole section
        chunks, manifest = chunk_document(text, chunk_size_tokens=400)
        assert manifest.total_chunks >= 2

    def test_sample_fixture(self):
        sample_path = FIXTURES / "sample_input.md"
        text = sample_path.read_text(encoding="utf-8")
        chunks, manifest = chunk_document(text, chunk_size_tokens=500)
        assert manifest.total_chunks >= 2
        # Verify all sections are covered
        all_chunk_text = "\n".join(chunks)
        assert "Measurable Functions" in all_chunk_text
        assert "Nonnegative Functions" in all_chunk_text

    def test_manifest_json_roundtrip(self, tmp_path):
        text = "## S1\n\nContent\n\n## S2\n\nMore content\n"
        _, manifest = chunk_document(text, source_name="test.md")
        json_path = tmp_path / "manifest.json"
        manifest.save(json_path)

        from proofread_ocr.models import ChunkManifest
        loaded = ChunkManifest.load(json_path)
        assert loaded.total_chunks == manifest.total_chunks
        assert loaded.source == manifest.source
        assert len(loaded.chunks) == len(manifest.chunks)
