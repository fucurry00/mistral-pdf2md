import argparse
import os
import re
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent
_DEFAULT_HEADER_PATTERN = r"Bara Kim 2026, Spring, Korea University\s+Real Analysis\s*"
_MATH_BLOCK_RE = re.compile(
    r"(?:Definition|Theorem|Proposition|Lemma|Corollary)\b[^\n]*(?:\n(?!\n).+)*",
    re.IGNORECASE,
)
_SEMANTIC_UNIT_RE = re.compile(
    r"(?:^|\n)((?:Definition|Theorem|Proposition|Lemma|Corollary)\b.*?)(?=\n(?:Definition|Theorem|Proposition|Lemma|Corollary|Proof)\b|\Z)",
    re.IGNORECASE | re.DOTALL,
)
_PROOF_RE = re.compile(r"(?:^|\n)(Proof\b.*?)(?=\n(?:Definition|Theorem|Proposition|Lemma|Corollary|Proof)\b|\Z)", re.IGNORECASE | re.DOTALL)
_TAIL_CONTEXT_CHARS = 400
_UNCERTAIN_RE = re.compile(r"<!--\s*OCR-UNCERTAIN[^>]*-->")
_LATEX_INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)")
_LATEX_BLOCK_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_LATEX_ENV_RE = re.compile(r"\\begin\{(\w+)\}|\\end\{(\w+)\}")


# ---------------------------------------------------------------------------
# Preprocessing
# ---------------------------------------------------------------------------

def preprocess(text: str, min_frequency_ratio: float = 0.4) -> tuple[str, list[str]]:
    """
    Detect and remove recurring noise lines (slide headers, footers, navigation).
    Returns (cleaned_text, removed_patterns).
    min_frequency_ratio: a line appearing in >= this fraction of estimated pages is noise.
    """
    lines = text.splitlines()
    # Estimate page count from separator lines
    sep_count = sum(1 for l in lines if re.match(r"^---\s*$", l))
    estimated_pages = max(sep_count, 1)
    threshold = max(2, int(estimated_pages * min_frequency_ratio))

    line_counts = Counter(l.strip() for l in lines if l.strip())
    noise_lines = {line for line, count in line_counts.items() if count >= threshold}

    if not noise_lines:
        return text, []

    cleaned = "\n".join(l for l in lines if l.strip() not in noise_lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned, sorted(noise_lines)


# ---------------------------------------------------------------------------
# Tail context extraction
# ---------------------------------------------------------------------------

def _extract_tail_context(chunk_text: str) -> str:
    """Return the last Definition/Theorem/etc. block from a chunk (up to _TAIL_CONTEXT_CHARS chars)."""
    matches = list(_MATH_BLOCK_RE.finditer(chunk_text))
    if matches:
        return matches[-1].group(0)[:_TAIL_CONTEXT_CHARS].strip()
    return chunk_text[-_TAIL_CONTEXT_CHARS:].strip()


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def split_into_chunks(text, pages_per_chunk=5, header_pattern=None, chunk_mode="pages"):
    """
    Splits the OCR'd markdown text into logical chunks.
    Returns list[dict] with keys:
      - text: chunk content
      - context_from_previous: last Definition/Theorem of the preceding chunk (empty for first)

    chunk_mode:
      "pages"    – split by header pattern then group by pages_per_chunk (default)
      "semantic" – group Definition/Theorem/Proof as atomic units by token budget
    """
    if chunk_mode == "semantic":
        raw_chunks = _semantic_chunks(text, token_budget=3000)
    else:
        if header_pattern is None:
            header_pattern = _DEFAULT_HEADER_PATTERN
        pages = re.split(header_pattern, text)
        pages = [p.strip() for p in pages if p.strip()]

        raw_chunks = []
        current_chunk: list[str] = []
        current_count = 0
        for page in pages:
            current_chunk.append(page)
            current_count += 1
            if current_count >= pages_per_chunk:
                raw_chunks.append("\n\n---\n\n".join(current_chunk))
                current_chunk = []
                current_count = 0
        if current_chunk:
            raw_chunks.append("\n\n---\n\n".join(current_chunk))

    chunks = []
    for i, chunk_text in enumerate(raw_chunks):
        context = _extract_tail_context(raw_chunks[i - 1]) if i > 0 else ""
        chunks.append({"text": chunk_text, "context_from_previous": context})
    return chunks


def _semantic_chunks(text: str, token_budget: int = 3000) -> list[str]:
    """
    Group Definition/Theorem/Proof units into chunks under token_budget.
    A Proof immediately following a Theorem is kept in the same unit.
    Approximates tokens as chars / 4.
    """
    # Split into semantic units: math blocks + their proofs
    units: list[str] = []
    remaining = text
    while remaining:
        m = _SEMANTIC_UNIT_RE.search(remaining)
        pm = _PROOF_RE.search(remaining)
        candidates = [(m, "math"), (pm, "proof")] if pm else [(m, "math")]
        earliest = min((c for c in candidates if c[0]), key=lambda c: c[0].start(), default=None)
        if not earliest:
            if remaining.strip():
                units.append(remaining.strip())
            break
        match, kind = earliest
        before = remaining[:match.start()].strip()
        if before:
            units.append(before)
        units.append(match.group(0).strip())
        remaining = remaining[match.end():]

    # Merge units into chunks under token budget
    raw_chunks: list[str] = []
    current_parts: list[str] = []
    current_tokens = 0
    for unit in units:
        unit_tokens = len(unit) // 4
        if current_tokens + unit_tokens > token_budget and current_parts:
            raw_chunks.append("\n\n".join(current_parts))
            current_parts = [unit]
            current_tokens = unit_tokens
        else:
            current_parts.append(unit)
            current_tokens += unit_tokens
    if current_parts:
        raw_chunks.append("\n\n".join(current_parts))
    return raw_chunks


# ---------------------------------------------------------------------------
# LaTeX validation
# ---------------------------------------------------------------------------

def validate_latex(text: str) -> list[str]:
    """
    Check for unmatched $ delimiters and \\begin/\\end pairs.
    Returns list of warning strings.
    """
    warnings: list[str] = []

    # Check inline $ balance (rough: count unescaped $, excluding $$)
    stripped = _LATEX_BLOCK_RE.sub("", text)
    dollar_count = len(re.findall(r"(?<!\$)\$(?!\$)", stripped))
    if dollar_count % 2 != 0:
        warnings.append(f"Unmatched inline $ delimiter (found {dollar_count} single $)")

    # Check \\begin/\\end pairs
    env_stack: list[str] = []
    for m in _LATEX_ENV_RE.finditer(text):
        if m.group(1):  # \begin
            env_stack.append(m.group(1))
        else:  # \end
            env_name = m.group(2)
            if env_stack and env_stack[-1] == env_name:
                env_stack.pop()
            else:
                warnings.append(f"Unmatched \\end{{{env_name}}}")
    for env in env_stack:
        warnings.append(f"Unclosed \\begin{{{env}}}")

    return warnings


# ---------------------------------------------------------------------------
# OCR-UNCERTAIN report
# ---------------------------------------------------------------------------

def extract_uncertain_report(text: str) -> list[str]:
    """Return all <!-- OCR-UNCERTAIN ... --> comments found in text."""
    return _UNCERTAIN_RE.findall(text)


# ---------------------------------------------------------------------------
# Gemini runner
# ---------------------------------------------------------------------------

def run_gemini(input_text, prompt_path):
    """Runs the gemini CLI command with the specified prompt and input text."""
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()
        cmd = ["gemini", "--model", "gemini-3-flash-preview", "-p", prompt]
        result = subprocess.run(
            cmd,
            input=input_text,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"\nError processing via gemini CLI: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("\nError: 'gemini' CLI command not found.", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Clean up OCR'd Markdown using Gemini CLI (2-Pass Approach)")
    parser.add_argument("input_file", help="Path to the input Markdown file")
    parser.add_argument("-o", "--output", help="Path to the output Markdown file", required=True)
    parser.add_argument("-p1", "--prompt1", default=str(_SCRIPT_DIR / "prompt_pass1.md"), help="Path to the Pass 1 prompt file")
    parser.add_argument("-p2", "--prompt2", default=str(_SCRIPT_DIR / "prompt_pass2.md"), help="Path to the Pass 2 prompt file")
    parser.add_argument("-c", "--chunk-size", type=int, default=5, help="Number of pages per chunk (default: 5, pages mode only)")
    parser.add_argument("--header-pattern", default=None, help="ページ分割に使う正規表現（省略時: Folland書籍のデフォルトパターン）")
    parser.add_argument("--chunk-mode", choices=["pages", "semantic"], default="pages", help="チャンク分割モード: pages（デフォルト）または semantic")
    parser.add_argument("-w", "--max-workers", type=int, default=5, help="Pass 2 の並列数（default: 5）")
    parser.add_argument("--auto-preprocess", action="store_true", help="繰り返しノイズ行を自動検出・除去してからOCRクリーンアップを実行")
    parser.add_argument("--report", help="OCR-UNCERTAIN箇所とLaTeX警告をこのファイルに出力")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Input file not found: {args.input_file}")
        sys.exit(1)
    if not os.path.exists(args.prompt1):
        print(f"Pass 1 Prompt file not found: {args.prompt1}")
        sys.exit(1)
    if not os.path.exists(args.prompt2):
        print(f"Pass 2 Prompt file not found: {args.prompt2}")
        sys.exit(1)

    print(f"Reading input file: {args.input_file}...")
    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Preprocessing
    if args.auto_preprocess:
        print("\n--- Preprocessing: detecting recurring noise lines ---")
        text, removed = preprocess(text)
        if removed:
            print(f"Removed {len(removed)} noise pattern(s):")
            for p in removed:
                print(f"  {p!r}")
        else:
            print("No recurring noise detected.")

    # Pass 1: Extract Global Context
    print("\n--- Pass 1: Analyzing entire document for global context ---")
    global_context = run_gemini(text, args.prompt1)
    print("Global context extracted successfully.\n")

    # Pass 2: Process Chunks
    print(f"--- Pass 2: Splitting and processing chunks (mode: {args.chunk_mode}) ---")
    chunks = split_into_chunks(
        text,
        pages_per_chunk=args.chunk_size,
        header_pattern=args.header_pattern,
        chunk_mode=args.chunk_mode,
    )
    print(f"Total chunks created: {len(chunks)}\n")

    def process_chunk(idx, chunk_dict):
        context_section = ""
        if chunk_dict["context_from_previous"]:
            context_section = f"\n\n<context_from_previous>\n{chunk_dict['context_from_previous']}\n</context_from_previous>"
        combined_input = (
            f"<global_context>\n{global_context}\n</global_context>"
            f"{context_section}"
            f"\n\n<target_chunk>\n{chunk_dict['text']}\n</target_chunk>"
        )
        result = run_gemini(combined_input, args.prompt2)
        print(f"  -> Chunk {idx}/{len(chunks)} completed.")
        return idx, result

    results = {}
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {executor.submit(process_chunk, i, chunk_dict): i for i, chunk_dict in enumerate(chunks, 1)}
        for future in as_completed(futures):
            idx, cleaned_text = future.result()
            results[idx] = cleaned_text

    processed_chunks = [results[i] for i in range(1, len(chunks) + 1)]
    output_text = "\n\n".join(processed_chunks)

    print(f"Combining chunks and writing to {args.output}...")
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output_text)
    print(f"Done! Cleaned file saved to: {args.output}")

    # Post-processing report
    latex_warnings = validate_latex(output_text)
    uncertain_items = extract_uncertain_report(output_text)

    if latex_warnings or uncertain_items:
        print(f"\n--- Post-processing report ---")
        for w in latex_warnings:
            print(f"  [LaTeX] {w}")
        print(f"  [OCR-UNCERTAIN] {len(uncertain_items)} item(s) flagged for review")

    if args.report:
        report_lines = ["# Post-processing Report\n"]
        report_lines.append(f"## LaTeX Warnings ({len(latex_warnings)})\n")
        report_lines.extend(f"- {w}\n" for w in latex_warnings)
        report_lines.append(f"\n## OCR-UNCERTAIN Items ({len(uncertain_items)})\n")
        report_lines.extend(f"- {item}\n" for item in uncertain_items)
        Path(args.report).write_text("".join(report_lines), encoding="utf-8")
        print(f"Report written to: {args.report}")


if __name__ == "__main__":
    main()
