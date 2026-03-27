"""
cleanup_ocr.py — General-purpose OCR Markdown cleanup.

Fixes (applied by default):
  1. html_entities      : HTML entities (&amp; &lt; &gt; etc.)
  2. page_numbers       : Standalone page numbers (Arabic + Roman numerals)
  3. running_headers    : Running headers/footers (book-specific regex patterns)
  4. separators         : Page-break --- separators
  5. page_break_headers : Repeated chapter titles after --- (bare text, not headings)
  6. empty_headings     : Empty ## headings with no content
  7. image_refs         : Image references (comment / delete / placeholder)
  8. standalone_dots    : Isolated dots left from blank pages
  9. excessive_blanks   : 4+ consecutive blank lines → 2

Usage:
  python cleanup_ocr.py <file.md> [file2.md ...]
  python cleanup_ocr.py <directory/>
  python cleanup_ocr.py <file.md> --preset dummit-foote
  python cleanup_ocr.py <file.md> --header-pattern "^Chapter \\d+" --header-pattern "^Section \\d+"
  python cleanup_ocr.py <file.md> --no-remove-separators
  python cleanup_ocr.py <file.md> --page-number-range 2,5
  python cleanup_ocr.py <file.md> -o cleaned.md
  python cleanup_ocr.py <directory/> --dry-run --verbose
  python cleanup_ocr.py <file.md> --only=html_entities,page_numbers
  python cleanup_ocr.py <directory/> --verify
"""

import argparse
import difflib
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

ALL_FIXES = [
    "html_entities",
    "page_numbers",
    "running_headers",
    "separators",
    "page_break_headers",
    "empty_headings",
    "image_refs",
    "standalone_dots",
    "excessive_blanks",
]


# ============================================================
# Fix functions
# ============================================================

def fix_html_entities(text: str) -> str:
    """Replace common HTML entities with plain characters."""
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
    return text


def fix_standalone_page_numbers(text: str, page_min: int = 3, page_max: int = 4) -> str:
    """Remove standalone Arabic and Roman numeral page numbers."""
    # Arabic numerals with configurable digit range (standalone lines)
    text = re.sub(rf"^\d{{{page_min},{page_max}}}\s*$", "", text, flags=re.MULTILINE)
    # Roman numerals (surrounded by blank lines)
    text = re.sub(
        r"\n\n(?:x{0,3}(?:ix|iv|v?i{0,3}))\n\n",
        "\n\n", text, flags=re.IGNORECASE,
    )
    return text


def fix_running_headers(text: str, patterns: list[str]) -> str:
    """Remove running header/footer lines matching the given regex patterns."""
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)
    return text


def fix_separators(text: str) -> str:
    """Remove --- page-break separator lines."""
    return re.sub(r"^---\s*$", "", text, flags=re.MULTILINE)


def fix_page_break_headers(text: str) -> str:
    """Remove bare chapter title repetitions that appear immediately after ---.

    Pattern seen in many textbooks:
      ---
      (blank line)
      5. Tensor Products    ← page header repeated as bare text (no #)
      (blank line)

    Only removes short lines (≤60 chars) starting with a numbered title format
    and containing no LaTeX ($), to avoid false-positives on numbered list items.
    """
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        if (
            lines[i].strip() == "---"
            and i + 2 < len(lines)
            and lines[i + 1].strip() == ""
            and re.match(r"^\d+\.\s+[A-Z]", lines[i + 2].strip())
            and not lines[i + 2].strip().startswith("#")
            and len(lines[i + 2].strip()) <= 60
            and "$" not in lines[i + 2]
        ):
            result.append(lines[i])      # keep ---
            result.append(lines[i + 1])  # keep blank line
            i += 3                       # skip title line
            continue
        result.append(lines[i])
        i += 1
    return "\n".join(result)


def fix_empty_headings(text: str) -> str:
    """Remove ## headings with no content."""
    lines = [line for line in text.split("\n") if line.strip() != "##"]
    return "\n".join(lines)


def fix_image_refs(text: str, mode: str = "comment") -> str:
    """Process image references.

    mode:
      'comment'     : convert to <!-- Figure: alt_text -->
      'delete'      : remove the line entirely
      'placeholder' : replace with [Figure]
    """
    if mode == "delete":
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)\n?", "", text)
    elif mode == "placeholder":
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "[Figure]", text)
    else:  # comment
        text = re.sub(
            r"!\[([^\]]*)\]\([^)]*\)",
            lambda m: "<!-- Figure: " + m.group(1) + " -->",
            text,
        )
    return text


def fix_standalone_dots(text: str) -> str:
    """Remove isolated dots left by blank pages."""
    return re.sub(r"\n\n\.\n\n", "\n\n", text)


def fix_excessive_blanks(text: str) -> str:
    """Collapse 4+ consecutive blank lines to 2 (one visible blank line)."""
    return re.sub(r"\n{4,}", "\n\n\n", text)


# ============================================================
# File processing
# ============================================================

def process_file(
    path: Path,
    active_fixes: set[str],
    patterns: list[str],
    remove_separators: bool,
    page_min: int,
    page_max: int,
    image_mode: str,
    dry_run: bool,
    verbose: bool,
    output_path: Path | None = None,
) -> bool:
    """Apply active fixes to a single file. Returns True if content changed."""
    original = path.read_text(encoding="utf-8")
    text = original

    if "html_entities" in active_fixes:
        text = fix_html_entities(text)
    if "page_numbers" in active_fixes:
        text = fix_standalone_page_numbers(text, page_min, page_max)
    if "running_headers" in active_fixes and patterns:
        text = fix_running_headers(text, patterns)
    if "separators" in active_fixes and remove_separators:
        text = fix_separators(text)
    if "page_break_headers" in active_fixes:
        text = fix_page_break_headers(text)
    if "empty_headings" in active_fixes:
        text = fix_empty_headings(text)
    if "image_refs" in active_fixes:
        text = fix_image_refs(text, mode=image_mode)
    if "standalone_dots" in active_fixes:
        text = fix_standalone_dots(text)
    if "excessive_blanks" in active_fixes:
        text = fix_excessive_blanks(text)

    text = text.strip() + "\n"
    changed = text != original

    if verbose and changed:
        diff = "\n".join(difflib.unified_diff(
            original.splitlines(), text.splitlines(),
            fromfile=f"a/{path.name}", tofile=f"b/{path.name}",
            lineterm="", n=1,
        ))
        print(diff)

    if changed and not dry_run:
        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(text, encoding="utf-8")
        else:
            backup = path.with_suffix(".md.bak")
            backup.write_text(original, encoding="utf-8")
            path.write_text(text, encoding="utf-8")

    return changed


# ============================================================
# Verification
# ============================================================

def verify_files(files: list[Path]) -> dict[str, int]:
    """Count remaining issues in the processed files."""
    counts = {"html_entities": 0, "image_refs": 0, "empty_headings": 0}
    for path in files:
        text = path.read_text(encoding="utf-8")
        counts["html_entities"] += len(re.findall(r"&gt;|&lt;|&amp;", text))
        counts["image_refs"] += len(re.findall(r"!\[", text))
        counts["empty_headings"] += len(re.findall(r"(?m)^##\s*$", text))
    return counts


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Clean up OCR-extracted Markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "inputs", nargs="+",
        help="Markdown files or directories to process",
    )
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
        help="Regex pattern for running headers to remove (repeatable)",
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
        help="Digit range for standalone Arabic page numbers (default: 3,4)",
    )
    parser.add_argument(
        "--image-mode",
        choices=["comment", "delete", "placeholder"],
        default="comment",
        help="How to handle image references (default: comment)",
    )
    parser.add_argument(
        "--only",
        default=None,
        help=f"Comma-separated fixes to apply. Choices: {','.join(ALL_FIXES)}",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing any files",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show unified diff for each changed file",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="After processing, report count of remaining issues",
    )
    parser.add_argument(
        "-o", "--output",
        help="Write output to this file (only valid with a single input file)",
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

    active_fixes = set(args.only.split(",")) if args.only else set(ALL_FIXES)

    # Collect files from inputs (files or directories)
    files: list[Path] = []
    for inp in args.inputs:
        p = Path(inp)
        if p.is_dir():
            files.extend(sorted(p.glob("*.md")))
        elif p.exists():
            files.append(p)
        else:
            print(f"Not found: {p}", file=sys.stderr)

    if not files:
        print("No .md files found.", file=sys.stderr)
        sys.exit(1)

    if args.output and len(files) > 1:
        print("Error: --output can only be used with a single input file", file=sys.stderr)
        sys.exit(1)

    mode_label = "[dry-run] " if args.dry_run else ""
    print(f"{mode_label}Processing {len(files)} file(s) ...")
    if args.only:
        print(f"  Active fixes: {args.only}")

    modified = 0
    for path in files:
        output_path = Path(args.output) if args.output else None
        changed = process_file(
            path,
            active_fixes=active_fixes,
            patterns=patterns,
            remove_separators=args.remove_separators,
            page_min=page_min,
            page_max=page_max,
            image_mode=args.image_mode,
            dry_run=args.dry_run,
            verbose=args.verbose,
            output_path=output_path,
        )
        if changed:
            modified += 1
            label = "[would modify]" if args.dry_run else "Modified"
            if output_path:
                suffix = f"  → {output_path}"
            elif not args.dry_run:
                suffix = f"  (backup: {path.with_suffix('.md.bak').name})"
            else:
                suffix = ""
            print(f"  {label:>15}: {path.name}{suffix}")
        elif args.verbose:
            print(f"  {'No changes':>15}: {path.name}")

    print(
        f"\n{mode_label}Done. "
        f"{'Would modify' if args.dry_run else 'Modified'} {modified}/{len(files)} files."
    )

    if args.verify and not args.dry_run:
        print("\n=== Verification ===")
        counts = verify_files(files)
        all_clear = True
        for check, count in counts.items():
            status = "✓" if count == 0 else "✗"
            if count > 0:
                all_clear = False
            print(f"  {status} {check}: {count} remaining")
        if all_clear:
            print("  All checks passed!")
        else:
            print("  Some issues remain. Re-run or check manually.")


if __name__ == "__main__":
    main()
