# proofread-ocr

LLM-based OCR proofreading pipeline using Gemini CLI.

## Architecture

4-phase pipeline:
1. **Context extraction** (`context.py`): Extract notation table, structure outline, terminology whitelist
2. **Chunking** (`chunker.py`): Split by `##`/`###` boundaries with overlap markers
3. **Parallel proofreading** (`proofreader.py`): Async subprocess calls to Gemini CLI
4. **Merge + review** (`merger.py`): Reassemble chunks, generate diff report and stats

## Key conventions

- stdlib only (no external dependencies)
- Async I/O via `asyncio.create_subprocess_exec`
- Token estimation: CJK > 30% → 3 chars/token, else 4 chars/token
- All data models in `models.py` as dataclasses with JSON serialization

## Running

```bash
uv run proofread-ocr <input.md> [options]
uv run pytest tests/
```
