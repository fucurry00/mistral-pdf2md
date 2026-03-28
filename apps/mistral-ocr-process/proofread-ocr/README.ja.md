# proofread-ocr

Gemini CLI を利用した、OCR 変換済み Markdown の LLM ベース校正パイプライン。

ルールベースのクリーンアップスクリプトでは対応不可能な、文脈依存の OCR エラー（文字の取り違え、LaTeX 記法の崩れ、相互参照の番号ずれ等）を検出・修正します。

[English README](README.md)

## 前提条件

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) v0.21.1+（Gemini 3 Flash アクセス可能）
- macOS (Apple Silicon) — 動作確認環境

## インストール

```bash
cd proofread-ocr
uv sync
```

## クイックスタート

```bash
# 全4フェーズを順次実行
uv run proofread-ocr input.md

# ドライラン — Gemini を呼ばずにチャンク分割結果をプレビュー
uv run proofread-ocr input.md --dry-run --verbose
```

## パイプライン全体像

```
input.md ──> Phase 1 ──> Phase 2 ──> Phase 3 ──> Phase 4 ──> output.md
             コンテキスト   チャンク     並列校正     マージ
             抽出           分割                      + レビュー
```

### Phase 1: コンテキスト抽出

文書全体を読み、後続の校正で各チャンクに共有する情報を抽出します。

- **記号テーブル（Notation Table）** — 記号とその意味の対応表
- **構造アウトライン（Structure Outline）** — 章・節・定理の番号付きリスト
- **用語ホワイトリスト（Terminology Whitelist）** — 校正で「誤字」として修正してはいけない専門用語

抽出後、人間によるレビューのために一時停止します（`--skip-context-review` でスキップ可能）。

### Phase 2: チャンク分割

`##` / `###` の見出し境界で文書を分割し、各チャンクを約 20,000 トークンに収めます。隣接チャンク間に 5 行のオーバーラップを設け、`<!-- OVERLAP_START/END -->` マーカーで明示します。

### Phase 3: 並列校正

各チャンクを Gemini CLI に並列送信します（`cat prompt context chunk | gemini -p ...`）。すべての修正にアノテーションが付きます。

```markdown
homomorphism <!-- FIXED: homornorphism -> homomorphism | OCR: rn -> m -->
```

リジューム対応 — 完了済みチャンクは再実行時にスキップされます。

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
| `-m, --model <model>` | `gemini-3-flash-preview` | Gemini モデル |
| `--chunk-size <tokens>` | `20000` | チャンクあたりの最大トークン数 |
| `--overlap-lines <n>` | `5` | チャンク間のオーバーラップ行数 |
| `--concurrency <n>` | `4` | Gemini の並列呼び出し数 |
| `--timeout <seconds>` | `300` | チャンクあたりのタイムアウト |
| `--skip-context-review` | — | Phase 1 後の人間レビューをスキップ |
| `--context <path>` | — | 既存の context.md を指定（Phase 1 をスキップ） |
| `--debug` | — | tmux モード（各ペインを視覚的に監視） |
| `--force` | — | キャッシュ済み結果を無視して全チャンク再実行 |
| `--dry-run` | — | チャンク分割結果とコマンド一覧の表示のみ |
| `--strip-annotations` | — | 出力から FIXED/UNCERTAIN コメントを除去 |
| `--verbose` | — | 詳細な進捗ログ |
| `--prompt <path>` | — | カスタム校正プロンプト |

### 実行例

```bash
# 既存のコンテキストを流用し、全チャンクを再校正
proofread-ocr input.md --context context.md --phase proofread --force

# tmux デバッグモード
proofread-ocr input.md --debug --concurrency 6

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
│   └── proofread.md            # Phase 3 プロンプト
├── src/proofread_ocr/
│   ├── cli.py                  # CLI エントリポイント
│   ├── context.py              # Phase 1: コンテキスト抽出
│   ├── chunker.py              # Phase 2: チャンク分割
│   ├── proofreader.py          # Phase 3: 並列校正
│   ├── merger.py               # Phase 4: マージ + レポート生成
│   ├── gemini.py               # Gemini CLI 非同期ラッパー
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
- **外部依存ゼロ** — 標準ライブラリのみ（Gemini CLI 本体を除く）
