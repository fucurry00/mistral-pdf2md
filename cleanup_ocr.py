"""
OCR cleanup for Mistral-extracted math textbook markdown.

Fixes (always applied):
  1. HTML entities  (&amp; &lt; &gt; etc.)
  2. Standalone page numbers  (configurable digit range, default 3-4)
  3. Page-break separators   (--- inserted between pages by OCR script)
  4. Excessive blank lines

Optional (via --header-pattern or --preset):
  5. Running headers/footers (book-specific regex patterns)

Usage:
  python cleanup_ocr.py <file.md> [file2.md ...]
  python cleanup_ocr.py <file.md> --preset dummit-foote
  python cleanup_ocr.py <file.md> --header-pattern "^Chapter \\d+" --header-pattern "^Section \\d+"
  python cleanup_ocr.py <file.md> --no-remove-separators
  python cleanup_ocr.py <file.md> --page-number-range 2,5
"""

import argparse
import re
import sys
from pathlib import Path

# Built-in presets: book name → list of regex patterns for running headers
PRESETS: dict[str, list[str]] = {
    "dummit-foote": [
        r"^Sec\. \d+\.\d+[^\n]*$",   # "Sec. 10.1 Basic Definitions and Examples"
        r"^Chap\. \d+[^\n]*$",         # "Chap. 10 Introduction to Module Theory"
    ],
}


def clean(
    text: str,
    header_patterns: list[str],
    remove_separators: bool,
    page_min: int,
    page_max: int,
) -> str:
    # 1. HTML entities
    entities = {
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&nbsp;": " ",
        "&#39;": "'",
        "&quot;": '"',
    }
    for ent, ch in entities.items():
        text = text.replace(ent, ch)

    # 2. Standalone page numbers
    text = re.sub(rf"^\d{{{page_min},{page_max}}}\s*$", "", text, flags=re.MULTILINE)

    # 3. Running headers / footers (book-specific)
    for pattern in header_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    # 4. Page-break --- separators
    if remove_separators:
        text = re.sub(r"^---\s*$", "", text, flags=re.MULTILINE)

    # 5. Collapse 3+ consecutive blank lines → 1 blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Clean up OCR-extracted markdown from math textbooks."
    )
    parser.add_argument("files", nargs="+", help="Markdown files to clean")
    parser.add_argument(
        "--preset",
        choices=list(PRESETS.keys()),
        help="Use a built-in header pattern preset for a specific book",
    )
    parser.add_argument(
        "--header-pattern",
        dest="header_patterns",
        action="append",
        default=[],
        metavar="REGEX",
        help="Regex pattern for running headers to remove (can be specified multiple times)",
    )
    parser.add_argument(
        "--no-remove-separators",
        dest="remove_separators",
        action="store_false",
        default=True,
        help="Keep --- page-break separators instead of removing them",
    )
    parser.add_argument(
        "--page-number-range",
        default="3,4",
        metavar="MIN,MAX",
        help="Digit range for standalone page numbers to remove (default: 3,4)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Write output to this file instead of overwriting input (only valid with a single input file)",
    )

    args = parser.parse_args()

    # Resolve header patterns
    patterns = list(args.header_patterns)
    if args.preset:
        patterns = PRESETS[args.preset] + patterns

    # Parse page number range
    try:
        page_min, page_max = map(int, args.page_number_range.split(","))
    except ValueError:
        print("Error: --page-number-range must be MIN,MAX (e.g. 3,4)", file=sys.stderr)
        sys.exit(1)

    if args.output and len(args.files) > 1:
        print("Error: --output can only be used with a single input file", file=sys.stderr)
        sys.exit(1)

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"File not found: {path}", file=sys.stderr)
            continue

        original = path.read_text(encoding="utf-8")
        cleaned = clean(
            original,
            header_patterns=patterns,
            remove_separators=args.remove_separators,
            page_min=page_min,
            page_max=page_max,
        )

        if args.output:
            out_path = Path(args.output)
        else:
            # Backup and overwrite in place
            backup = path.with_suffix(".md.bak")
            backup.write_text(original, encoding="utf-8")
            out_path = path

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(cleaned, encoding="utf-8")

        orig_lines = original.count("\n")
        new_lines = cleaned.count("\n")
        suffix = f"  → {out_path}" if args.output else f"  (backup: {path.with_suffix('.md.bak').name})"
        print(f"{path.name}: {orig_lines} → {new_lines} lines{suffix}")


if __name__ == "__main__":
    main()
