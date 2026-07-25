"""Traceable JSON debug bundle writer."""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from enum import Enum
from pathlib import Path
from typing import Any


def _jsonable(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return _jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "model_dump"):
        return _jsonable(value.model_dump())
    return str(value)


def write_debug_bundle(
    output_dir: Path,
    *,
    raw_ocr: Any,
    pages: Any,
    blocks: Any,
    proposals: Any,
    decisions: Any,
    applied_diffs: Any,
    warnings: Any,
) -> Path:
    debug_dir = output_dir / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "ocr_raw.json": raw_ocr,
        "pages.json": pages,
        "blocks.json": blocks,
        "edit_candidates.json": proposals,
        "gate_decisions.json": decisions,
        "applied_diffs.json": applied_diffs,
        "warnings.json": warnings,
    }
    for name, value in files.items():
        (debug_dir / name).write_text(
            json.dumps(_jsonable(value), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return debug_dir
