"""Command-line entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pdf_curator.errors import PdfCuratorError
from pdf_curator.pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf-curator",
        description="Convert a PDF into provenance-first curated Markdown",
    )
    parser.add_argument("input_pdf", type=Path, help="source PDF path")
    parser.add_argument("output_dir", type=Path, help="output directory")
    parser.add_argument(
        "--from-ocr-json",
        type=Path,
        help="use a recorded Mistral OCR JSON response instead of live OCR",
    )
    parser.add_argument("--pages", help="one-based page selection, e.g. 1-20 or 1,3,5")
    parser.add_argument(
        "--min-content-retention",
        type=float,
        default=0.7,
        help="minimum source content-word retention required for success (default: 0.7)",
    )
    parser.add_argument("--debug", action="store_true", help="persist the full debug bundle")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = run_pipeline(
            args.input_pdf,
            args.output_dir,
            from_ocr_json=args.from_ocr_json,
            pages=args.pages,
            debug=args.debug,
            min_content_word_retention=args.min_content_retention,
        )
    except (PdfCuratorError, OSError, ValueError) as error:
        print(f"pdf-curator: error: {error}", file=sys.stderr)
        return 1
    print(result.curated_path)
    if result.debug_dir is not None:
        print(result.debug_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
