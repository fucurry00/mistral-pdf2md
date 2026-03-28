"""Tests for the merger module."""

from pathlib import Path

from proofread_ocr.merger import (
    _extract_annotations,
    _strip_all_annotations,
    _strip_markers,
    merge_results,
    validate_latex,
)
from proofread_ocr.models import ChunkManifest, ChunkMeta, ProofreadResult


class TestValidateLatex:
    def test_balanced_inline(self):
        text = "We have $x + y$ and $z = 0$."
        assert validate_latex(text) == []

    def test_unbalanced_inline(self):
        text = "Missing close $x + y."
        warnings = validate_latex(text)
        assert len(warnings) == 1
        assert "Unmatched inline $" in warnings[0]

    def test_balanced_env(self):
        text = "\\begin{align} x &= 1 \\end{align}"
        assert validate_latex(text) == []

    def test_unbalanced_env(self):
        text = "\\begin{align} x &= 1"
        warnings = validate_latex(text)
        assert any("Unclosed" in w for w in warnings)

    def test_mismatched_env(self):
        text = "\\begin{align} x \\end{equation}"
        warnings = validate_latex(text)
        assert len(warnings) >= 1


class TestStripMarkers:
    def test_strip_overlap(self):
        text = "before\n<!-- OVERLAP_START -->\noverlap content\n<!-- OVERLAP_END -->\nafter"
        result = _strip_markers(text)
        assert "overlap content" not in result
        assert "before" in result
        assert "after" in result

    def test_strip_chunk_meta(self):
        text = '<!-- CHUNK_META\nchunk_id: 001\nsection: "test"\n-->\nactual content'
        result = _strip_markers(text)
        assert "CHUNK_META" not in result
        assert "actual content" in result

    def test_no_markers(self):
        text = "plain text without markers"
        assert _strip_markers(text) == text


class TestExtractAnnotations:
    def test_fixed_annotation(self):
        text = "homomorphism <!-- FIXED: homornorphism → homomorphism | OCR: rn → m -->"
        entries = _extract_annotations(text)
        assert len(entries) == 1
        assert entries[0].confidence == "FIXED"
        assert entries[0].original == "homornorphism"
        assert entries[0].corrected == "homomorphism"

    def test_uncertain_annotation(self):
        text = "$G$-invariant <!-- UNCERTAIN: G-invariant → $G$-invariant | LaTeX正規化? -->"
        entries = _extract_annotations(text)
        assert len(entries) == 1
        assert entries[0].confidence == "UNCERTAIN"

    def test_mixed_annotations(self):
        text = (
            "## §1.1\n"
            "word1 <!-- FIXED: a → b | reason1 -->\n"
            "word2 <!-- UNCERTAIN: c → d | reason2 -->\n"
        )
        entries = _extract_annotations(text)
        assert len(entries) == 2
        assert entries[0].section == "§1.1"

    def test_no_annotations(self):
        text = "clean text with no corrections"
        assert _extract_annotations(text) == []


class TestStripAnnotations:
    def test_strip_fixed(self):
        text = "homo <!-- FIXED: a → b | r --> rest"
        result = _strip_all_annotations(text)
        assert "FIXED" not in result
        assert "homo" in result
        assert "rest" in result

    def test_strip_uncertain(self):
        text = "text <!-- UNCERTAIN: x → y | z --> more"
        result = _strip_all_annotations(text)
        assert "UNCERTAIN" not in result


class TestMergeResults:
    def _make_manifest(self, n_chunks=2) -> ChunkManifest:
        chunks = [
            ChunkMeta(
                id=f"{i+1:03d}", section=f"Section {i+1}",
                prev_section="", next_section="",
                line_start=i*10+1, line_end=(i+1)*10,
                estimated_tokens=100,
            )
            for i in range(n_chunks)
        ]
        return ChunkManifest(
            source="test.md", total_chunks=n_chunks,
            chunk_size_target=1000, overlap_lines=5, chunks=chunks,
        )

    def test_basic_merge(self, tmp_path):
        manifest = self._make_manifest(2)
        chunks_dir = tmp_path / "chunks"
        results_dir = tmp_path / "results"
        chunks_dir.mkdir()
        results_dir.mkdir()

        # Write chunk files
        (chunks_dir / "chunk_001.md").write_text(
            "<!-- CHUNK_META\nchunk_id: 001\n-->\nChunk 1 content"
        )
        (chunks_dir / "chunk_002.md").write_text(
            "<!-- CHUNK_META\nchunk_id: 002\n-->\nChunk 2 content"
        )

        # Write result files
        r1 = ProofreadResult(chunk_id="001", success=True, output_text=(
            "<!-- CHUNK_META\nchunk_id: 001\n-->\n"
            "Proofread chunk 1 <!-- FIXED: a → b | test -->"
        ))
        r1.save(results_dir / "chunk_001.json")
        r2 = ProofreadResult(chunk_id="002", success=True, output_text=(
            "<!-- CHUNK_META\nchunk_id: 002\n-->\n"
            "Proofread chunk 2"
        ))
        r2.save(results_dir / "chunk_002.json")

        output_path = tmp_path / "output" / "proofread.md"
        out, diff, stats = merge_results(
            manifest=manifest,
            results_dir=results_dir,
            chunks_dir=chunks_dir,
            output_path=output_path,
        )

        assert out.exists()
        content = out.read_text(encoding="utf-8")
        assert "Proofread chunk 1" in content
        assert "Proofread chunk 2" in content
        assert "CHUNK_META" not in content

        assert diff.exists()
        diff_content = diff.read_text(encoding="utf-8")
        assert "a" in diff_content  # FIXED entry should appear

        assert stats.exists()

    def test_failed_chunk_fallback(self, tmp_path):
        manifest = self._make_manifest(1)
        chunks_dir = tmp_path / "chunks"
        results_dir = tmp_path / "results"
        chunks_dir.mkdir()
        results_dir.mkdir()

        (chunks_dir / "chunk_001.md").write_text(
            "<!-- CHUNK_META\nchunk_id: 001\n-->\nOriginal content"
        )

        # No result file -> should fall back to original
        output_path = tmp_path / "output" / "proofread.md"
        out, _, _ = merge_results(
            manifest=manifest,
            results_dir=results_dir,
            chunks_dir=chunks_dir,
            output_path=output_path,
        )

        content = out.read_text(encoding="utf-8")
        assert "Original content" in content
