# OCR Cleanup Tool Specification (2-Pass Architecture)

## Overview

This tool automates the process of cleaning up and formatting Markdown files generated from OCR. It is designed for university lecture slides containing repetitive headers, mathematical expressions, and structural noise.

The tool uses the `gemini` CLI in a **2-pass architecture** to ensure global consistency, with optional preprocessing, parallel chunk processing, and post-processing validation.

## Requirements

- **Python 3.13+**
- **Gemini CLI**: `gemini` must be installed and authenticated (`gemini auth login`)

## Directory Structure

```
apps/ocr_cleanup-two_pass/
├── prompt_pass1.md      # Pass 1: global context extraction (YAML output)
├── prompt_pass2.md      # Pass 2: chunk formatting with faithfulness constraints
├── process_markdown.py  # Orchestration script
├── SPEC.md              # This document
├── docs/
│   └── improve-plan.md  # Design notes and improvement ideas
└── workspace/           # Input/output working directory
```

## Architecture

```
[input.md]
    │
    ├─ (--auto-preprocess)
    │   Detect and remove recurring noise lines (headers, footers, nav)
    │
    ├─ Pass 1: Global Context Extraction
    │   Feed entire document → Gemini → YAML global_context
    │   (metadata, symbols, assumed_notation, structure, style_rules)
    │
    └─ Pass 2: Chunk Processing (parallel)
        Split into chunks → for each chunk:
          - context_from_previous (last Definition/Theorem of prev chunk)
          - global_context + context_from_previous + target_chunk → Gemini
        Merge chunks in order → [output.md]
        │
        └─ Post-processing
            LaTeX validation ($, \begin/\end balance)
            OCR-UNCERTAIN item collection
            (--report) → report.md
```

## Pass 1: Global Context Extraction

- Feeds the **entire** raw OCR document to Gemini
- Output is structured **YAML** with 5 keys:
  - `metadata`: title, document_type, chapter_range
  - `symbols`: notations explicitly defined in the document
  - `assumed_notation`: standard math symbols used without definition (e.g., $\mathbb{R}$)
  - `structure`: numbering scheme, block types (Definition, Theorem, etc.)
  - `style_rules`: abbreviations, OCR artifact corrections

## Pass 2: Chunk Processing

- Splits document into chunks (configurable mode and size)
- Each chunk is processed independently and in **parallel** (`--max-workers`)
- Each chunk receives:
  - `global_context`: YAML from Pass 1
  - `context_from_previous`: last Definition/Theorem statement from the previous chunk (for cross-boundary continuity)
  - `target_chunk`: the OCR text to clean
- **Faithfulness constraints** (highest priority):
  - Never add, delete, or rewrite mathematical content
  - Never complete partial proofs or sentences
  - Uncertain text is flagged as `<!-- OCR-UNCERTAIN: original="..." -->`

## Chunking Modes

| Mode | Flag | Behavior |
|------|------|----------|
| `pages` | `--chunk-mode pages` (default) | Split by header pattern, group by `--chunk-size` pages |
| `semantic` | `--chunk-mode semantic` | Group Definition/Theorem/Proof as atomic units under 3000-token budget |

## Components

### `prompt_pass1.md`
Instructs Gemini to analyze the entire document and output structured YAML global context.

### `prompt_pass2.md`
Instructs Gemini to format a single chunk with faithfulness constraints, global context, and cross-chunk continuity.

### `process_markdown.py`
Orchestrator handling: preprocessing → Pass 1 → chunking → Pass 2 (parallel) → merge → post-processing.

## Usage

### Basic

```bash
uv run python apps/ocr_cleanup-two_pass/process_markdown.py <input.md> -o <output.md>
```

### All Options

```bash
uv run python apps/ocr_cleanup-two_pass/process_markdown.py <input.md> -o <output.md> \
  --auto-preprocess \          # 繰り返しノイズ行を自動除去
  --chunk-mode semantic \      # セマンティックチャンキング
  --chunk-size 5 \             # pages モード時のページ数/チャンク
  --header-pattern "regex" \   # pages モード時のページ区切りパターン
  --max-workers 5 \            # Pass 2 並列数
  --report review.md \         # LaTeX警告・OCR-UNCERTAIN一覧を出力
  -p1 prompt_pass1.md \        # Pass 1 プロンプト（省略可）
  -p2 prompt_pass2.md          # Pass 2 プロンプト（省略可）
```

### Example

```bash
# Folland Real Analysis Ch2（デフォルト設定）
uv run python apps/ocr_cleanup-two_pass/process_markdown.py \
  apps/ocr_cleanup-two_pass/workspace/Ch2-Real_Analysis_Folland/main.md \
  -o apps/ocr_cleanup-two_pass/workspace/Ch2-Real_Analysis_Folland/cleaned_main.md

# 別の書籍（カスタムパターン + 自動前処理 + レポート出力）
uv run python apps/ocr_cleanup-two_pass/process_markdown.py input.md -o output.md \
  --auto-preprocess \
  --header-pattern "^Chapter \d+" \
  --chunk-mode semantic \
  --report review.md
```

## CLI Reference

| 引数 | デフォルト | 説明 |
|------|----------|------|
| `input_file` | 必須 | 入力Markdownファイル |
| `-o`, `--output` | 必須 | 出力ファイルパス |
| `-p1`, `--prompt1` | `prompt_pass1.md`（隣） | Pass 1 プロンプトファイル |
| `-p2`, `--prompt2` | `prompt_pass2.md`（隣） | Pass 2 プロンプトファイル |
| `-c`, `--chunk-size` | `5` | ページ数/チャンク（pagesモード） |
| `--header-pattern` | Follandパターン | ページ区切りの正規表現 |
| `--chunk-mode` | `pages` | `pages` または `semantic` |
| `-w`, `--max-workers` | `5` | Pass 2 並列数 |
| `--auto-preprocess` | off | 繰り返しノイズ行の自動除去 |
| `--report` | なし | レポート出力先ファイル |

## Post-processing Validation

出力ファイルに対して自動で実行される：

- **LaTeX検証**: `$` の対応チェック、`\begin`/`\end` の対応チェック
- **OCR-UNCERTAINカウント**: Gemini が挿入した不確実フラグの集計
- `--report` 指定時は上記をMarkdownファイルに保存
