# AGENTS.md

## Scope

This repository manages a PDF-to-Markdown pipeline. Follow the documentation map
in README.md and the current behavior contract in SPEC.md.

## Documentation Rules

- Do not add session resume commands or temporary run notes as committed docs.
- Keep `SPEC.md` short and current; do not use it as an implementation journal.
- Put runnable usage in the nearest README.
- Put narrow design notes under `docs/` only when they are still actively useful.
- Prefer updating existing docs over adding new top-level Markdown files.

## Implementation Notes

- Main app: `apps/mistral-ocr-process/`
- Proofreading package: `apps/mistral-ocr-process/proofread-ocr/`
- Use `uv run ...` command forms in docs.
- `convert-pdf` takes output as a positional argument, not `-o`.
- Current proofreading backend is Antigravity CLI (`agy`).

## Validation

Before committing documentation changes:

- Run `git diff --check`.
- Search for stale references such as `.claude`, `python3 pipeline`,
  `Gemini CLI`, `SESSIONS`, and `convert-pdf -o`.
