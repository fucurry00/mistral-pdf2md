"""Normalize dict and SDK object response shapes into the internal page model."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from pdf_curator.errors import ValidationError
from pdf_curator.models import OcrPage


def _get(value: Any, name: str, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get(name, default)
    return getattr(value, name, default)


def _plain(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    if hasattr(value, "model_dump"):
        return _plain(value.model_dump())
    if hasattr(value, "__dict__"):
        return {
            key: _plain(item)
            for key, item in vars(value).items()
            if not key.startswith("_")
        }
    return str(value)


def response_to_dict(response: Any) -> dict[str, Any]:
    plain = _plain(response)
    if not isinstance(plain, dict):
        raise ValidationError("OCR response must be an object with a pages array")
    return plain


def normalize_ocr_response(response: Any) -> list[OcrPage]:
    raw_pages = _get(response, "pages")
    if not isinstance(raw_pages, Iterable) or isinstance(raw_pages, (str, bytes, dict)):
        raise ValidationError("OCR response is missing a pages array")

    pages: list[OcrPage] = []
    for position, raw_page in enumerate(raw_pages):
        raw_index = _get(raw_page, "index", position)
        if not isinstance(raw_index, int) or raw_index < 0:
            raise ValidationError(f"OCR page {position} has an invalid index")

        markdown = _get(raw_page, "markdown")
        if markdown is None:
            markdown = _get(raw_page, "text")
        header = _get(raw_page, "header")
        footer = _get(raw_page, "footer")
        images = list(_get(raw_page, "images", []) or [])
        tables = list(_get(raw_page, "tables", []) or [])
        dimensions = _plain(_get(raw_page, "dimensions"))
        confidence = _plain(
            _get(raw_page, "confidence_scores", _get(raw_page, "confidence"))
        )

        usable_metadata = bool(header or footer or images or tables)
        if markdown is None and not usable_metadata:
            raise ValidationError(
                f"OCR page {raw_index} has neither markdown/text nor usable page metadata"
            )
        if markdown is not None and not isinstance(markdown, str):
            raise ValidationError(f"OCR page {raw_index} markdown must be text")

        pages.append(
            OcrPage(
                index=raw_index + 1,
                markdown=markdown or "",
                dimensions=dimensions,
                confidence=confidence,
                images=[_plain(item) for item in images],
                tables=[_plain(item) for item in tables],
                header=header,
                footer=footer,
            )
        )

    if not pages:
        raise ValidationError("OCR response contains no pages")
    if len({page.index for page in pages}) != len(pages):
        raise ValidationError("OCR response contains duplicate page indices")
    return sorted(pages, key=lambda page: page.index)
