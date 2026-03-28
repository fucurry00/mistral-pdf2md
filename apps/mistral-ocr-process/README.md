# mistral-ocr-process

PDF-to-Markdown conversion pipeline: Mistral OCR, rule-based cleanup, and LLM-based proofreading.

[日本語版 README](README.ja.md)

## Pipeline

```
PDF ──> Stage 1 ──> Stage 2 ──> Stage 3 ──> Stage 4 (optional)
        Mistral     Rule-based   Gemini       LLM
        OCR         Cleanup      Analysis     Proofreading
```

| Stage | Script | What it does |
| --- | --- | --- |
| 1. OCR | `convert_pdf_to_markdown.py` | Converts PDF pages to Markdown via Mistral OCR API |
| 2. Cleanup | `cleanup_ocr.py` | Removes OCR artifacts with regex rules (general or math mode) |
| 3. Analyze | `pipeline.py` (built-in) | Detects remaining artifacts via Gemini CLI |
| 4. Proofread | `proofread-ocr/` | Context-aware LLM proofreading (4-phase pipeline) |

Stages 1-3 are orchestrated by `pipeline.py`. Stage 4 runs independently.

## Prerequisites

- Python 3.11+
- [Mistral API key](https://docs.mistral.ai/) in `.env` (`MISTRAL_API_KEY=...`)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) (for stages 3 and 4)
- Python packages: `mistralai`, `pypdf`, `python-dotenv` (for stage 1 only)

## Quick Start

```bash
# Full pipeline: OCR → cleanup → analyze
python3 pipeline.py input.pdf output/

# Cleanup only (math mode, default)
python3 cleanup_ocr.py document.md

# Cleanup only (general mode)
python3 cleanup_ocr.py document.md --mode general

# LLM proofreading (separate tool)
cd proofread-ocr && uv run proofread-ocr ../output/document/document.md
```

## Components

### `pipeline.py` — Orchestrator

Runs stages 1-3 in sequence. Supports single file or batch directory processing.

```bash
python3 pipeline.py input.pdf [output_dir] [options]
python3 pipeline.py pdf_dir/ [output_dir]              # batch mode

# Options
--mode math|general     # cleanup mode (default: math)
--steps ocr,cleanup,analyze  # select stages (default: all)
--preset dummit-foote   # book-specific header patterns
--pages "1-50"          # page selection (single file only)
--chunk-size 20         # pages per OCR API call (default: 20)
--dry-run               # preview without processing
```

Output structure:
```
output/{stem}/
├── {stem}.md           # cleaned Markdown
├── {stem}.md.bak       # pre-cleanup backup
├── {stem}.analysis.md  # Gemini artifact report
└── images/             # extracted images
```

### `convert_pdf_to_markdown.py` — Mistral OCR

Converts PDF to Markdown via the Mistral OCR API. Supports page selection, chunked processing for large files, and resume from interruption (`.progress.json`).

```bash
python3 convert_pdf_to_markdown.py input.pdf -o output.md
python3 convert_pdf_to_markdown.py input.pdf -o output.md --pages "1-10"
```

Requires: `mistralai`, `pypdf`, `python-dotenv`

### `cleanup_ocr.py` — Rule-based Cleanup

Regex-based cleanup with two modes:

**General mode** (9 fixes): HTML entities, page numbers, running headers, separators, repeated titles, empty headings, image refs, standalone dots, excessive blanks.

**Math mode** (14 fixes, default): All general fixes plus tab corruption, spaced `\text{}`, connective spacing, author/CAPS headers, empty `$$` blocks.

```bash
python3 cleanup_ocr.py file.md                         # math mode (default)
python3 cleanup_ocr.py file.md --mode general
python3 cleanup_ocr.py directory/                       # batch
python3 cleanup_ocr.py file.md --preset dummit-foote
python3 cleanup_ocr.py file.md --only=html_entities,spaced_text
python3 cleanup_ocr.py file.md --dry-run --verbose
python3 cleanup_ocr.py file.md --verify
```

No external dependencies (stdlib only).

### `proofread-ocr/` — LLM Proofreading

A separate Python package that performs context-aware proofreading using Gemini CLI. See [proofread-ocr/README.md](proofread-ocr/README.md) for details.

4-phase pipeline: context extraction → chunk splitting → parallel proofreading → merge with diff report.

```bash
cd proofread-ocr
uv sync
uv run proofread-ocr input.md
```

## Directory Structure

```
mistral-ocr-process/
├── pipeline.py                 # Orchestrator (stages 1-3)
├── convert_pdf_to_markdown.py  # Stage 1: Mistral OCR API
├── cleanup_ocr.py              # Stage 2: Rule-based cleanup
├── .env                        # API keys (not committed)
├── proofread-ocr/              # Stage 4: LLM proofreading (Python package)
│   ├── pyproject.toml
│   ├── src/proofread_ocr/
│   ├── tests/
│   └── prompts/
└── workspace/                  # Test data and sample outputs
```
