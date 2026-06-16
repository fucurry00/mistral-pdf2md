# proofread-ocr

LLM-based OCR proofreading pipeline using a completion API (Anthropic/Gemini).

## Architecture

4-phase pipeline:
1. **Context extraction** (`context.py`): Extract notation table, structure outline, terminology whitelist
2. **Chunking** (`chunker.py`): Split by `##`/`###` boundaries with overlap markers
3. **Parallel proofreading** (`proofreader.py`): Async completion-API calls via `llm.py` (`run_llm`)
4. **Merge + review** (`merger.py`): Reassemble chunks, generate diff report and stats

## Key conventions

- stdlib plus official provider SDKs (`anthropic`, `google-genai`)
- Provider inferred from `--model` name at the `run_llm()` seam in `llm.py`
- Async I/O via the SDKs' async clients (`AsyncAnthropic`, `client.aio`)
- Token estimation: CJK > 30% → 3 chars/token, else 4 chars/token
- All data models in `models.py` as dataclasses with JSON serialization

## Running

```bash
uv run proofread-ocr <input.md> [options]
uv run pytest tests/
```
