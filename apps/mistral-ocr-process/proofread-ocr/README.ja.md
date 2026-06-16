# proofread-ocr

completion API（Anthropic または Google Gemini）を利用した、OCR 変換済み Markdown の LLM ベース校正パイプライン。

ルールベースのクリーンアップスクリプトでは対応不可能な、文脈依存の OCR エラー（文字の取り違え、LaTeX 記法の崩れ、相互参照の番号ずれ等）を検出・修正します。

[English README](README.md)

## 前提条件

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- 選択したプロバイダの API キー:
  - Gemini モデル用 `GEMINI_API_KEY`（デフォルト: `gemini-3.1-flash-lite-preview`）
  - Claude モデル用 `ANTHROPIC_API_KEY`（例: `claude-haiku-4-5-20251001`）
- `--edit-mode hashline` を使う場合は [Bun](https://bun.sh/) 1.3.14+
- macOS (Apple Silicon) — 動作確認環境

## インストール

```bash
cd proofread-ocr
uv sync
bun install  # --edit-mode hashline を使う場合のみ必要
```

## クイックスタート

```bash
# 全4フェーズを順次実行
uv run proofread-ocr input.md

# ドライラン — LLM を呼ばずにチャンク分割結果をプレビュー
uv run proofread-ocr input.md --dry-run --verbose
```

## パイプライン全体像

```
input.md ──> Phase 1 ──> Phase 2 ──> Phase 3 ──> Phase 4 ──> output.md
             コンテキスト   チャンク     並列校正     マージ
             抽出           分割                      + レビュー
```

## LLM バックエンド

公式プロバイダ SDK を通じて completion API を直接呼びます。プロバイダは
`src/proofread_ocr/llm.py` の `run_llm()` 境界で `--model` 名から判定します。

- `gemini` を含む名前 → Google GenAI SDK（`GEMINI_API_KEY`）
- `claude`/`haiku`/`sonnet`/`opus` を含む名前 → Anthropic SDK（`ANTHROPIC_API_KEY`）

`run_llm()` は `prompt + context + chunk` を受け取り、校正済み Markdown（hashline
モードでは Hashline パッチ）を返します。プロバイダの切替・追加はこの一箇所の変更で
済み、コード全体のリネームは不要です。これは従来の Antigravity CLI (`agy`)
subprocess バックエンドを置き換えたものです。

### Phase 1: コンテキスト抽出

文書全体を読み、後続の校正で各チャンクに共有する情報を抽出します。

- **記号テーブル（Notation Table）** — 記号とその意味の対応表
- **構造アウトライン（Structure Outline）** — 章・節・定理の番号付きリスト
- **用語ホワイトリスト（Terminology Whitelist）** — 校正で「誤字」として修正してはいけない専門用語

抽出後、人間によるレビューのために一時停止します（`--skip-context-review` でスキップ可能）。

### Phase 2: チャンク分割

`##` / `###` の見出し境界で文書を分割し、各チャンクを約 20,000 トークンに収めます。隣接チャンク間に 5 行のオーバーラップを設け、`<!-- OVERLAP_START/END -->` マーカーで明示します。

### Phase 3: 並列校正

各チャンクを completion API へ並列送信します（`prompt + context + chunk` を `run_llm()` 経由で）。すべての修正にアノテーションが付きます。

```markdown
homomorphism <!-- FIXED: homornorphism -> homomorphism | OCR: rn -> m -->
```

リジューム対応 — 完了済みチャンクは再実行時にスキップされます。

実験的な安全寄りの編集方式として Hashline mode も利用できます。

```bash
uv run proofread-ocr input.md --edit-mode hashline
```

このモードでは、モデルは校正済みチャンク全文ではなく Hashline patch を返します。
TypeScript sidecar が `@oh-my-pi/hashline` で元チャンクの snapshot に対して
patch を適用し、成功した場合だけ校正済みテキストとして保存します。
設計意図、失敗時の扱い、検証内容は
[docs/hashline-edit-mode.md](docs/hashline-edit-mode.md) にまとめています。

### Phase 4: マージ + レビュー

チャンクを再結合（オーバーラップ/メタデータマーカーを除去）し、以下を生成します。

- `proofread.md` — YAML フロントマター付き校正済み文書
- `diff_report.md` — 全 FIXED / UNCERTAIN 修正の一覧表
- `stats.json` — 実行統計（所要時間、トークン使用量、成功/失敗数）

## 使い方

```
proofread-ocr <input.md> [options]
proofread-ocr <directory/> [options]     # ディレクトリ内の全 .md を処理
```

### フェーズ指定

```bash
proofread-ocr input.md --phase context    # Phase 1 のみ
proofread-ocr input.md --phase chunk      # Phase 2 のみ
proofread-ocr input.md --phase proofread  # Phase 3 のみ
proofread-ocr input.md --phase merge      # Phase 4 のみ
```

### 主要オプション

| オプション | デフォルト | 説明 |
| --- | --- | --- |
| `-o, --output <path>` | `{input}_proofread.md` | 出力先ファイルパス |
| `-w, --workdir <path>` | `.proofread/` | 中間ファイル用作業ディレクトリ |
| `-m, --model <model>` | `gemini-3.1-flash-lite-preview` | モデル名（プロバイダは名前から判定） |
| `--chunk-size <tokens>` | `20000` | チャンクあたりの最大トークン数 |
| `--overlap-lines <n>` | `5` | チャンク間のオーバーラップ行数 |
| `--concurrency <n>` | `10` | LLM の並列リクエスト数 |
| `--timeout <seconds>` | `300` | チャンクあたりのタイムアウト |
| `--skip-context-review` | — | Phase 1 後の人間レビューをスキップ |
| `--context <path>` | — | 既存の context.md を指定（Phase 1 をスキップ） |
| `--force` | — | キャッシュ済み結果を無視して全チャンク再実行 |
| `--dry-run` | — | チャンク分割結果と実行予定の呼び出しの表示のみ |
| `--strip-annotations` | — | 出力から FIXED/UNCERTAIN コメントを除去 |
| `--verbose` | — | 詳細な進捗ログ |
| `--prompt <path>` | — | カスタム校正プロンプト |
| `--edit-mode <mode>` | `rewrite` | `rewrite` または実験的な `hashline` patch mode |

### 実行例

```bash
# 既存のコンテキストを流用し、全チャンクを再校正
proofread-ocr input.md --context context.md --phase proofread --force

# デフォルトの Gemini ではなく Claude で校正
proofread-ocr input.md --model claude-haiku-4-5-20251001 --concurrency 6

# アノテーションなしのクリーンな出力
proofread-ocr input.md --strip-annotations

# ディレクトリ内の全ファイルをバッチ処理
proofread-ocr ocr_output/ -o proofread_output/
```

## プロジェクト構成

```
proofread-ocr/
├── pyproject.toml
├── prompts/
│   ├── extract_context.md      # Phase 1 プロンプト
│   ├── proofread.md            # Phase 3 rewrite プロンプト
│   └── proofread_hashline.md   # Phase 3 Hashline patch プロンプト
├── scripts/
│   └── apply_hashline.ts       # @oh-my-pi/hashline 用 Bun sidecar
├── src/proofread_ocr/
│   ├── cli.py                  # CLI エントリポイント
│   ├── context.py              # Phase 1: コンテキスト抽出
│   ├── chunker.py              # Phase 2: チャンク分割
│   ├── proofreader.py          # Phase 3: 並列校正
│   ├── merger.py               # Phase 4: マージ + レポート生成
│   ├── llm.py                  # completion API 非同期ラッパー（Anthropic/Gemini）
│   ├── llm_cli.py              # stdin→completion→stdout CLI（proofread-llm）
│   ├── hashline.py             # Hashline sidecar の Python ラッパー
│   └── models.py               # データモデル（dataclass）
├── tests/
│   ├── test_chunker.py
│   ├── test_merger.py
│   └── fixtures/
└── evals/
    └── evals.json
```

## テスト実行

```bash
uv run pytest tests/ -v
```

## 設計原則

- **忠実性最優先** — 原文の意味を変更しない。校正であり、編集・リライトではない
- **透明性** — すべての修正にアノテーション（原文・修正後・理由）を付与
- **冪等性** — 再実行可能。中断からの再開をサポート
- **最小依存** — 標準ライブラリ + 公式プロバイダ SDK（`anthropic`, `google-genai`）
