"""JSON-shaped YAML frontmatter for dependency-free deterministic output."""

from __future__ import annotations

import json
from typing import Any


def render_frontmatter(metadata: dict[str, Any]) -> str:
    return f"---\n{json.dumps(metadata, ensure_ascii=False, indent=2)}\n---"
