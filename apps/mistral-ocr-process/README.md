# mistral-ocr-process

PDF-to-Markdown conversion pipeline: Mistral OCR → rule-based cleanup → Gemini proofreading.

## Pipeline

```
PDF ──> Stage 1 ──> Stage 2 ──> Stage 3
        Mistral     Rule-based   Gemini
        OCR         Cleanup      Proofread
```

| Stage | Script | What it does |
| --- | --- | --- |
| 1. OCR | `convert_pdf_to_markdown.py` | Converts PDF pages to Markdown via Mistral OCR API |
| 2. Cleanup | `cleanup_ocr.py` | Removes OCR artifacts with regex rules (general or math mode) |
| 3. Proofread | `proofread-ocr/` | Context-aware LLM proofreading via Antigravity CLI (4-phase) |

All three stages are orchestrated by `pipeline.py`.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [Mistral API key](https://docs.mistral.ai/) in `.env` (`MISTRAL_API_KEY=...`)
- [Antigravity CLI](https://github.com/google-gemini/adk-python) (`agy`) for stage 3

## Quick Start

```bash
uv sync

# Full pipeline: OCR → cleanup → proofread
uv run pipeline input.pdf output/

# OCR + cleanup only (skip proofreading)
uv run pipeline input.pdf output/ --steps ocr,cleanup

# Cleanup only
uv run cleanup-ocr document.md

# Run proofreading standalone
cd proofread-ocr && uv run proofread-ocr input.md
```

## Components

### `pipeline.py` — Orchestrator

Runs all 3 stages in sequence. Supports single file or batch directory processing.

```bash
uv run pipeline input.pdf [output_dir] [options]
uv run pipeline pdf_dir/ [output_dir]          # batch mode

# Options
--mode math|general            # cleanup mode (default: math)
--steps ocr,cleanup,proofread  # select stages (default: all)
--preset dummit-foote          # book-specific header patterns
--pages "1-50"                 # page selection (single file only)
--chunk-size 20                # pages per OCR API call (default: 20)
--dry-run                      # preview without processing
```

Output structure:
```
output/{stem}/
├── {stem}.md           # final Markdown (proofread result)
├── {stem}.md.bak       # pre-proofread backup
├── .proofread/         # proofread working files (chunks, diffs, stats)
└── images/             # extracted images
```

### `convert_pdf_to_markdown.py` — Mistral OCR

Converts PDF to Markdown via the Mistral OCR API. Supports page selection, chunked processing for large files, and resume from interruption (`.progress.json`).

```bash
uv run convert-pdf input.pdf -o output.md
uv run convert-pdf input.pdf -o output.md --pages "1-10"
```

### `cleanup_ocr.py` — Rule-based Cleanup

Regex-based cleanup with two modes:

**General mode** (9 fixes): HTML entities, page numbers, running headers, separators, repeated titles, empty headings, image refs, standalone dots, excessive blanks.

**Math mode** (14 fixes, default): All general fixes plus tab corruption, spaced `\text{}`, connective spacing, author/CAPS headers, empty `$$` blocks.

```bash
uv run cleanup-ocr file.md                       # math mode (default)
uv run cleanup-ocr file.md --mode general
uv run cleanup-ocr directory/                    # batch
uv run cleanup-ocr file.md --preset dummit-foote
uv run cleanup-ocr file.md --dry-run --verbose
```

No external dependencies (stdlib only).

### `proofread-ocr/` — LLM Proofreading

A separate Python package for context-aware proofreading via Antigravity CLI (`agy`). See [proofread-ocr/README.md](proofread-ocr/README.md) for details.

4-phase pipeline: context extraction → chunk splitting → parallel proofreading → merge with diff report.

```bash
cd proofread-ocr
uv sync
uv run proofread-ocr input.md
```

## Directory Structure

```
mistral-ocr-process/
├── pyproject.toml              # Project config + script entries
├── pipeline.py                 # Orchestrator (all 3 stages)
├── convert_pdf_to_markdown.py  # Stage 1: Mistral OCR API
├── cleanup_ocr.py              # Stage 2: Rule-based cleanup
├── .env                        # API keys (not committed)
└── proofread-ocr/              # Stage 3: LLM proofreading (Python package)
    ├── pyproject.toml
    ├── src/proofread_ocr/
    ├── tests/
    └── prompts/
```
