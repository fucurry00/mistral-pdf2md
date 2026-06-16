"""Minimal stdin -> completion -> stdout CLI, reusing `run_llm`.

Lets the parent pipeline (pipeline.py cleanup planner) make a one-shot LLM call
without depending on any LLM SDK itself or on agy: it shells out via
`uv run --project proofread-ocr proofread-llm`, the same pattern used for the
main proofreading step. The user message is read from stdin; the system prompt
and model are passed as flags.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
import tempfile
from pathlib import Path

from .llm import run_llm


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="proofread-llm",
        description="Read stdin as the user message, print the completion to stdout.",
    )
    parser.add_argument("--system", default=None, help="System prompt")
    parser.add_argument(
        "-m", "--model", default="gemini-3.1-flash-lite-preview",
        help="Model name (provider inferred from it)",
    )
    parser.add_argument("--timeout", type=int, default=180, help="Per-request timeout (s)")
    parser.add_argument("--max-tokens", type=int, default=8000, help="Max output tokens")
    args = parser.parse_args()

    user_text = sys.stdin.read()
    if not user_text.strip():
        print("Error: no input received on stdin", file=sys.stderr)
        sys.exit(1)

    # run_llm reads from files; stage stdin to a temp file to reuse it as-is.
    with tempfile.NamedTemporaryFile(
        "w", suffix=".md", encoding="utf-8", delete=False
    ) as tmp:
        tmp.write(user_text)
        tmp_path = Path(tmp.name)

    try:
        response = asyncio.run(
            run_llm(
                file_paths=[tmp_path],
                prompt=args.system,
                model=args.model,
                timeout=args.timeout,
                max_tokens=args.max_tokens,
            )
        )
    finally:
        tmp_path.unlink(missing_ok=True)

    if response.returncode != 0:
        print(response.stderr, file=sys.stderr)
        sys.exit(1)

    sys.stdout.write(response.text)


if __name__ == "__main__":
    main()
