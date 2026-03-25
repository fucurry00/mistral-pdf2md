#!/usr/bin/env python3
"""
Convert PDF to Markdown using Mistral OCR API.

Usage:
    python convert_pdf_to_markdown.py <input.pdf> <output.md> [--pages "1-5"] [--chunk-size 20] [--timeout 120]

Resume: if a previous run was interrupted, re-run the same command.
A progress file (.progress.json) is saved alongside the output and
picked up automatically to skip already-completed chunks.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import io
from pathlib import Path
from dotenv import load_dotenv
from mistralai.client import Mistral
from pypdf import PdfReader, PdfWriter

DEFAULT_TIMEOUT = 120  # seconds


def load_api_key():
    """Load Mistral API key from project root .env"""
    # scripts/ -> mistral-pdf-to-markdown/ -> skills/ -> .claude/ -> project root
    env_path = Path(__file__).parent / ".env"
    load_dotenv(env_path)
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError(f"MISTRAL_API_KEY not found in {env_path}")
    return api_key


def parse_page_selection(page_selection, total_pages):
    """Parse page selection string into list of 0-indexed page numbers."""
    if not page_selection:
        return list(range(total_pages))

    if "-" in page_selection and "," not in page_selection:
        start, end = map(int, page_selection.split("-"))
        pages = list(range(start - 1, end))
    else:
        pages = [int(p) - 1 for p in page_selection.split(",")]

    valid = [p for p in pages if 0 <= p < total_pages]
    skipped = len(pages) - len(valid)
    if skipped:
        print(f"Warning: {skipped} page(s) out of range (PDF has {total_pages} pages), skipping")
    return valid


def extract_page_range(pdf_path, page_indices):
    """Extract given page indices (0-indexed) from PDF and return as base64."""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for i in page_indices:
        writer.add_page(reader.pages[i])
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


def process_with_mistral(api_key, base64_pdf, timeout):
    """Send PDF to Mistral OCR API and return response."""
    import httpx
    client = Mistral(api_key=api_key, timeout_ms=timeout * 1000)
    response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": f"data:application/pdf;base64,{base64_pdf}",
        },
        include_image_base64=True,
    )
    return response


def save_images(ocr_response, output_path, img_offset=0):
    """Extract and save images from OCR response. Returns number of images saved."""
    images_dir = Path(output_path).parent / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for page in ocr_response.pages:
        for img in page.images or []:
            data = getattr(img, "image_base64", None)
            if data:
                if data.startswith("data:image"):
                    data = data.split(",", 1)[1]
                img_bytes = base64.b64decode(data)
                img_path = images_dir / f"img-{img_offset + count}.jpeg"
                img_path.write_bytes(img_bytes)
                print(f"  Saved image: {img_path} ({len(img_bytes) / 1024:.1f} KB)")
                count += 1
    return count


def load_progress(progress_path):
    """Load saved progress from a previous interrupted run."""
    if progress_path.exists():
        return json.loads(progress_path.read_text())
    return {"completed_chunks": [], "markdown_chunks": [], "img_offset": 0}


def save_progress(progress_path, state):
    progress_path.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def convert_pdf_to_markdown(pdf_path, output_path, page_selection=None, chunk_size=20, timeout=DEFAULT_TIMEOUT):
    """
    Main conversion function.

    Args:
        pdf_path: Path to input PDF
        output_path: Path to output markdown file
        page_selection: Optional page selection string (e.g. "1-5" or "1,3,5")
        chunk_size: Pages per API call (default 20). Use None to send all at once.
        timeout: API call timeout in seconds (default 120)
    """
    pdf_path = Path(pdf_path)
    output_path = Path(output_path)
    progress_path = output_path.parent / f".{output_path.stem}.progress.json"

    print(f"Converting: {pdf_path.name}")
    if page_selection:
        print(f"Pages: {page_selection}")

    print("Loading API key...")
    api_key = load_api_key()

    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    pages = parse_page_selection(page_selection, total_pages)

    if not pages:
        raise ValueError(
            f"No valid pages to process. "
            f"PDF has {total_pages} page(s); check your --pages argument."
        )

    print(f"Total pages to process: {len(pages)}")

    if chunk_size is None or len(pages) <= chunk_size:
        # Single API call — no progress file needed
        print("Extracting PDF...")
        b64 = extract_page_range(pdf_path, pages)
        print(f"  Size: {len(b64) / 1024:.1f} KB (base64)")
        print(f"Processing with Mistral OCR API (timeout: {timeout}s)...")
        response = process_with_mistral(api_key, b64, timeout)
        chunk_md = "\n\n---\n\n".join(p.markdown for p in response.pages)
        print("Extracting images...")
        saved = save_images(response, output_path, 0)
        if saved > 0:
            chunk_md = re.sub(
                r"!\[img-(\d+)\.jpeg\]\(img-(\d+)",
                lambda m: f"![img-{m.group(1)}.jpeg](images/img-{m.group(1)}",
                chunk_md,
            )
        markdown_content = chunk_md
        img_total = saved
    else:
        # Chunked processing with resume support
        chunks = [pages[i:i + chunk_size] for i in range(0, len(pages), chunk_size)]
        state = load_progress(progress_path)

        if state["completed_chunks"]:
            print(
                f"Resuming previous run: {len(state['completed_chunks'])}/{len(chunks)} "
                f"chunks already done."
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)

        for idx, chunk in enumerate(chunks):
            if idx in state["completed_chunks"]:
                print(f"  Chunk {idx + 1}/{len(chunks)}: already done, skipping.")
                continue

            print(f"  Chunk {idx + 1}/{len(chunks)}: pages {chunk[0]+1}-{chunk[-1]+1}...")
            b64 = extract_page_range(pdf_path, chunk)
            response = process_with_mistral(api_key, b64, timeout)
            chunk_md = "\n\n---\n\n".join(p.markdown for p in response.pages)
            saved = save_images(response, output_path, state["img_offset"])
            if saved > 0:
                offset = state["img_offset"]
                def _renum(m, _offset=offset):
                    n = _offset + int(m.group(1))
                    return f"![img-{n}.jpeg](images/img-{n}"
                chunk_md = re.sub(r"!\[img-(\d+)\.jpeg\]\(img-(\d+)", _renum, chunk_md)
            state["img_offset"] += saved
            state["markdown_chunks"].append(chunk_md)
            state["completed_chunks"].append(idx)
            save_progress(progress_path, state)

            if idx < len(chunks) - 1:
                time.sleep(1)

        markdown_content = "\n\n---\n\n".join(state["markdown_chunks"])
        img_total = state["img_offset"]

        # Clean up progress file on success
        progress_path.unlink(missing_ok=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_content, encoding="utf-8")

    print(f"\n✓ Conversion complete!")
    print(f"  Markdown: {output_path}")
    print(f"  Pages: {len(pages)}")
    print(f"  Characters: {len(markdown_content)}")
    print(f"  Images: {img_total}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown using Mistral OCR API"
    )
    parser.add_argument("input_pdf", help="Input PDF file path")
    parser.add_argument("output_md", help="Output Markdown file path")
    parser.add_argument("--pages", help='Page selection: "1,3,5" or "1-5"', default=None)
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=20,
        help="Pages per API call for large PDFs (default: 20, 0 = no chunking)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"API call timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )

    args = parser.parse_args()
    chunk_size = args.chunk_size if args.chunk_size > 0 else None

    try:
        convert_pdf_to_markdown(
            args.input_pdf, args.output_md, args.pages, chunk_size, args.timeout
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
