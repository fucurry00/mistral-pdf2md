"""
Convert Part III.pdf to Markdown using Mistral OCR API.
Processes in chunks to handle large PDFs.
"""
import base64
import os
import io
import time
from pathlib import Path
from dotenv import load_dotenv
from mistralai.client import Mistral
from pypdf import PdfReader, PdfWriter

load_dotenv(Path(__file__).parent / ".env")

CHUNK_SIZE = 20  # pages per API call


def extract_page_range(pdf_path, start, end):
    """Extract pages [start, end) (0-indexed) as base64."""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for i in range(start, min(end, len(reader.pages))):
        writer.add_page(reader.pages[i])
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


def ocr_chunk(client, b64_pdf):
    response = client.ocr.process(
        model="mistral-ocr-latest",
        document={"type": "document_url", "document_url": f"data:application/pdf;base64,{b64_pdf}"},
        include_image_base64=True,
    )
    return response


def save_images(response, images_dir, img_offset):
    count = 0
    for page in response.pages:
        for img in (page.images or []):
            data = getattr(img, "image_base64", None)
            if data:
                if data.startswith("data:image"):
                    data = data.split(",", 1)[1]
                (images_dir / f"img-{img_offset + count}.jpeg").write_bytes(base64.b64decode(data))
                count += 1
    return count


def convert(pdf_path, output_path, chunk_size=CHUNK_SIZE):
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env")

    pdf_path = Path(pdf_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    images_dir = output_path.parent / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Converting: {pdf_path.name} ({total_pages} pages)")

    client = Mistral(api_key=api_key)
    all_markdown = []
    img_offset = 0

    chunks = range(0, total_pages, chunk_size)
    for i, start in enumerate(chunks):
        end = min(start + chunk_size, total_pages)
        print(f"  Chunk {i+1}/{len(chunks)}: pages {start+1}-{end}...")

        b64 = extract_page_range(pdf_path, start, end)
        response = ocr_chunk(client, b64)

        chunk_md = "\n\n---\n\n".join(p.markdown for p in response.pages)
        saved = save_images(response, images_dir, img_offset)
        if saved > 0:
            chunk_md = chunk_md.replace("](img-", "](images/img-")
        img_offset += saved
        all_markdown.append(chunk_md)

        # avoid rate limiting
        if end < total_pages:
            time.sleep(1)

    markdown = "\n\n---\n\n".join(all_markdown)
    output_path.write_text(markdown, encoding="utf-8")

    print(f"\nDone!")
    print(f"  Output: {output_path}")
    print(f"  Pages: {total_pages}")
    print(f"  Chars: {len(markdown)}")
    print(f"  Images: {img_offset}")


if __name__ == "__main__":
    root = Path(__file__).parent
    convert(
        pdf_path=root / "pdf-src/Part III.pdf",
        output_path=root / "mistral-output/Part III.md",
    )
