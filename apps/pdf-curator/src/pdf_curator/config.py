"""Runtime configuration for live OCR."""

from __future__ import annotations

import os

from pdf_curator.errors import ConfigurationError


def load_mistral_api_key() -> str:
    """Read an already-injected process variable; never load dotenv files."""

    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ConfigurationError(
            "MISTRAL_API_KEY is required for live OCR; use --from-ocr-json for offline input"
        )
    return api_key
