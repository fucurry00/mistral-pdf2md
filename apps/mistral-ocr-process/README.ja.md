# mistral-ocr-process

PDF から Markdown への変換パイプラインです。Mistral OCR、ルールベースクリーンアップ、LLM 校正を順に実行します。任意で LLM cleanup planner を挟み、本文ではなく `cleanup_plan.json` だけを生成できます。

[English README](README.md)

## パイプライン

```
PDF ──> Stage 1 ──> Stage 2 ──> Stage 3
        Mistral     ルールベース  Antigravity
        OCR         Cleanup       Proofread
```

| ステージ | スクリプト | 機能 |
| --- | --- | --- |
| 1. OCR | `convert_pdf_to_markdown.py` | Mistral OCR API で PDF を Markdown に変換 |
| 2a. Cleanup planner | `pipeline.py --steps plan-cleanup,...` | 任意。LLM が `cleanup_plan.json` だけを生成 |
| 2b. Cleanup | `cleanup_ocr.py` | 正規表現ルールで OCR アーティファクトを除去 |
| 3. Proofread | `proofread-ocr/` | Antigravity CLI (`agy`) 経由で文脈ベース校正 |

3ステージは `pipeline.py` で一括実行できます。

## 前提条件

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- `.env` の Mistral API キー（`MISTRAL_API_KEY=...`）
- Stage 3 を使う場合は Antigravity CLI (`agy`)
- `--edit-mode hashline` を使う場合のみ Bun 1.3.14+

## クイックスタート

```bash
uv sync

# フルパイプライン: OCR → cleanup → proofread
uv run pipeline input.pdf output/

# OCR + cleanup のみ
uv run pipeline input.pdf output/ --steps ocr,cleanup

# OCR + cleanup plan + deterministic cleanup + proofread
uv run pipeline input.pdf output/ --steps ocr,plan-cleanup,cleanup,proofread

# cleanup のみ
uv run cleanup-ocr document.md

# proofread 単体実行
cd proofread-ocr
uv run proofread-ocr input.md
```

## コンポーネント

### `pipeline.py`

単一 PDF または PDF ディレクトリを処理するオーケストレータです。

```bash
uv run pipeline input.pdf [output_dir] [options]
uv run pipeline pdf_dir/ [output_dir]

--mode math|general
--steps ocr,cleanup,proofread
--steps ocr,plan-cleanup,cleanup,proofread
--preset dummit-foote
--pages "1-50"
--chunk-size 20
--cleanup-plan cleanup_plan.json
--planner-timeout 180
--dry-run
```

出力構造:

```text
output/{stem}/
├── {stem}.md
├── {stem}.md.bak
├── cleanup_plan.json
├── .proofread/
└── images/
```

### `convert_pdf_to_markdown.py`

Mistral OCR API で PDF を Markdown に変換します。ページ選択、チャンク処理、中断からの再開に対応します。

```bash
uv run convert-pdf input.pdf output.md
uv run convert-pdf input.pdf output.md --pages "1-10"
```

### `cleanup_ocr.py`

正規表現ベースのクリーンアップです。

- `general`: 汎用 OCR アーティファクト除去。
- `math`: デフォルト。LaTeX/数学文書向け修正を追加。

```bash
uv run cleanup-ocr file.md
uv run cleanup-ocr file.md --mode general
uv run cleanup-ocr directory/
uv run cleanup-ocr file.md --preset dummit-foote
uv run cleanup-ocr file.md --plan cleanup_plan.json
uv run cleanup-ocr file.md --dry-run --verbose
```

`cleanup_plan.json` は実行コードではなく設定 DSL です。主なフィールドは
`mode`, `preset`, `header_patterns`, `page_header_author`,
`remove_separators`, `disabled_fixes`, `only_fixes`, `page_number_range`,
`image_mode` です。未知のフィールド、未知の fix、壊れた正規表現は拒否されます。

### `proofread-ocr/`

Antigravity CLI (`agy`) を使う独立パッケージです。詳細は [proofread-ocr/README.ja.md](proofread-ocr/README.ja.md) を参照してください。

4フェーズ: context extraction → chunk splitting → parallel proofreading → merge。

## ディレクトリ構成

```text
mistral-ocr-process/
├── pyproject.toml
├── pipeline.py
├── convert_pdf_to_markdown.py
├── cleanup_ocr.py
└── proofread-ocr/
    ├── pyproject.toml
    ├── src/proofread_ocr/
    ├── tests/
    └── prompts/
```
