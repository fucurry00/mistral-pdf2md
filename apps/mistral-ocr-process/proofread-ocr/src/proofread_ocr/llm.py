"""Completion-API wrapper for the proofreading pipeline.

Routes by model name to the official provider SDK:
  - "claude"/"haiku"/"sonnet"/"opus"  -> Anthropic   (ANTHROPIC_API_KEY)
  - "gemini"                           -> Google GenAI (GEMINI_API_KEY)

Replaces the former agy/Gemini-CLI subprocess backend. The public surface
(`run_llm` returning an `LLMResponse`) is a drop-in for the old `run_gemini`,
minus the dead `output_format` argument.
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from pathlib import Path

_ENV_LOADED = False


def _ensure_env_loaded() -> None:
    """Load API keys from a `.env` file once, without overriding real env vars.

    proofread-ocr runs as a nested uv project (often via `uv run --project`),
    so the process does not auto-inherit the parent project's `.env`. Search the
    likely locations and let an already-exported variable win.
    """
    global _ENV_LOADED
    if _ENV_LOADED:
        return
    from dotenv import find_dotenv, load_dotenv

    here = Path(__file__).resolve()
    candidates = [
        here.parents[3] / ".env",  # apps/mistral-ocr-process/.env (parent project)
        here.parents[2] / ".env",  # proofread-ocr/.env (standalone)
    ]
    for env_path in candidates:
        if env_path.is_file():
            load_dotenv(env_path, override=False)
    found = find_dotenv(usecwd=True)
    if found:
        load_dotenv(found, override=False)
    _ENV_LOADED = True


@dataclass
class LLMResponse:
    text: str
    raw_stdout: str
    stderr: str
    returncode: int
    duration_sec: float
    tokens_in: int | None = None
    tokens_out: int | None = None


def _provider_for(model: str) -> str:
    name = model.lower()
    if name.startswith("gemini") or "gemini" in name:
        return "gemini"
    if any(tok in name for tok in ("claude", "haiku", "sonnet", "opus", "fable")):
        return "anthropic"
    # Default to Anthropic for unrecognised names.
    return "anthropic"


def _read_and_concat_files(file_paths: list[Path]) -> str:
    """Read files and concatenate their contents with blank-line separators."""
    parts = []
    for filepath in file_paths:
        if not filepath.exists():
            raise FileNotFoundError(f"Input file not found: {filepath}")
        parts.append(filepath.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


async def _run_anthropic(
    system: str, user: str, model: str, timeout: int, max_tokens: int
) -> LLMResponse:
    start = time.monotonic()
    try:
        from anthropic import AsyncAnthropic
    except ImportError as exc:
        return LLMResponse(
            text="", raw_stdout="", returncode=-1, duration_sec=0.0,
            stderr=f"anthropic SDK not installed: {exc}. Run `uv add anthropic`.",
        )

    client = AsyncAnthropic()
    try:
        msg = await client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            timeout=float(timeout),
        )
    except Exception as exc:  # noqa: BLE001 - surface any SDK/HTTP error as failure
        return LLMResponse(
            text="", raw_stdout="", returncode=-1,
            duration_sec=time.monotonic() - start,
            stderr=f"{type(exc).__name__}: {exc}",
        )

    text = "".join(
        block.text for block in msg.content if getattr(block, "type", None) == "text"
    )
    return LLMResponse(
        text=text,
        raw_stdout=text,
        stderr="",
        returncode=0,
        duration_sec=time.monotonic() - start,
        tokens_in=msg.usage.input_tokens,
        tokens_out=msg.usage.output_tokens,
    )


async def _run_gemini(
    system: str, user: str, model: str, timeout: int, max_tokens: int
) -> LLMResponse:
    start = time.monotonic()
    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        return LLMResponse(
            text="", raw_stdout="", returncode=-1, duration_sec=0.0,
            stderr=f"google-genai SDK not installed: {exc}. Run `uv add google-genai`.",
        )

    client = genai.Client()
    try:
        resp = await client.aio.models.generate_content(
            model=model,
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=system or None,
                max_output_tokens=max_tokens,
                http_options=types.HttpOptions(timeout=timeout * 1000),  # ms
            ),
        )
    except Exception as exc:  # noqa: BLE001
        return LLMResponse(
            text="", raw_stdout="", returncode=-1,
            duration_sec=time.monotonic() - start,
            stderr=f"{type(exc).__name__}: {exc}",
        )

    text = resp.text or ""
    usage = getattr(resp, "usage_metadata", None)
    return LLMResponse(
        text=text,
        raw_stdout=text,
        stderr="",
        returncode=0,
        duration_sec=time.monotonic() - start,
        tokens_in=getattr(usage, "prompt_token_count", None) if usage else None,
        tokens_out=getattr(usage, "candidates_token_count", None) if usage else None,
    )


async def run_llm(
    file_paths: list[Path],
    prompt: str | None = None,
    model: str = "gemini-3.1-flash-lite-preview",
    timeout: int = 300,
    max_tokens: int = 32000,
) -> LLMResponse:
    """Call a completion API with concatenated file contents as the user message.

    Args:
        file_paths: Files whose concatenated content becomes the user message
            (typically [prompt_file, context_file, target_file]).
        prompt: Short instruction used as the system prompt. The detailed task
            instructions live inside the first file for backward compatibility.
        model: Model name; provider is inferred from it.
        timeout: Per-request timeout in seconds.
        max_tokens: Maximum output tokens.

    Returns:
        LLMResponse with returncode 0 on success, -1 on any failure.
    """
    try:
        user = _read_and_concat_files(file_paths)
    except FileNotFoundError as exc:
        return LLMResponse(
            text="", raw_stdout="", stderr=str(exc), returncode=-1, duration_sec=0.0,
        )

    _ensure_env_loaded()
    system = prompt or "You are a careful assistant. Follow the instructions in the input."
    provider = _provider_for(model)
    runner = _run_anthropic if provider == "anthropic" else _run_gemini

    try:
        return await asyncio.wait_for(
            runner(system, user, model, timeout, max_tokens),
            timeout=timeout + 30,
        )
    except asyncio.TimeoutError:
        return LLMResponse(
            text="", raw_stdout="", returncode=-1, duration_sec=float(timeout),
            stderr=f"Timeout after {timeout}s ({provider}/{model})",
        )
