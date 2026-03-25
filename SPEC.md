# PDF → Markdown 変換パイプライン 仕様書

## 概要

Mistral OCR API を利用して PDF を Markdown に変換し、後処理でアーティファクトを除去するパイプライン。数学書籍のような LaTeX 数式・図版を含む大容量 PDF を対象に設計されている。

---

## ディレクトリ構成

```
project-root/
├── .env                          # MISTRAL_API_KEY を格納
├── main.py                       # 実行エントリポイント（書籍専用の変換定義）
├── cleanup_ocr.py                # OCR 後処理クリーンアップツール
├── pyproject.toml / uv.lock      # 依存関係
└── .claude/skills/mistral-pdf-to-markdown/
    ├── SKILL.md                  # Claude スキル定義
    └── scripts/
        └── convert_pdf_to_markdown.py   # 汎用変換スクリプト（CLI）
```

---

## コンポーネント 1: convert_pdf_to_markdown.py

**パス:** `.claude/skills/mistral-pdf-to-markdown/scripts/convert_pdf_to_markdown.py`

### 役割

PDF ファイルを受け取り、Mistral OCR API でテキストと画像を抽出し、Markdown ファイルと画像ファイル群として出力する汎用 CLI ツール。

### CLI

```
python convert_pdf_to_markdown.py <input.pdf> <output.md> [オプション]
```

| 引数 | 型 | デフォルト | 説明 |
|------|----|-----------|------|
| `input_pdf` | positional | — | 入力 PDF ファイルパス |
| `output_md` | positional | — | 出力 Markdown ファイルパス |
| `--pages` | str | None（全ページ） | ページ選択: `"1-5"` または `"1,3,5"` |
| `--chunk-size` | int | 20 | API 呼び出しあたりのページ数（0 = チャンクなし） |
| `--timeout` | int | 120 | API タイムアウト（秒） |

### 処理フロー

```
入力 PDF
  ↓
ページ選択の解析（parse_page_selection）
  ↓
チャンク分割（chunk_size ページずつ）
  ↓ ← チャンクごとにループ
  PDF の該当ページを base64 エンコード（extract_page_range）
  ↓
  Mistral OCR API 呼び出し（mistral-ocr-latest）
  ↓
  画像を images/ に保存（save_images）+ グローバル番号付け
  ↓
  Markdown 内の画像参照をグローバル番号に書き換え
  ↓
  進捗を .{stem}.progress.json に保存（resume 対応）
  ↓
チャンク結果を --- で結合
  ↓
output.md に書き出し
```

### 出力構造

```
output.md の親ディレクトリ/
├── output.md           # テキスト + 画像参照を含む Markdown
└── images/
    ├── img-0.jpeg
    ├── img-1.jpeg
    └── ...             # チャンクをまたいで連番（重複なし）
```

### 画像参照フォーマット

```markdown
![img-N.jpeg](images/img-N.jpeg)
```

N はファイル全体でユニークな通し番号。チャンクをまたいでも重複しない。

### API

| 項目 | 値 |
|------|-----|
| モデル | `mistral-ocr-latest` |
| エンドポイント | `client.ocr.process()` |
| 入力形式 | base64 エンコードされた PDF（data URI） |
| 画像取得 | `include_image_base64=True` |
| import パス | `from mistralai.client import Mistral` |

### 環境変数

| 変数名 | 必須 | 説明 |
|--------|------|------|
| `MISTRAL_API_KEY` | ✓ | Mistral API キー |

読み込みパス: スクリプトから 5階層上（`scripts/ → skill/ → skills/ → .claude/ → project-root/`）の `.env`

### エラーハンドリング

| 状況 | 挙動 |
|------|------|
| `MISTRAL_API_KEY` 未設定 | エラーメッセージ（.env のパスを明示）、exit 1 |
| `--pages` が全て範囲外 | エラーメッセージ（PDF のページ数を表示）、exit 1 |
| 一部ページが範囲外 | Warning を表示して継続 |
| API タイムアウト | 例外が main() の try-except で捕捉、exit 1 |
| チャンク中断 | 再実行で `.progress.json` を読み込み、完了済みチャンクをスキップ |

### resume 仕様

- チャンクモード時のみ動作（ページ数 > chunk-size）
- 進捗ファイルパス: `<output>.parent / .{output.stem}.progress.json`
- 保存タイミング: 各チャンク完了直後
- 再開条件: 同一コマンドを再実行（ファイルが存在すれば自動検出）
- 完了時: progress ファイルを自動削除

### 依存パッケージ

```
mistralai
python-dotenv
pypdf
```

---

## コンポーネント 2: cleanup_ocr.py

**パス:** `cleanup_ocr.py`

### 役割

変換後の Markdown から OCR アーティファクトを除去する後処理ツール。インプレース上書き（バックアップあり）または別ファイル出力に対応。

### CLI

```
python cleanup_ocr.py <file.md> [file2.md ...] [オプション]
```

| 引数 | 型 | デフォルト | 説明 |
|------|----|-----------|------|
| `files` | positional（複数可） | — | 処理対象の Markdown ファイル |
| `--preset` | str | None | 書籍プリセット（現在: `dummit-foote`） |
| `--header-pattern` | str（複数指定可） | [] | 除去するランニングヘッダーの正規表現 |
| `--no-remove-separators` | flag | False | `---` を残す |
| `--page-number-range` | str | `"3,4"` | ページ番号とみなす桁数範囲 MIN,MAX |
| `-o` / `--output` | str | None | 別ファイルに出力（単一ファイル時のみ） |

### 処理内容（適用順）

1. **HTML エンティティ変換**: `&amp;` → `&`, `&lt;` → `<`, `&gt;` → `>`, `&nbsp;` → ` `, `&#39;` → `'`, `&quot;` → `"`
2. **単独行ページ番号の除去**: 指定桁数（デフォルト 3〜4 桁）の整数のみの行を削除
3. **ランニングヘッダー/フッターの除去**: `--header-pattern` または `--preset` で指定したパターンにマッチする行を削除
4. **ページ区切り `---` の除去**: 変換スクリプトが挿入した `---` 行を削除（`--no-remove-separators` で無効化）
5. **連続空行の正規化**: 3行以上の連続空行を 1行に圧縮

### 組み込みプリセット

| プリセット名 | 除去パターン |
|-------------|-------------|
| `dummit-foote` | `^Sec\. \d+\.\d+[^\n]*$`（例: `Sec. 10.1 Basic Definitions...`）|
| | `^Chap\. \d+[^\n]*$`（例: `Chap. 10 Introduction to Module Theory`）|

### バックアップ動作

- `-o` 未指定（インプレース）時: 元ファイルを `.md.bak` として保存してから上書き
- `-o` 指定時: バックアップなし、指定パスに出力

---

## パイプライン全体のワークフロー

```
pdf-src/Foo.pdf
  ↓
1. 変換
   uv run python .claude/skills/mistral-pdf-to-markdown/scripts/convert_pdf_to_markdown.py \
     pdf-src/Foo.pdf Foo/Foo.md [--pages ...] [--chunk-size 20] [--timeout 120]
  ↓
Foo/
├── Foo.md        ← OCR 生テキスト（ページ番号・ランニングヘッダー含む）
└── images/       ← 抽出画像（img-0.jpeg, img-1.jpeg, ...）

  ↓
2. 後処理（Dummit & Foote の場合）
   uv run python cleanup_ocr.py Foo/Foo.md --preset dummit-foote
  ↓
Foo/
├── Foo.md        ← クリーン済み Markdown
├── Foo.md.bak    ← 変換前バックアップ
└── images/
```

---

## 環境セットアップ

```bash
# プロジェクトルートで
uv init --name <valid-name>
uv add mistralai python-dotenv pypdf

# .env にキーを追加
echo "MISTRAL_API_KEY=your_key_here" >> .env
```

---

## 制限事項・注意点

| 項目 | 内容 |
|------|------|
| チャンクサイズ | API の入力サイズ上限により 20〜30 ページ推奨 |
| 画像形式 | JPEG のみ（Mistral API の出力に依存） |
| 数式 | LaTeX として出力される。LLM による後処理は数式書き換えリスクがあるため非推奨 |
| resume | チャンクモード（ページ数 > chunk-size）でのみ有効。単一 API 呼び出し時は無効 |
| `--pages` の混在書式 | `"1-5,10"` のような混在書式は未対応。範囲か列挙のいずれか一方を使用 |
