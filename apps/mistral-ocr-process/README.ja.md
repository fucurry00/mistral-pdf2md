# mistral-ocr-process

PDF→Markdown 変換パイプライン: Mistral OCR、ルールベースクリーンアップ、LLM校正。

[English README](README.md)

## パイプライン

```
PDF ──> Stage 1 ──> Stage 2 ──> Stage 3 ──> Stage 4（任意）
        Mistral     ルールベース  Gemini       LLM
        OCR         クリーンアップ 分析         校正
```

| ステージ | スクリプト | 機能 |
| --- | --- | --- |
| 1. OCR | `convert_pdf_to_markdown.py` | Mistral OCR API で PDF を Markdown に変換 |
| 2. クリーンアップ | `cleanup_ocr.py` | 正規表現ルールで OCR アーティファクトを除去（汎用/数学モード） |
| 3. 分析 | `pipeline.py`（内蔵） | Gemini CLI で残存アーティファクトを検出 |
| 4. 校正 | `proofread-ocr/` | 文脈ベースの LLM 校正（4フェーズパイプライン） |

Stage 1〜3 は `pipeline.py` で一括実行。Stage 4 は独立実行。

## 前提条件

- Python 3.11+
- [Mistral API キー](https://docs.mistral.ai/) を `.env` に設定（`MISTRAL_API_KEY=...`）
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)（Stage 3, 4 で使用）
- Python パッケージ: `mistralai`, `pypdf`, `python-dotenv`（Stage 1 のみ）

## クイックスタート

```bash
# フルパイプライン: OCR → クリーンアップ → 分析
python3 pipeline.py input.pdf output/

# クリーンアップのみ（数学モード、デフォルト）
python3 cleanup_ocr.py document.md

# クリーンアップのみ（汎用モード）
python3 cleanup_ocr.py document.md --mode general

# LLM 校正（別ツール）
cd proofread-ocr && uv run proofread-ocr ../output/document/document.md
```

## コンポーネント

### `pipeline.py` — オーケストレータ

Stage 1〜3 を順次実行。単一ファイルまたはディレクトリのバッチ処理に対応。

```bash
python3 pipeline.py input.pdf [output_dir] [options]
python3 pipeline.py pdf_dir/ [output_dir]              # バッチモード

# オプション
--mode math|general     # クリーンアップモード（デフォルト: math）
--steps ocr,cleanup,analyze  # 実行ステージの選択（デフォルト: 全部）
--preset dummit-foote   # 書籍固有のヘッダパターン
--pages "1-50"          # ページ選択（単一ファイルのみ）
--chunk-size 20         # OCR API 1回あたりのページ数（デフォルト: 20）
--dry-run               # プレビューのみ
```

出力構造:
```
output/{stem}/
├── {stem}.md           # クリーンアップ済み Markdown
├── {stem}.md.bak       # クリーンアップ前のバックアップ
├── {stem}.analysis.md  # Gemini アーティファクト分析レポート
└── images/             # 抽出画像
```

### `convert_pdf_to_markdown.py` — Mistral OCR

Mistral OCR API で PDF を Markdown に変換。ページ選択、大ファイルのチャンク処理、中断からの再開（`.progress.json`）に対応。

```bash
python3 convert_pdf_to_markdown.py input.pdf -o output.md
python3 convert_pdf_to_markdown.py input.pdf -o output.md --pages "1-10"
```

依存パッケージ: `mistralai`, `pypdf`, `python-dotenv`

### `cleanup_ocr.py` — ルールベースクリーンアップ

正規表現ベースのクリーンアップ。2つのモード:

**汎用モード**（9修正）: HTML エンティティ、ページ番号、ランニングヘッダ、区切り線、タイトル重複、空見出し、画像参照、孤立ドット、過剰空行。

**数学モード**（14修正、デフォルト）: 汎用修正に加え、タブ化け、`\text{}` 内スペース、接続詞スペーシング、著者名/大文字ヘッダ、空数式ブロック。

```bash
python3 cleanup_ocr.py file.md                         # 数学モード（デフォルト）
python3 cleanup_ocr.py file.md --mode general
python3 cleanup_ocr.py directory/                       # バッチ
python3 cleanup_ocr.py file.md --preset dummit-foote
python3 cleanup_ocr.py file.md --only=html_entities,spaced_text
python3 cleanup_ocr.py file.md --dry-run --verbose
python3 cleanup_ocr.py file.md --verify
```

外部依存なし（標準ライブラリのみ）。

### `proofread-ocr/` — LLM 校正

Gemini CLI を使った文脈ベースの校正を行う独立した Python パッケージ。詳細は [proofread-ocr/README.ja.md](proofread-ocr/README.ja.md) を参照。

4フェーズ: コンテキスト抽出 → チャンク分割 → 並列校正 → マージ+差分レポート。

```bash
cd proofread-ocr
uv sync
uv run proofread-ocr input.md
```

## ディレクトリ構成

```
mistral-ocr-process/
├── pipeline.py                 # オーケストレータ（Stage 1-3）
├── convert_pdf_to_markdown.py  # Stage 1: Mistral OCR API
├── cleanup_ocr.py              # Stage 2: ルールベースクリーンアップ
├── .env                        # API キー（コミット対象外）
├── proofread-ocr/              # Stage 4: LLM 校正（Python パッケージ）
│   ├── pyproject.toml
│   ├── src/proofread_ocr/
│   ├── tests/
│   └── prompts/
└── workspace/                  # テストデータとサンプル出力
```
