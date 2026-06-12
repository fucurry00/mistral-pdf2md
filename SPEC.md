# Current Specification

This document records the current behavior of the repository at a high level.
Operational usage belongs in the nearest README; implementation details belong
in code and tests.

## Scope

`mistral-pdf2md` converts PDFs into Markdown through a three-stage pipeline:

1. Mistral OCR converts PDF pages to Markdown and extracted images.
2. Rule-based cleanup removes common OCR artifacts.
3. `proofread-ocr` performs LLM-based proofreading on the Markdown.

The supported implementation lives under `apps/mistral-ocr-process/`.

## Entry Points

From `apps/mistral-ocr-process/`:

```bash
uv run pipeline input.pdf output/
uv run pipeline input.pdf output/ --steps ocr,cleanup
uv run convert-pdf input.pdf output.md
uv run cleanup-ocr output.md
```

From `apps/mistral-ocr-process/proofread-ocr/`:

```bash
uv run proofread-ocr input.md
uv run proofread-ocr input.md --dry-run --verbose
uv run pytest tests/ -v
```

## Pipeline Contract

The default `pipeline` command runs:

```text
PDF -> Mistral OCR -> cleanup-ocr -> proofread-ocr -> Markdown
```

The orchestrator supports `--steps ocr,cleanup,proofread`, `--mode
math|general`, `--preset`, `--pages`, `--chunk-size`, and `--dry-run`.

Output for a single PDF is written to:

```text
output/{stem}/
├── {stem}.md
├── {stem}.md.bak
├── .proofread/
└── images/
```

## OCR Stage

`convert_pdf_to_markdown.py` calls the Mistral OCR API with
`mistral-ocr-latest`. It supports page selection, chunked processing, image
extraction, and resume via `.{output_stem}.progress.json`.

Required environment:

- `MISTRAL_API_KEY` in `apps/mistral-ocr-process/.env`
- Python 3.11+
- `uv`

## Cleanup Stage

`cleanup_ocr.py` is stdlib-only and has two modes:

- `general`: generic OCR artifact cleanup.
- `math`: default mode; includes LaTeX/math-specific repairs.

The stage can process files or directories and can run in dry-run/verbose mode.

## Proofreading Stage

`proofread-ocr` is a separate Python package under
`apps/mistral-ocr-process/proofread-ocr/`. It runs four phases:

1. Context extraction.
2. Chunk splitting.
3. Parallel proofreading through Antigravity CLI (`agy`).
4. Merge with diff and stats output.

The default edit mode is `rewrite`. Experimental `hashline` mode uses a Bun
sidecar and `@oh-my-pi/hashline` to apply compact patches.

## Documentation Policy

- `README.md`: repository overview and documentation map.
- `SPEC.md`: short current behavior contract only.
- App READMEs: runnable usage for each app/package.
- `docs/*.md`: focused design notes that are still useful.
- Session/resume notes are intentionally not versioned as project
  documentation.
