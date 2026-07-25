# pdf-curator

`pdf-curator` converts a PDF into a source-referenced `curated.md` for local AI
agents. Every emitted content block retains a PDF page range, and rendering fails
closed if provenance is missing.

This is a new implementation boundary. `apps/mistral-ocr-process/` and
`proofread-ocr/` are reference-only and are not imported or executed.

## Usage

```bash
cd apps/pdf-curator

# Live Mistral OCR (requires MISTRAL_API_KEY in the process environment)
uv run pdf-curator input.pdf output/

# Offline recorded OCR response
uv run pdf-curator input.pdf output/ \
  --from-ocr-json tests/fixtures/simple_ocr.json \
  --debug

# Restrict processing to one-based source pages
uv run pdf-curator input.pdf output/ --pages 1-20

# Override the fail-closed content retention floor
uv run pdf-curator input.pdf output/ --min-content-retention 0.8
```

Normal output contains `curated.md`. `--debug`, and every validation failure,
writes `debug/` with raw OCR, normalized pages, blocks, proposals, gate
decisions, applied diffs, and warnings.

All mutations use one of three channels: deterministic `auto_prepass`, bounded
single `edit`, or deterministic `replace_all`. A `ProposalClient` supplies typed
Pass 2 proposals; the default client is `NoOpProposalClient`. Recorded OCR JSON
is extraction input only and cannot inject edit proposals.

## Tests

```bash
uv run pytest tests/ -v
```

Recorded OCR fixtures are the default test path. No network or API key is
required for them.

## API key boundary

`pdf-curator` deliberately does not read `.env` files. Live OCR accepts the key
only from the already-populated `MISTRAL_API_KEY` process variable.

File permissions cannot make a user-owned `.env` readable by this process but
unreadable by Codex running as the same OS user. If the key must be unavailable
to Codex, do not place it in this workspace and do not run the live command
through Codex. Inject it from a user-controlled terminal or an access-controlled
secret broker, then run the command outside the Codex session.
