"""Hashline sidecar integration for patch-based proofreading."""

from __future__ import annotations

import asyncio
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


class HashlineError(RuntimeError):
    """Raised when Hashline preparation or patch application fails."""


@dataclass(frozen=True)
class HashlineTarget:
    path: str
    tag: str
    header: str
    numbered_text: str


_HASHLINE_HEADER_RE = re.compile(r"^\[[^\]\n]+#[0-9A-Fa-f]{4}\]\s*$", re.MULTILINE)
_FENCE_RE = re.compile(r"```(?:hashline|text|diff|patch)?\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)


def _sidecar_path() -> Path:
    return Path(__file__).resolve().parents[2] / "scripts" / "apply_hashline.ts"


async def _run_sidecar(payload: dict, timeout: int = 30) -> dict:
    bun = shutil.which("bun")
    if bun is None:
        raise HashlineError("Bun is required for --edit-mode hashline. Install Bun and run `bun install`.")

    script = _sidecar_path()
    if not script.exists():
        raise HashlineError(f"Hashline sidecar not found: {script}")

    proc = await asyncio.create_subprocess_exec(
        bun,
        str(script),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(json.dumps(payload).encode("utf-8")),
            timeout=timeout,
        )
    except asyncio.TimeoutError as exc:
        proc.kill()
        await proc.wait()
        raise HashlineError(f"Hashline sidecar timed out after {timeout}s") from exc

    stdout_text = stdout.decode("utf-8", errors="replace")
    stderr_text = stderr.decode("utf-8", errors="replace")
    if proc.returncode != 0:
        message = stderr_text.strip() or stdout_text.strip() or f"exit code {proc.returncode}"
        raise HashlineError(message)

    try:
        data = json.loads(stdout_text)
    except json.JSONDecodeError as exc:
        raise HashlineError(f"Invalid Hashline sidecar output: {stdout_text[:500]}") from exc
    if not isinstance(data, dict):
        raise HashlineError("Invalid Hashline sidecar output: expected object")
    return data


async def describe_target(path: str, text: str, timeout: int = 30) -> HashlineTarget:
    """Return the Hashline header/tag and numbered display text for a chunk."""
    data = await _run_sidecar(
        {"command": "describe", "path": path, "text": text},
        timeout=timeout,
    )
    try:
        return HashlineTarget(
            path=str(data["path"]),
            tag=str(data["tag"]),
            header=str(data["header"]),
            numbered_text=str(data["numberedText"]),
        )
    except KeyError as exc:
        raise HashlineError(f"Invalid Hashline describe response: missing {exc}") from exc


def extract_hashline_patch(raw_text: str) -> str:
    """Extract a Hashline patch from an LLM response.

    The prompt asks for patch-only output, but this tolerates a fenced block or
    short leading prose so failed formatting does not force a model rerun.
    """
    text = raw_text.strip()
    if not text:
        raise HashlineError("Empty Hashline patch response")

    for match in _FENCE_RE.finditer(text):
        candidate = match.group(1).strip()
        if _HASHLINE_HEADER_RE.search(candidate):
            return candidate

    header = _HASHLINE_HEADER_RE.search(text)
    if header is None:
        raise HashlineError("Hashline patch response did not contain a [path#TAG] header")
    return text[header.start():].strip().removesuffix("```").strip()


async def apply_hashline_patch(path: str, text: str, patch: str, timeout: int = 30) -> str:
    """Apply a Hashline patch to in-memory text and return the patched text."""
    data = await _run_sidecar(
        {"command": "apply", "path": path, "text": text, "patch": patch},
        timeout=timeout,
    )
    try:
        return str(data["text"])
    except KeyError as exc:
        raise HashlineError("Invalid Hashline apply response: missing text") from exc
