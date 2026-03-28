"""Async wrapper for the Gemini CLI."""

from __future__ import annotations

import asyncio
import json
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class GeminiResponse:
    text: str
    raw_stdout: str
    stderr: str
    returncode: int
    duration_sec: float
    tokens_in: int | None = None
    tokens_out: int | None = None


_MAX_RETRIES = 3
_INITIAL_BACKOFF = 2.0


def _parse_json_response(raw: str) -> tuple[str, int | None, int | None]:
    """Extract text content and token stats from Gemini JSON output.

    Gemini CLI with --output-format json returns a JSON object.
    We extract the response text and optional token usage.
    """
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # If JSON parsing fails, treat the entire stdout as plain text
        return raw, None, None

    # Gemini CLI JSON structure may vary; handle common shapes
    if isinstance(data, dict):
        # Try common keys
        text = data.get("response", data.get("text", data.get("content", "")))
        if isinstance(text, list):
            text = "\n".join(str(part) for part in text)
        usage = data.get("usageMetadata", data.get("usage", {}))
        tokens_in = usage.get("promptTokenCount", usage.get("input_tokens"))
        tokens_out = usage.get("candidatesTokenCount", usage.get("output_tokens"))
        return str(text), tokens_in, tokens_out

    return raw, None, None


def _read_and_concat_files(file_paths: list[Path]) -> str:
    """Read files and concatenate their contents with separators."""
    parts = []
    for filepath in file_paths:
        if filepath.exists():
            parts.append(filepath.read_text(encoding="utf-8"))
        else:
            raise FileNotFoundError(f"Input file not found: {filepath}")
    return "\n\n".join(parts)


async def run_gemini(
    file_paths: list[Path],
    prompt: str | None = None,
    model: str = "gemini-3-flash-preview",
    output_format: str = "json",
    timeout: int = 300,
) -> GeminiResponse:
    """Run the Gemini CLI asynchronously with retry logic.

    Uses stdin pipe pattern: cat files | gemini -p "prompt"
    This is the recommended approach for non-interactive mode.

    Args:
        file_paths: List of file paths to read and pipe as stdin.
        prompt: Optional short prompt string passed via -p. If None,
                the first file in file_paths is treated as the prompt.
        model: Gemini model name.
        output_format: Output format (json recommended).
        timeout: Timeout in seconds per attempt.
    """
    # Read all file contents and concatenate
    stdin_text = _read_and_concat_files(file_paths)

    # Build command
    cmd = ["gemini"]
    if prompt:
        cmd.extend(["-p", prompt])
    else:
        cmd.extend(["-p", "Process the following input:"])
    cmd.extend(["--output-format", output_format, "-m", model])

    last_error = ""
    for attempt in range(_MAX_RETRIES):
        start = time.monotonic()
        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            try:
                stdout_bytes, stderr_bytes = await asyncio.wait_for(
                    proc.communicate(input=stdin_text.encode("utf-8")),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                proc.kill()
                await proc.wait()
                duration = time.monotonic() - start
                last_error = f"Timeout after {timeout}s"
                if attempt < _MAX_RETRIES - 1:
                    continue
                return GeminiResponse(
                    text="",
                    raw_stdout="",
                    stderr=last_error,
                    returncode=-1,
                    duration_sec=duration,
                )

            duration = time.monotonic() - start
            stdout_str = stdout_bytes.decode("utf-8", errors="replace")
            stderr_str = stderr_bytes.decode("utf-8", errors="replace")

            # Check for rate limiting (429)
            if proc.returncode != 0 and "429" in stderr_str:
                backoff = _INITIAL_BACKOFF * (2 ** attempt)
                last_error = f"Rate limited (429), backing off {backoff}s"
                if attempt < _MAX_RETRIES - 1:
                    await asyncio.sleep(backoff)
                    continue

            text, tokens_in, tokens_out = _parse_json_response(stdout_str)

            return GeminiResponse(
                text=text,
                raw_stdout=stdout_str,
                stderr=stderr_str,
                returncode=proc.returncode,
                duration_sec=duration,
                tokens_in=tokens_in,
                tokens_out=tokens_out,
            )

        except FileNotFoundError:
            return GeminiResponse(
                text="",
                raw_stdout="",
                stderr="'gemini' CLI command not found. Install: https://github.com/google-gemini/gemini-cli",
                returncode=-1,
                duration_sec=0.0,
            )

    # All retries exhausted
    return GeminiResponse(
        text="",
        raw_stdout="",
        stderr=f"All {_MAX_RETRIES} retries exhausted. Last error: {last_error}",
        returncode=-1,
        duration_sec=0.0,
    )


def launch_tmux_session(
    chunks: list[Path],
    context_path: Path,
    prompt_path: Path,
    results_dir: Path,
    model: str,
) -> None:
    """Launch a tmux session with one pane per chunk for visual debugging.

    Uses cat | gemini pipe pattern for each pane.
    """
    if not shutil.which("tmux"):
        print("Error: tmux is not installed.", file=sys.stderr)
        sys.exit(1)

    session_name = "proofread"

    # Kill existing session if any
    subprocess.run(["tmux", "kill-session", "-t", session_name], capture_output=True)

    # Create new session
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name], check=True)

    for i, chunk_path in enumerate(chunks):
        chunk_id = chunk_path.stem.replace("chunk_", "")
        result_path = results_dir / f"chunk_{chunk_id}.json"
        done_marker = results_dir / f".done_{chunk_id}"

        cmd = (
            f"cat {prompt_path} {context_path} {chunk_path} "
            f"| gemini -p 'Proofread the following OCR text per the instructions.' "
            f"--output-format json -m {model} "
            f"| tee {result_path}; "
            f"touch {done_marker}"
        )

        if i > 0:
            subprocess.run(["tmux", "split-window", "-t", session_name, cmd], check=True)
        else:
            subprocess.run(["tmux", "send-keys", "-t", session_name, cmd, "Enter"], check=True)

    # Tile the panes
    subprocess.run(["tmux", "select-layout", "-t", session_name, "tiled"], check=True)

    # Attach
    print(f"Attaching to tmux session '{session_name}'...")
    print("Detach with Ctrl-b d. Completion markers: .done_NNN files.")
    subprocess.run(["tmux", "attach", "-t", session_name])
