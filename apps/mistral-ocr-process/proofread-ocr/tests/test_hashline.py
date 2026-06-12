"""Tests for Hashline response handling."""

import pytest

from proofread_ocr.hashline import HashlineError, extract_hashline_patch


def test_extract_plain_hashline_patch():
    raw = "[chunk_001.md#A1B2]\nreplace 2..2:\n+fixed"
    assert extract_hashline_patch(raw) == raw


def test_extract_fenced_hashline_patch():
    raw = "Here is the patch:\n```hashline\n[chunk_001.md#A1B2]\nreplace 1..1:\n+fixed\n```"
    assert extract_hashline_patch(raw) == "[chunk_001.md#A1B2]\nreplace 1..1:\n+fixed"


def test_extract_rejects_missing_header():
    with pytest.raises(HashlineError):
        extract_hashline_patch("replace 1..1:\n+fixed")
