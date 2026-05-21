# mistral-pdf2md

PDF → Markdown conversion pipeline using Mistral OCR and Gemini-based proofreading.

## Architecture

```
PDF ──> Mistral OCR ──> Rule-based Cleanup ──> Gemini Proofread ──> Markdown
```

### Apps

| App | Description |
| --- | --- |
| `apps/mistral-ocr-process/` | Core pipeline: OCR → cleanup → proofread |
| `apps/mcp-server/` | MCP server exposing the pipeline to Claude |

## Quick Start

```bash
# Full pipeline (OCR → cleanup → proofread)
cd apps/mistral-ocr-process
uv run pipeline input.pdf output/

# Via MCP (Claude integration)
cd apps/mcp-server
uv run pdf2md-mcp
```

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- Mistral API key in `.env` (`MISTRAL_API_KEY=...`)
- [Antigravity CLI](https://github.com/google-gemini/adk-python) (`agy`)
