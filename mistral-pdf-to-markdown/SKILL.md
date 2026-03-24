---
name: mistral-pdf-to-markdown
description: Convert PDFs to Markdown using Mistral OCR API with image extraction. Use when you need to extract structured text and images from PDFs, especially for scanned documents or documents with complex formatting. Outputs Markdown with embedded images.
---

# Mistral PDF to Markdown Converter

Convert PDF documents to Markdown format using Mistral's OCR API. Automatically extracts text, formatting, and images.

## When to Use

- Converting research papers or documents to Markdown
- Extracting text from scanned PDFs (OCR capability)
- Preserving document structure with headers and formatting
- Extracting embedded images from PDFs

## Quick Start

Use the conversion script from this skill's directory:

```bash
# Convert entire PDF (auto-chunked, 20 pages per API call)
python scripts/convert_pdf_to_markdown.py input.pdf output.md

# Convert specific pages
python scripts/convert_pdf_to_markdown.py input.pdf output.md --pages "1-5"
python scripts/convert_pdf_to_markdown.py input.pdf output.md --pages "1,3,5"

# Large PDF with custom chunk size
python scripts/convert_pdf_to_markdown.py input.pdf output.md --chunk-size 30

# Custom API timeout (seconds)
python scripts/convert_pdf_to_markdown.py input.pdf output.md --timeout 180

# Resume an interrupted run (just re-run the same command)
python scripts/convert_pdf_to_markdown.py input.pdf output.md
```

## Output Structure

```
Output/PDFConversions/
├── document.md          # Markdown with text and image references
└── images/
    ├── img-0.jpeg      # Extracted images
    ├── img-1.jpeg
    └── ...
```

## Usage in Code

```python
from pathlib import Path
import subprocess

# Run conversion script
result = subprocess.run([
    "python",
    ".claude/skills/mistral-pdf-to-markdown/scripts/convert_pdf_to_markdown.py",
    "input.pdf",
    "Output/PDFConversions/output.md",
    "--pages", "1-10"
], capture_output=True, text=True)

print(result.stdout)
```

## Key Features

- **Markdown formatting**: Preserves headers, lists, and structure
- **Image extraction**: Saves images to `images/` subfolder automatically
- **Page selection**: Extract specific pages or ranges
- **Chunked processing**: Large PDFs are split into chunks (default 20 pages) to avoid API limits
- **Scanned PDF support**: True OCR capability for image-based PDFs
- **Relative paths**: Image references use `![...](images/img-X.jpeg)`

## Requirements

The script requires:
- Mistral API key as `MISTRAL_API_KEY` in `.env` at the project root
- Python packages: `mistralai`, `python-dotenv`, `pypdf`

## Common Use Cases

### Convert Research Paper
```bash
python scripts/convert_pdf_to_markdown.py \
  "Data/papers/research.pdf" \
  "Notes/Paper Markdown/research.md"
```

### Extract Specific Sections
```bash
# Extract pages 10-20 (introduction and methods)
python scripts/convert_pdf_to_markdown.py \
  "paper.pdf" \
  "Notes/Paper Markdown/intro_methods.md" \
  --pages "10-20"
```

### Extract Figures Only
```bash
# Extract pages with figures
python scripts/convert_pdf_to_markdown.py \
  "paper.pdf" \
  "Notes/Paper Markdown/figures.md" \
  --pages "25,27,30,35"
```

## Error Handling

**API Key Not Found:**
```
Error: MISTRAL_API_KEY not found in /path/to/project/.env
```
→ Add `MISTRAL_API_KEY=your_key` to `.env` at the project root

**All Pages Out of Range:**
```
Error: No valid pages to process. PDF has 10 page(s); check your --pages argument.
```
→ Check total page count and fix the `--pages` argument

**Some Pages Out of Range:**
```
Warning: 3 page(s) out of range (PDF has 50 pages), skipping
```
→ Processing continues with the valid pages

**API Rate Limit / Large PDF:**
→ Use `--chunk-size` to reduce pages per request (default is 20).
→ A 1-second delay is automatically inserted between chunks.

**API Timeout:**
```
Error: ... timeout ...
```
→ Increase with `--timeout 180` (default: 120 seconds)

**Interrupted Mid-Run:**
→ Simply re-run the exact same command. Progress is saved per chunk in
  `.{output-name}.progress.json` and completed chunks are skipped automatically.

## Notes

- Images are saved as JPEG files in `images/` subfolder
- Markdown image references are automatically updated to `images/img-X.jpeg`
- Large PDFs may take longer to process due to API limits
- For simple text extraction without OCR, consider using the `pdf` skill instead
- Scanned PDFs benefit most from this skill's OCR capability

## See Also

- `pdf` skill - For local PDF manipulation without API calls
- `reference.md` - Additional details about the Mistral OCR API
