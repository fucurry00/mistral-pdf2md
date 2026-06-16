# proofread-ocr

LLM-based proofreading pipeline for OCR-converted Markdown documents, powered by a completion API (Anthropic or Google Gemini).

Detects and corrects context-dependent OCR errors (character confusion, broken LaTeX, cross-reference mismatches) that rule-based cleanup scripts cannot handle.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- An API key for the chosen provider:
  - `GEMINI_API_KEY` for Gemini models (default: `gemini-3.1-flash-lite-preview`)
  - `ANTHROPIC_API_KEY` for Claude models (e.g. `claude-haiku-4-5-20251001`)
- [Bun](https://bun.sh/) 1.3.14+ if using `--edit-mode hashline`
- macOS (Apple Silicon) — tested environment

## Installation

```bash
cd proofread-ocr
uv sync
bun install  # only required for --edit-mode hashline
```

## Quick Start

```bash
# Full pipeline (all 4 phases)
uv run proofread-ocr input.md

# Dry run — preview chunk splits without calling the LLM
uv run proofread-ocr input.md --dry-run --verbose
```

## Pipeline Overview

```
input.md ──> Phase 1 ──> Phase 2 ──> Phase 3 ──> Phase 4 ──> output.md
             Context      Chunk       Parallel     Merge
             Extraction   Splitting   Proofread    + Review
```

## LLM Backend

The pipeline calls a completion API directly through the official provider SDK.
The provider is inferred from the `--model` name at the `run_llm()` boundary in
`src/proofread_ocr/llm.py`:

- names containing `gemini` → Google GenAI SDK (`GEMINI_API_KEY`)
- names containing `claude`/`haiku`/`sonnet`/`opus` → Anthropic SDK (`ANTHROPIC_API_KEY`)

`run_llm()` takes `prompt + context + chunk` and returns corrected Markdown (or a
Hashline patch in `hashline` mode). Switching or adding a provider is a change at
this single seam, not a rename across the codebase. This replaces the earlier
Antigravity CLI (`agy`) subprocess backend.

### Phase 1: Context Extraction

Reads the entire document and extracts shared context for proofreading:

- **Notation Table** — symbols and their meanings
- **Structure Outline** — numbered list of chapters, sections, theorems
- **Terminology Whitelist** — domain-specific terms that must not be "corrected"

After extraction, the pipeline pauses for human review (skip with `--skip-context-review`).

### Phase 2: Chunk Splitting

Splits the document at `##` / `###` heading boundaries into chunks of ~20,000 tokens each. Adjacent chunks share 5-line overlaps marked with `<!-- OVERLAP_START/END -->` to preserve cross-boundary context.

### Phase 3: Parallel Proofreading

Each chunk is sent to the completion API in parallel (`prompt + context + chunk` via `run_llm()`). Every correction is annotated:

```markdown
homomorphism <!-- FIXED: homornorphism -> homomorphism | OCR: rn -> m -->
```

Supports resume — already-completed chunks are skipped on re-run.

Hashline mode is available as an experimental safer editing path:

```bash
uv run proofread-ocr input.md --edit-mode hashline
```

In this mode, the model returns a compact Hashline patch instead of a full
rewritten chunk. The TypeScript sidecar applies it with `@oh-my-pi/hashline`
against the original chunk snapshot before the corrected text is saved.
See [docs/hashline-edit-mode.md](docs/hashline-edit-mode.md) for the design,
failure handling, and validation notes.

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
| `-m, --model <model>` | `gemini-3.1-flash-lite-preview` | Model name (provider inferred from it) |
| `--chunk-size <tokens>` | `20000` | Max tokens per chunk |
| `--overlap-lines <n>` | `5` | Overlap lines between chunks |
| `--concurrency <n>` | `10` | Parallel LLM requests |
| `--timeout <seconds>` | `300` | Timeout per chunk |
| `--skip-context-review` | — | Skip human review of context.md |
| `--context <path>` | — | Use existing context.md (skip Phase 1) |
| `--force` | — | Re-run all chunks ignoring cached results |
| `--dry-run` | — | Show chunk splits and planned calls without executing |
| `--strip-annotations` | — | Remove FIXED/UNCERTAIN comments from output |
| `--verbose` | — | Detailed progress logging |
| `--prompt <path>` | — | Custom proofreading prompt |
| `--edit-mode <mode>` | `rewrite` | `rewrite` or experimental `hashline` patch mode |
| `--preset <name>` | — | Book-specific preset (e.g. `dummit-foote`) |

### Examples

```bash
# Reuse existing context, re-proofread all chunks
proofread-ocr input.md --context context.md --phase proofread --force

# Proofread with Claude instead of the default Gemini model
proofread-ocr input.md --model claude-haiku-4-5-20251001 --concurrency 6

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
│   ├── proofread.md            # Phase 3 rewrite prompt
│   └── proofread_hashline.md   # Phase 3 Hashline patch prompt
├── scripts/
│   └── apply_hashline.ts       # Bun sidecar for @oh-my-pi/hashline
├── src/proofread_ocr/
│   ├── cli.py                  # CLI entry point
│   ├── context.py              # Phase 1: context extraction
│   ├── chunker.py              # Phase 2: chunk splitting
│   ├── proofreader.py          # Phase 3: parallel proofreading
│   ├── merger.py               # Phase 4: merge + reports
│   ├── llm.py                  # Async completion-API wrapper (Anthropic/Gemini)
│   ├── llm_cli.py              # stdin->completion->stdout CLI (proofread-llm)
│   ├── hashline.py             # Python wrapper around the Hashline sidecar
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
- **Minimal dependencies** — stdlib plus the official provider SDKs (`anthropic`, `google-genai`)
