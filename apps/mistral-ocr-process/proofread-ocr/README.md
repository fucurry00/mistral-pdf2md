# proofread-ocr

LLM-based proofreading pipeline for OCR-converted Markdown documents, powered by Gemini CLI.

Detects and corrects context-dependent OCR errors (character confusion, broken LaTeX, cross-reference mismatches) that rule-based cleanup scripts cannot handle.

[日本語版 README](README.ja.md)

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) v0.21.1+ (with Gemini 3 Flash access)
- macOS (Apple Silicon) — tested environment

## Installation

```bash
cd proofread-ocr
uv sync
```

## Quick Start

```bash
# Full pipeline (all 4 phases)
uv run proofread-ocr input.md

# Dry run — preview chunk splits without calling Gemini
uv run proofread-ocr input.md --dry-run --verbose
```

## Pipeline Overview

```
input.md ──> Phase 1 ──> Phase 2 ──> Phase 3 ──> Phase 4 ──> output.md
             Context      Chunk       Parallel     Merge
             Extraction   Splitting   Proofread    + Review
```

### Phase 1: Context Extraction

Reads the entire document and extracts shared context for proofreading:

- **Notation Table** — symbols and their meanings
- **Structure Outline** — numbered list of chapters, sections, theorems
- **Terminology Whitelist** — domain-specific terms that must not be "corrected"

After extraction, the pipeline pauses for human review (skip with `--skip-context-review`).

### Phase 2: Chunk Splitting

Splits the document at `##` / `###` heading boundaries into chunks of ~20,000 tokens each. Adjacent chunks share 5-line overlaps marked with `<!-- OVERLAP_START/END -->` to preserve cross-boundary context.

### Phase 3: Parallel Proofreading

Each chunk is sent to Gemini CLI in parallel (`cat prompt context chunk | gemini -p ...`). Every correction is annotated:

```markdown
homomorphism <!-- FIXED: homornorphism -> homomorphism | OCR: rn -> m -->
```

Supports resume — already-completed chunks are skipped on re-run.

### Phase 4: Merge + Review

Reassembles chunks (stripping overlap/metadata markers), then generates:

- `proofread.md` — corrected document with YAML frontmatter
- `diff_report.md` — table of all FIXED/UNCERTAIN corrections
- `stats.json` — execution statistics (timing, token usage, success/failure counts)

## Usage

```
proofread-ocr <input.md> [options]
proofread-ocr <directory/> [options]     # process all .md files
```

### Phase Selection

```bash
proofread-ocr input.md --phase context    # Phase 1 only
proofread-ocr input.md --phase chunk      # Phase 2 only
proofread-ocr input.md --phase proofread  # Phase 3 only
proofread-ocr input.md --phase merge      # Phase 4 only
```

### Key Options

| Option | Default | Description |
| --- | --- | --- |
| `-o, --output <path>` | `{input}_proofread.md` | Output file path |
| `-w, --workdir <path>` | `.proofread/` | Working directory for intermediate files |
| `-m, --model <model>` | `gemini-3-flash-preview` | Gemini model |
| `--chunk-size <tokens>` | `20000` | Max tokens per chunk |
| `--overlap-lines <n>` | `5` | Overlap lines between chunks |
| `--concurrency <n>` | `4` | Parallel Gemini invocations |
| `--timeout <seconds>` | `300` | Timeout per chunk |
| `--skip-context-review` | — | Skip human review of context.md |
| `--context <path>` | — | Use existing context.md (skip Phase 1) |
| `--debug` | — | tmux mode (visual monitoring) |
| `--force` | — | Re-run all chunks ignoring cached results |
| `--dry-run` | — | Show chunk splits and commands without executing |
| `--strip-annotations` | — | Remove FIXED/UNCERTAIN comments from output |
| `--verbose` | — | Detailed progress logging |
| `--prompt <path>` | — | Custom proofreading prompt |

### Examples

```bash
# Reuse existing context, re-proofread all chunks
proofread-ocr input.md --context context.md --phase proofread --force

# Debug mode with tmux
proofread-ocr input.md --debug --concurrency 6

# Clean output without annotation comments
proofread-ocr input.md --strip-annotations

# Batch process a directory
proofread-ocr ocr_output/ -o proofread_output/
```

## Project Structure

```
proofread-ocr/
├── pyproject.toml
├── prompts/
│   ├── extract_context.md      # Phase 1 prompt
│   └── proofread.md            # Phase 3 prompt
├── src/proofread_ocr/
│   ├── cli.py                  # CLI entry point
│   ├── context.py              # Phase 1: context extraction
│   ├── chunker.py              # Phase 2: chunk splitting
│   ├── proofreader.py          # Phase 3: parallel proofreading
│   ├── merger.py               # Phase 4: merge + reports
│   ├── gemini.py               # Async Gemini CLI wrapper
│   └── models.py               # Data models (dataclasses)
├── tests/
│   ├── test_chunker.py
│   ├── test_merger.py
│   └── fixtures/
└── evals/
    └── evals.json
```

## Running Tests

```bash
uv run pytest tests/ -v
```

## Design Principles

- **Faithfulness first** — never alter the author's meaning; proofread, don't rewrite
- **Transparency** — every fix is annotated with original text, correction, and reason
- **Idempotency** — re-runnable with resume support; interrupted runs continue from where they stopped
- **Zero external dependencies** — stdlib only (beyond Gemini CLI itself)
