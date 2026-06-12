# mistral-pdf2md

PDF to Markdown conversion pipeline using Mistral OCR, rule-based cleanup, and
LLM-based proofreading.

## Architecture

```
PDF
  -> Mistral OCR
  -> Rule-based cleanup
  -> OCR proofreading
     - rewrite mode: corrected chunk text
     - hashline mode: validated Hashline patch
  -> Markdown + diff report + stats
```

The proofreading stage currently uses Antigravity CLI (`agy`) as the Gemini
execution backend. A future OpenAI backend should target the Responses API for
synchronous chunk proofreading; an OpenAI Batch API executor is a good fit for
large asynchronous runs, but is intentionally not implemented yet. Codex App
Server is not the right boundary for this batch text-to-text stage because it is
designed for rich Codex client integrations with threads, approvals, and
streamed agent events.

The default proofreading edit mode is `rewrite`, where the model returns the
fully corrected chunk. An experimental `hashline` mode is available in
`apps/mistral-ocr-process/proofread-ocr`: the model returns a compact Hashline
patch, and a Bun/TypeScript sidecar applies it with `@oh-my-pi/hashline` against
the original chunk snapshot before saving the corrected text. This keeps the
full `oh-my-pi` agent out of the production path while reusing its safer
line-anchored patch applier.

See:

- [`apps/mistral-ocr-process/proofread-ocr/README.md`](apps/mistral-ocr-process/proofread-ocr/README.md)
- [`apps/mistral-ocr-process/proofread-ocr/docs/hashline-edit-mode.md`](apps/mistral-ocr-process/proofread-ocr/docs/hashline-edit-mode.md)

### Apps

| App | Description |
| --- | --- |
| `apps/mistral-ocr-process/` | Core pipeline: OCR → cleanup → proofread |
| `apps/mistral-ocr-process/proofread-ocr/` | Chunked OCR proofreading with `rewrite` and experimental `hashline` edit modes |
| `apps/mcp-server/` | MCP server exposing the pipeline to Claude |

## Quick Start

```bash
# Full pipeline (OCR → cleanup → proofread)
cd apps/mistral-ocr-process
uv run pipeline input.pdf output/

# Proofread an existing Markdown file
cd apps/mistral-ocr-process/proofread-ocr
uv run proofread-ocr input.md

# Experimental Hashline patch mode
bun install
uv run proofread-ocr input.md --edit-mode hashline

# Via MCP (Claude integration)
cd apps/mcp-server
uv run pdf2md-mcp
```

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- Mistral API key in `.env` (`MISTRAL_API_KEY=...`)
- [Antigravity CLI](https://github.com/google-gemini/adk-python) (`agy`)
- [Bun](https://bun.sh/) 1.3.14+ only when using `--edit-mode hashline`
