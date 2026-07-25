# Specification

This document is the **target contract for the v1 refactor** (`refactor/llm-agent`),
derived from `REFACTOR/CONSENSUS.md`. The full design rationale and the v1/v2
boundary live in `REFACTOR/CONSENSUS.md`; this SPEC is the short contract.
Where the target diverges from what is currently built, see **Implementation
Status** at the end — unbuilt behavior is not claimed as current. Operational
usage belongs in the nearest README; implementation details belong in code and
tests.

## Purpose

Convert lecture PDFs into an **original-reference `curated.md`** that local AI
agents (`claude code`, `codex`, `cowork`) can search, cite, and partially read.
The target is machine-usable knowledge, not human pretty-reading. The
faithfulness authority (source of truth) is the source PDF; `curated.md` is the
primary deliverable.

## Pipeline (target)

```text
PDF
 -> OCR (Mistral, single source)            # Q1: text-layer fusion is v2
 -> block classification + page tagging      # Q6: every block carries source page(range)
 -> deterministic pre-pass (minimal)         # repeated header / separators only
 -> chunk-internal editing agent + gate      # Q2 / Q5
 -> global reconciliation (gated agent)      # Q4
 -> curated.md (+ frontmatter metadata)
```

- **Single-source OCR.** Multi-source integration (text layer + OCR + layout
  weighting/conflict detection) is deferred to v2.
- **Block classification** into `title` / `heading` / `paragraph` / `list_item`
  / `table` / `figure_caption` (emitted) plus `header_footer` / `page_number` /
  `unknown` (excluded or debug/warnings).
- **Granularity:** 1 PDF -> 1 `curated.md` by default; large PDFs split into
  per-chapter files with a TOC `curated.md` (split decided by text volume /
  heading structure / chapter boundaries, not page count alone).

## Editing Model

The LLM never holds edit authority. The script owns it. The LLM acts only as
**analyzer / proposer / checker** across three passes (Global Planning ->
Chunk Editing -> Global Reconciliation).

- **Agent tools:** `READ`, `GREP` (read-only, unrestricted); `EDIT` (single,
  script-provided, the only single-change path); `replace_all` (bulk,
  deterministic — the LLM judges, the script applies across all matches).
- **One gate for every mutation:** type check, `before`-exists-in-source check,
  diff log. Triggers are the only variable: auto pre-pass (universally-safe
  rules only, kept minimal) / single `EDIT` / bulk `replace_all`.
- **Two-layer gate (Q5):**
  - *Bright-line invariants (deterministic, non-overridable):* reject net-new
    body prose (hallucination); isolate unjustified bulk content deletion to
    warnings. **Carve-out:** system-generated structural/provenance annotations
    (`Source:` lines, `<!-- PDF p.N -->` markers, derived from page tags) are
    not LLM-authored content and are exempt from the net-new-text rejection.
  - *Grey zone (fuzzy judgment):* judged on objective diff geometry (edit
    distance, word-set delta, hunk size, pattern match), **not** self-reported
    confidence. v1 routes the grey zone to human `warnings`; v2 routes it to a
    **separate-context reviewer agent** that did not author the edit.

### Agent Backend Options

The chunk-internal editing agent (the `READ` / `GREP` / `EDIT` / `replace_all`
role) may be backed by either:

1. **Completion API + hashline patch applier** *(current path).* LLM calls via
   `run_llm()` (Anthropic / Gemini); `@oh-my-pi/hashline` applies compact
   patches as the `EDIT` / `replace_all` backend. Constrained: no large agent
   execution surface.
2. **pi-coding-agent (full `oh-my-pi` agent)** *(option).* Uses the full
   `oh-my-pi` coding agent — native `READ` / `GREP` / `EDIT`, LSP, subagent,
   etc. — directly as the chunk-internal agent. It brings native agentic
   editing power; safety is preserved because the gate is enforced at the tool
   boundary (typed `EDIT`), so the agent's broader authority cannot bypass the
   bright-line invariants. The current code deliberately excludes the full
   agent and reuses only the `@oh-my-pi/hashline` patch applier; this option
   re-introduces the full agent as a selectable backend.

## Provenance and References (Q6)

- **Requirement:** every block MUST be tagged with its source page (range) from
  OCR onward; merges union the tags. Emit **fails closed** if any block lacks a
  page tag. This block->page tag is the single source of truth for page
  references and for the gate's `before`-exists-in-source check.
- **`curated.md` emits:** section + page range under each heading
  (`Source: PDF p.12-18`) and lightweight machine-targeted page-boundary markers
  (`<!-- PDF p.14 -->`). Paragraph/coordinate references are not put in the body;
  coordinates, block IDs, and OCR confidence go to the `--debug` bundle.

## Metadata (frontmatter)

Stored in `curated.md` frontmatter (not a separate file):
`title`, `source_pdf`, `page_count`, `course_name` / `lecture_name`,
`instructor`, `date` / `term`, `section_index` (derived view of page tags),
`glossary` (author term-variant synonym map), `processing_summary`
(OCR + gate stats: N auto / M isolated / K rejected), `warnings`
(low-confidence spots, unresolved tables/figures/formulas). Low-confidence
fields are `uncertain`, not blank.

## Tables, Figures, Formulas

Common fallback: anything not faithfully text-representable -> a pointer to the
authority, `[X on PDF p.N]`.

- **Tables:** convert to Markdown table when clean; broken-table behavior is
  OCR-quality dependent and tuned at implementation time, with
  `[Table on PDF p.X]` as the safe fallback.
- **Figures:** verbatim caption (`figure_caption`) + `[Figure on PDF p.X]`.
  No image embedding, no in-figure text reconstruction, **no AI-Note synthesis
  in v1** (summary/synthesis is a non-goal).
- **Formulas:** low-confidence -> `[Formula on PDF p.X]`.

## Terminology Handling

Author term variation is **not normalized in the body** (faithfulness > coherence).

- OCR-corrupted terms (same word, garbled) -> `bulk_ocr_fix` (auto, faithful).
- Genuine author variants -> recorded in the `glossary` metadata as a synonym
  map; the body is left unchanged. Heading-*level* normalization (`#` vs `##`)
  stays auto because it changes no words.

## Success Criteria

- Generates `curated.md` from a lecture PDF.
- Every section has a PDF page range.
- Repeated headers/footers/page-numbers are largely removed from the body.
- Major headings/lists/paragraphs are preserved.
- Low-confidence spots appear in `warnings`.
- `--debug` exposes extraction candidates, LLM edit candidates, applied diffs.
- Does not break on at least 3 kinds of lecture PDF, where **"does not break"**
  means all of: (1) completes without crash; (2) valid Markdown + frontmatter;
  (3) source content-word retention >= floor (no catastrophic loss); (4) zero
  passed `content_add` (no hallucination, guaranteed by the gate); (5) the other
  criteria above hold. Threshold values are tuned at implementation/test time.

Non-goals (v1): human pretty-reading / reading-flow tuning, summarization,
figure-point synthesis, multi-source fusion, full OCR accuracy, full table/
formula reconstruction, Word/HTML/Docs input, real parallel multi-worker
editing, human review UI, content addition / teaching material, author-term
body unification, Web (claude.ai / chatgpt.com) export.

## Implementation Status (current vs target)

**Currently built** (under `apps/mistral-ocr-process/`):

- OCR: Mistral `mistral-ocr-latest` (`convert_pdf_to_markdown.py`) — page
  selection, chunked processing, image extraction, resume.
- Cleanup: stdlib `cleanup-ocr` (`general` / `math` modes) + opt-in
  `plan-cleanup` static-cleanup DSL (`cleanup_plan.json`).
- Proofread (`proofread-ocr/`): completion-API backend (`run_llm`, Anthropic /
  Gemini; migrated from `agy`, live-unverified per
  `proofread-ocr/docs/backend-migration-status.md`). Four phases: context,
  chunk, proofread, merge. Edit modes: `rewrite` (default) and experimental
  `hashline` (`@oh-my-pi/hashline` sidecar).

**Introduced by this refactor** (not yet built):

- Single-source block model: per-block page tagging + classification taxonomy.
- The gated editing model (typed `EDIT`, two-layer gate, three triggers)
  replacing the `rewrite` / `hashline` binary.
- `curated.md` + frontmatter metadata + page markers; the `[X on PDF p.N]`
  pointer principle; the `glossary` synonym map.
- Global Planning / Global Reconciliation passes per the consensus.
- The **pi-coding-agent** (full `oh-my-pi` agent) backend option.

## Entry Points (current)

From `apps/mistral-ocr-process/`:

```bash
uv run pipeline input.pdf output/
uv run pipeline input.pdf output/ --steps ocr,plan-cleanup,cleanup,proofread
uv run convert-pdf input.pdf output.md
uv run cleanup-ocr output.md --plan cleanup_plan.json
```

From `apps/mistral-ocr-process/proofread-ocr/`:

```bash
uv run proofread-ocr input.md
uv run proofread-ocr input.md --edit-mode hashline
uv run pytest tests/ -v
```

Required: `MISTRAL_API_KEY` (and provider keys for proofread) in
`apps/mistral-ocr-process/.env`; Python 3.11+; `uv`.

## Documentation Policy

- `README.md`: repository overview and documentation map.
- `SPEC.md`: short target contract + current-vs-target status.
- `REFACTOR/CONSENSUS.md`: full v1 design rationale and v1/v2 boundary.
- App READMEs: runnable usage for each app/package.
- `docs/*.md`: focused design notes that are still useful.
