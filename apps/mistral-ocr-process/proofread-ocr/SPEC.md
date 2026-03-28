# proofread-ocr: LLMベースOCR校正パイプライン 設計仕様書

## 概要

OCR→Markdown変換後の文書に残る誤字脱字・記法崩れを、LLM（Gemini 3 Flash）を用いて文脈ベースで校正するパイプライン。既存の機械的クリーンアップ（`cleanup_ocr.py`, `fix_ocr_math_md.py`）では対応不可能な、文脈依存の修正を担う。

### 設計原則

- **忠実性最優先**: 原文の意味・構造を変更しない。校正であり、編集・リライトではない。
- **透明性**: すべての修正にアノテーションを付与し、人間がレビュー可能な状態を維持する。
- **コスト効率**: Gemini CLIのサブスクリプション枠を活用し、API従量課金を回避する。
- **冪等性**: 同じ入力に対して再実行可能。中断からの再開をサポートする。

### 前提条件

- Gemini CLI インストール済み（v0.21.1+）
- Gemini 3 Flash アクセス可能（Google AI Pro/Ultra プラン）
- Python 3.11+, `uv`, macOS (Apple Silicon)
- 入力: Mistral OCR → `cleanup_ocr.py` / `fix_ocr_math_md.py` 処理済みの Markdown ファイル

---

## パイプライン全体像

```
入力 .md ──→ Phase 1 ──→ Phase 2 ──→ Phase 3 ──→ Phase 4 ──→ 出力 .md
             コンテキスト   チャンク     並列校正     マージ
             抽出           分割                      + レビュー
```

Phase 0（前処理）は既存パイプライン（Mistral OCR → cleanup_ocr.py / fix_ocr_math_md.py）が担当。
本ツールは Phase 0 完了後の Markdown を入力として受け取る。

---

## Phase 1: コンテキスト抽出

### 目的

文書全体を読み、後続の並列校正で各チャンクに注入する「共有コンテキスト」を生成する。

### 実行方法

Gemini 3 Flash のロングコンテキスト（1Mトークン）を活用し、文書全体を一括入力。

```bash
gemini -p "@prompts/extract_context.md @input.md" \
  --output-format json \
  -m gemini-3-flash-preview \
  > work/context_raw.json
```

### 出力: `context.md`

3つのセクションからなるMarkdownファイル。

#### 1. 記号テーブル（Notation Table）

文書中で定義・使用されている記号とその意味の対応表。

```markdown
## Notation Table

| 記号      | 意味           | スコープ | 初出 |
| --------- | -------------- | -------- | ---- |
| $G$       | 群 (group)     | Ch.1-5   | §1.1 |
| $G$       | グラフ (graph) | Ch.9     | §9.1 |
| $\varphi$ | 準同型写像     | 全体     | §1.3 |
| $[G:H]$   | 指数 (index)   | 全体     | §3.2 |
```

#### 2. 構造アウトライン（Structure Outline）

章・節・定理・定義・補題の番号付きリスト。相互参照の整合性チェックに使用。

```markdown
## Structure Outline

- Chapter 1: Introduction to Groups
  - §1.1 Basic Axioms
    - Definition 1.1.1: Group
    - Definition 1.1.2: Abelian group
    - Proposition 1.1.3
  - §1.2 Dihedral Groups
    - Theorem 1.2.1
    - ...
```

#### 3. 用語ホワイトリスト（Terminology Whitelist）

書籍固有の術語。LLMが「誤字」と判断して勝手に修正するのを防ぐ。

```markdown
## Terminology Whitelist

- G-set（著者独自用語、§4.1で定義）
- left coset space
- fiber product
- centralizer
- normalizer
```

### 人間レビューポイント

Phase 1 の出力は後続全体の精度に波及するため、`context.md` 生成後に人間が確認・修正するステップを設ける。CLIフラグ `--skip-context-review` で省略可能。

---

## Phase 2: チャンク分割

### 分割戦略

#### 境界の優先順位

1. `##`（セクションレベル）— 最優先の分割境界
2. `###`（サブセクションレベル）— セクションが大きい場合のフォールバック
3. 定理ブロック間の空行 — サブセクション内でも大きい場合の最終手段

`#`（章レベル）は分割境界としない（通常は大きすぎるため）。

#### トークン予算

| パラメータ       | 値                            | 備考                       |
| ---------------- | ----------------------------- | -------------------------- |
| チャンク上限     | 20,000 トークン（デフォルト） | `--chunk-size` で調整可    |
| 共有コンテキスト | 可変（通常 5,000-15,000）     | context.md のサイズ依存    |
| オーバーラップ   | 前後各 5 行                   | `--overlap-lines` で調整可 |

チャンクサイズは大きすぎると「見落とし」が増え、小さすぎると文脈が不足する。
20,000トークンは数学書のセクション1-2個分に相当し、精度と効率のバランス点。

#### オーバーラップ処理

各チャンクに前チャンク末尾5行と次チャンク冒頭5行を含める。

```
chunk_001: [本体 ........... ] + [overlap_after: 5行]
chunk_002: [overlap_before: 5行] + [本体 ........... ] + [overlap_after: 5行]
chunk_003: [overlap_before: 5行] + [本体 ........... ]
```

マージ時にはオーバーラップ部分を除去し、本体のみを連結する。
オーバーラップ部分はマーカーで明示する:

```markdown
<!-- OVERLAP_START -->

（前チャンクの末尾5行）

<!-- OVERLAP_END -->

（本体）

<!-- OVERLAP_START -->

（次チャンクの冒頭5行）

<!-- OVERLAP_END -->
```

#### チャンクメタデータ

各チャンクファイルの冒頭に注入するメタデータ:

```markdown
<!-- CHUNK_META
chunk_id: 003
section: "§3.2 Quotient Groups"
prev_section: "§3.1 Cosets"
next_section: "§3.3 The Isomorphism Theorems"
total_chunks: 24
-->
```

### 出力

```
work/chunks/
├── chunk_001.md
├── chunk_002.md
├── ...
└── chunk_manifest.json   # 全チャンクのメタデータ一覧
```

`chunk_manifest.json`:

```json
{
  "source": "input.md",
  "total_chunks": 24,
  "chunk_size_target": 20000,
  "overlap_lines": 5,
  "chunks": [
    {
      "id": "001",
      "section": "§1.1 Basic Axioms",
      "line_start": 1,
      "line_end": 145,
      "estimated_tokens": 18200
    }
  ]
}
```

---

## Phase 3: 並列校正

### 校正プロンプト設計

プロンプトは3層構造。`prompts/proofread.md` としてテンプレート化する。

#### 第1層: ロール定義とグローバル制約

```markdown
あなたは学術書のOCR校正の専門家です。
OCR処理によって生じた誤りを修正してください。

## 厳守事項

- Markdownの構造（見出しレベル、リスト階層、コードブロック）を変更しない
- LaTeX数式の数学的意味を変更しない（表記の正規化のみ許可）
- 用語ホワイトリストに記載された語を「誤字」として修正しない
- 原文に存在しないテキストを追加しない
- 文体の改変、パラフレーズを行わない
- 内容の要約・省略を行わない

## 修正対象

- OCRによる文字化け・文字の取り違え（例: rn → m, l → 1, O → 0）
- 脱字・衍字（余分な文字の挿入）
- LaTeX記法の崩れ（`\text{}` 内のスペース混入、`$$` のネスト崩れ等）
- 相互参照の番号ずれ（「Theorem 3.2」が構造アウトラインに存在するか確認）
- 句読点・スペースの正規化
- 明らかな単語の分断（OCRが単語途中で改行を入れたケース）

## 修正のアノテーション

修正を行った場合、修正箇所の直後に以下のHTMLコメントを挿入してください:

- 確信度が高い修正: `<!-- FIXED: {原文} → {修正後} | {理由} -->`
- 確信度が低い修正: `<!-- UNCERTAIN: {原文} → {修正案} | {理由} -->`

## 出力形式

校正済みの全文を出力してください。アノテーション以外の追加テキストは不要です。
```

#### 第2層: コンテキストシート

```markdown
## 文書コンテキスト

以下はこの文書全体から抽出した情報です。校正の判断材料として参照してください。

{context.md の内容をここに展開}
```

#### 第3層: チャンク固有の指示

```markdown
## 校正対象

以下のテキストを校正してください。
`<!-- OVERLAP_START -->` と `<!-- OVERLAP_END -->` で囲まれた部分は前後の文脈参照用です。
校正対象は本体部分のみですが、オーバーラップ部分も含めて出力してください。

{chunk_NNN.md の内容}
```

### 実行コマンド

```bash
gemini -p "@prompts/proofread.md @work/context.md @work/chunks/chunk_001.md" \
  --output-format json \
  -m gemini-3-flash-preview \
  > work/results/chunk_001.json
```

### Gemini CLI のパラメータ

| パラメータ     | 値                       | 備考                            |
| -------------- | ------------------------ | ------------------------------- |
| モデル         | `gemini-3-flash-preview` | `--model` で指定                |
| thinking_level | `high`                   | GEMINI.md または API設定で指定  |
| 出力形式       | `json`                   | レスポンス抽出 + 統計取得のため |

### 並列実行制御

#### subprocess モード（デフォルト）

```python
async def run_proofread(chunk_path: Path, context_path: Path, prompt_path: Path, output_path: Path) -> Result:
    proc = await asyncio.create_subprocess_exec(
        "gemini", "-p",
        f"@{prompt_path} @{context_path} @{chunk_path}",
        "--output-format", "json",
        "-m", "gemini-3-flash-preview",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    # JSON パース → レスポンス抽出
    ...
```

並列度は `--concurrency` で制御（デフォルト: 4）。
Gemini CLIのレート制限に応じて調整する。

#### tmux モード（--debug）

```bash
# セッション作成
tmux new-session -d -s proofread

# 各チャンクにペインを割り当て
for chunk in work/chunks/chunk_*.md; do
  id=$(basename "$chunk" .md | sed 's/chunk_//')
  tmux split-window -t proofread \
    "gemini -p '@prompts/proofread.md @work/context.md @$chunk' \
     --output-format json \
     -m gemini-3-flash-preview \
     | tee work/results/chunk_${id}.json; \
     touch work/results/.done_${id}"
done

tmux select-layout -t proofread tiled
tmux attach -t proofread
```

完了検知: `.done_{id}` ファイルの存在をポーリング。

### エラーハンドリング

- **タイムアウト**: チャンクあたり最大5分（`--timeout`）。超過時はリトライキューに入れる。
- **レート制限**: 429エラー時は指数バックオフ（初期2秒、最大60秒、最大3回リトライ）。
- **パースエラー**: JSONパース失敗時は生のstdoutをログに保存し、スキップ。
- **部分失敗**: 一部チャンクが失敗しても、成功したチャンクのマージは実行。失敗チャンクは元のテキストをそのまま使用し、diffレポートに記録。

### リジューム機能

`work/results/` に既に結果が存在するチャンクはスキップする。
`--force` で全チャンクを再実行。

---

## Phase 4: マージ + レビュー

### マージ処理

1. `chunk_manifest.json` の順序に従って結果を連結
2. 各チャンクからオーバーラップ部分（`<!-- OVERLAP_START -->` ～ `<!-- OVERLAP_END -->`）を除去
3. チャンクメタデータコメント（`<!-- CHUNK_META ... -->`）を除去
4. 結果を `output/proofread.md` に書き出し

### diffレポート生成

`output/diff_report.md` — 修正箇所の一覧。人間のレビュー用。

```markdown
# 校正 Diff レポート

生成日時: 2026-03-28T15:30:00+09:00
入力ファイル: input.md
総修正数: 42 (確定: 35, 要確認: 7)

## 確定修正 (FIXED)

| #   | セクション | 原文            | 修正後         | 理由        |
| --- | ---------- | --------------- | -------------- | ----------- |
| 1   | §1.1       | `homornorphism` | `homomorphism` | OCR: rn → m |
| 2   | §2.3       | `Thearem 2.1`   | `Theorem 2.1`  | OCR: a → o  |
| ... |            |                 |                |             |

## 要確認 (UNCERTAIN)

| #   | セクション | 原文          | 修正案          | 理由               |
| --- | ---------- | ------------- | --------------- | ------------------ |
| 1   | §4.2       | `G-invariant` | `$G$-invariant` | LaTeX記法の正規化? |
| ... |            |               |                 |                    |
```

### 統計レポート

`output/stats.json` — パイプライン全体の実行統計。

```json
{
  "source": "input.md",
  "timestamp": "2026-03-28T15:30:00+09:00",
  "model": "gemini-3-flash-preview",
  "phases": {
    "context_extraction": {
      "duration_sec": 45,
      "tokens": { "input": 120000, "output": 3500 }
    },
    "chunking": {
      "total_chunks": 24,
      "avg_chunk_tokens": 18500
    },
    "proofreading": {
      "succeeded": 23,
      "failed": 1,
      "total_duration_sec": 180,
      "total_tokens": { "input": 680000, "output": 450000 },
      "per_chunk": [...]
    },
    "merge": {
      "total_fixes": 35,
      "total_uncertain": 7
    }
  }
}
```

---

## 最終出力の文書構造

```markdown
---
title: "Abstract Algebra"
author: "Dummit & Foote"
source_format: "PDF (OCR → Markdown)"
ocr_engine: "mistral-ocr"
proofread_model: "gemini-3-flash-preview"
proofread_date: "2026-03-28"
pipeline_version: "1.0.0"
total_fixes: 35
uncertain_fixes: 7
---

<!-- DOCUMENT_INDEX
notation_table:
  - symbol: "$G$"
    meaning: "group"
    scope: "Ch.1-5"
  - symbol: "$\\varphi$"
    meaning: "homomorphism"
    scope: "global"

structure_outline:
  - chapter: 1
    title: "Introduction to Groups"
    sections:
      - number: "1.1"
        title: "Basic Axioms"
        theorems: ["Definition 1.1.1", "Definition 1.1.2", "Proposition 1.1.3"]

terminology_whitelist:
  - "G-set"
  - "left coset space"
  - "fiber product"
END_DOCUMENT_INDEX -->

# Chapter 1: Introduction to Groups

## §1.1 Basic Axioms

（本文）
```

### 構造の設計意図

- **YAMLフロントマター**: Obsidianプロパティとして認識。検索・フィルタリングに使用。
- **XMLインデックス（HTMLコメント）**: LLMが将来この文書を再処理する際のコンテキスト。Obsidianのレンダリングに影響しない。`grep` で即座に参照可能。
- **本文**: 校正済みMarkdown。`<!-- FIXED: ... -->` アノテーションは残す（レビュー完了後に一括除去するスクリプトを別途用意）。

---

## CLI インターフェース

```
proofread-ocr — LLMベースOCR校正パイプライン

Usage:
  proofread-ocr <input.md> [options]
  proofread-ocr <directory/> [options]       # ディレクトリ内の全.mdを処理

Phases:
  proofread-ocr <input.md>                   # Phase 1-4 を順次実行
  proofread-ocr <input.md> --phase context   # Phase 1 のみ（コンテキスト抽出）
  proofread-ocr <input.md> --phase chunk     # Phase 2 のみ（チャンク分割）
  proofread-ocr <input.md> --phase proofread # Phase 3 のみ（並列校正）
  proofread-ocr <input.md> --phase merge     # Phase 4 のみ（マージ）

Options:
  -o, --output <path>           出力先ファイルパス（デフォルト: input_proofread.md）
  -w, --workdir <path>          作業ディレクトリ（デフォルト: .proofread/）
  -m, --model <model>           Geminiモデル（デフォルト: gemini-3-flash-preview）
  --chunk-size <tokens>         チャンクサイズ上限（デフォルト: 20000）
  --overlap-lines <n>           オーバーラップ行数（デフォルト: 5）
  --concurrency <n>             並列度（デフォルト: 4）
  --timeout <seconds>           チャンクあたりのタイムアウト（デフォルト: 300）
  --skip-context-review         Phase 1 後の人間レビューをスキップ
  --debug                       tmuxモードで実行（各ペインの出力を視覚的に監視）
  --force                       既存の結果を無視して全チャンク再実行
  --dry-run                     実行せず、チャンク分割結果とコマンド一覧を表示
  --verbose                     詳細ログ出力
  --strip-annotations           出力から FIXED/UNCERTAIN アノテーションを除去

Context Options:
  --context <path>              既存のcontext.mdを指定（Phase 1をスキップ）
  --preset <name>               書籍プリセット（cleanup_ocr.pyと共通）

Prompt Options:
  --prompt <path>               カスタム校正プロンプトを指定
  --thinking-level <level>      Gemini thinking level: minimal|low|medium|high（デフォルト: high）
```

### 実行例

```bash
# 基本的な使い方
proofread-ocr algebra_textbook.md

# 既存のcontext.mdを流用して校正のみ再実行
proofread-ocr algebra_textbook.md --context context.md --phase proofread --force

# チャンク分割の確認（dry-run）
proofread-ocr algebra_textbook.md --dry-run --verbose

# デバッグモード（tmuxで各ペインを監視）
proofread-ocr algebra_textbook.md --debug --concurrency 6

# アノテーション除去済みのクリーンな出力
proofread-ocr algebra_textbook.md --strip-annotations

# ディレクトリ内の全ファイルを処理
proofread-ocr ocr_output/ -o proofread_output/
```

---

## ファイル構成

```
proofread-ocr/
├── pyproject.toml
├── CLAUDE.md
├── prompts/
│   ├── extract_context.md      # Phase 1: コンテキスト抽出プロンプト
│   └── proofread.md            # Phase 3: 校正プロンプト
├── src/
│   └── proofread_ocr/
│       ├── __init__.py
│       ├── cli.py              # CLIエントリポイント
│       ├── context.py          # Phase 1: コンテキスト抽出
│       ├── chunker.py          # Phase 2: チャンク分割
│       ├── proofreader.py      # Phase 3: 並列校正（subprocess / tmux）
│       ├── merger.py           # Phase 4: マージ + diff生成
│       ├── gemini.py           # Gemini CLI ラッパー
│       └── models.py           # データモデル（Chunk, Result, etc.）
├── tests/
│   ├── test_chunker.py
│   ├── test_merger.py
│   └── fixtures/
│       ├── sample_input.md
│       └── sample_context.md
└── evals/
    └── evals.json              # スキル評価用テストケース
```

---

## 制約事項・既知の問題

- **Gemini CLI stdout/stderr 分離問題**: issue #12267（P1）。`--output-format json` + `jq` によるレスポンス抽出で回避。
- **`@file` の非インタラクティブモード対応**: issue #3311。`@file` が非インタラクティブモードで動作しない場合、`cat` によるstdinパイプにフォールバックする。
- **thinking_level の CLI 指定方法**: Gemini CLI から直接 `thinking_level` を指定する方法が限定的。`GEMINI.md` または `.gemini/settings.json` 経由での設定をフォールバックとする。
- **チャンクサイズとトークン数の推定**: 正確なトークンカウントにはtiktokenなどのトークナイザが必要。初期実装では文字数ベースの近似（1トークン ≈ 3文字（日本語）/ 4文字（英語））で対応し、精度が問題になれば後から改善する。

---

## 将来の拡張

- **書籍プリセットシステム**: `cleanup_ocr.py` のプリセットと統合し、書籍ごとの校正パターン（running header, 記号用法等）を一括設定。
- **差分適用モード**: 全文出力ではなく、diff形式での校正出力に対応。トークン効率の改善。
- **校正品質の自動評価**: 校正前後のテキストをさらに別モデル（Claude等）で評価し、過修正・見落としを検出。
- **Obsidian統合**: 校正済みファイルの自動配置、Spaced Repetition用の誤りパターンカード生成。
- **Claude Code スキル化**: `proofread-ocr` をClaude Codeスキルとしてラップし、SKILL.mdからトリガー可能にする。
