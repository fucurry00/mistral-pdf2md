"""Phase 1: Extract document context using a completion API."""

from __future__ import annotations

import sys
from pathlib import Path

from .llm import run_llm


async def extract_context(
    input_path: Path,
    workdir: Path,
    prompt_path: Path,
    model: str = "gemini-3.1-flash-lite-preview",
    skip_review: bool = False,
    verbose: bool = False,
) -> tuple[Path, float]:
    """Extract notation table, structure outline, and terminology whitelist.

    Args:
        input_path: Path to the input markdown file.
        workdir: Working directory for intermediate files.
        prompt_path: Path to the extract_context.md prompt.
        model: Gemini model name.
        skip_review: If True, skip human review of context.md.
        verbose: Print detailed progress.

    Returns:
        Tuple of (path to context.md, duration in seconds).
    """
    workdir.mkdir(parents=True, exist_ok=True)
    context_raw_path = workdir / "context_raw.json"
    context_path = workdir / "context.md"

    print("Phase 1: Extracting document context...")

    # Call the completion API with the full document
    response = await run_llm(
        file_paths=[prompt_path, input_path],
        prompt="Extract document context per the instructions in the input.",
        model=model,
    )

    if response.returncode != 0:
        print(f"Error in context extraction: {response.stderr}", file=sys.stderr)
        sys.exit(1)

    # Save raw response
    context_raw_path.write_text(response.raw_stdout, encoding="utf-8")

    # Save parsed context
    context_text = response.text
    if not context_text.strip():
        print("Warning: Empty context extracted. Check the input file.", file=sys.stderr)
        context_text = "## Notation Table\n\n(empty)\n\n## Structure Outline\n\n(empty)\n\n## Terminology Whitelist\n\n(empty)\n"

    context_path.write_text(context_text, encoding="utf-8")

    if verbose:
        print(f"  Raw response saved to: {context_raw_path}")
        print(f"  Context saved to: {context_path}")
        if response.tokens_in:
            print(f"  Tokens: {response.tokens_in} in / {response.tokens_out} out")

    print(f"  Context extracted in {response.duration_sec:.1f}s")

    # Human review checkpoint
    if not skip_review:
        print(f"\n--- Context Review ---")
        print(f"Please review and edit if needed: {context_path}")
        print(f"{'='*60}")
        # Print a preview (first 40 lines)
        lines = context_text.splitlines()
        for line in lines[:40]:
            print(f"  {line}")
        if len(lines) > 40:
            print(f"  ... ({len(lines) - 40} more lines)")
        print(f"{'='*60}")
        try:
            input("Press Enter to continue, or Ctrl-C to abort... ")
        except KeyboardInterrupt:
            print("\nAborted by user.")
            sys.exit(0)

    return context_path, response.duration_sec
