"""Live Mistral OCR adapter kept behind a narrow app-local boundary."""

from __future__ import annotations

import base64
import io
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from pdf_curator.errors import ValidationError


def _pdf_bytes(pdf_path: Path, selected_pages: list[int] | None) -> bytes:
    if not selected_pages:
        return pdf_path.read_bytes()

    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page_number in selected_pages:
        if page_number > len(reader.pages):
            raise ValidationError(
                f"page {page_number} is out of range for {len(reader.pages)}-page PDF"
            )
        writer.add_page(reader.pages[page_number - 1])
    buffer = io.BytesIO()
    writer.write(buffer)
    return buffer.getvalue()


def run_mistral_ocr(
    pdf_path: Path,
    *,
    api_key: str,
    selected_pages: list[int] | None = None,
) -> object:
    """Submit a PDF as a base64 document URL and return the SDK response."""

    from mistralai.client import Mistral

    encoded = base64.b64encode(_pdf_bytes(pdf_path, selected_pages)).decode("ascii")
    client = Mistral(api_key=api_key)
    return client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": f"data:application/pdf;base64,{encoded}",
        },
        table_format="markdown",
        extract_header=True,
        extract_footer=True,
        confidence_scores_granularity="word",
        include_image_base64=False,
    )
