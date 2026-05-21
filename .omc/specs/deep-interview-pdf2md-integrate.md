# Deep Interview Spec: PDF→Markdown パイプライン統合

## Metadata
- Interview ID: di-pdf2md-integrate-001
- Rounds: 9
- Final Ambiguity Score: 17.6%
- Type: brownfield
- Generated: 2026-05-21
- Threshold: 20%
- Initial Context Summarized: no
- Status: PASSED

---

## Clarity Breakdown

| Dimension | Score (avg) | Weight | Weighted |
|-----------|-------------|--------|---------|
| Goal Clarity | 0.83 | 0.35 | 0.290 |
| Constraint Clarity | 0.815 | 0.25 | 0.204 |
| Success Criteria | 0.845 | 0.25 | 0.211 |
| Context Clarity | 0.795 | 0.15 | 0.119 |
| **Total Clarity** | | | **0.824** |
| **Ambiguity** | | | **17.6%** |

---

## Topology

| Component | Status | Description | Coverage |
|-----------|--------|-------------|----------|
| 統合パイプライン本体 | active | OCR → cleanup → Gemini清書 を繋ぐ単一オーケストレーター | `pipeline.py` の Step 3 を `proofread-ocr` subprocess 呼び出しに置き換え |
| インターフェース層 | active | 統合後のパイプラインを CLI / MCP から呼び出せるようにする | `pipeline.py` + `mcp_server.py` の両方を更新。skill は今回スコープ外 |

---

## Goal

`pipeline.py` の Step 3 (`analyze`) を廃止し、`proofread-ocr` パッケージ（4フェーズ Gemini 清書パイプライン）への subprocess 呼び出しに置き換えることで、**PDF → Mistral OCR → ルールベース cleanup → Gemini 清書 → `{stem}.md`** という一貫したパイプラインを実現する。`mcp_server.py` の `proofread=True` パスも同様に `proofread-ocr` を使うよう更新する。

---

## Constraints

- **3ステップ固定**: OCR → cleanup → proofread の順。cleanup は必ず残す（Geminiへの入力ノイズ削減）
- **`proofread-ocr` 呼び出し方法**: subprocess（`cleanup_ocr.py` と同じパターン）
- **渡すオプション**: `--preset` のみ。`proofread-ocr` の細かいオプション（`--phase`, `--concurrency` 等）は pipeline 経由では制御しない
- **`--skip-context-review` は常に有効**: バッチ処理で人間レビューの割り込みを回避する
- **出力ファイル**: `{stem}.md` が最終版（proofread 結果で上書き）。`{stem}.md.bak` にはcleanup済みバックアップが残る
- **レポートファイル**: `diff_report.md`, `stats.json` は副産物として生成されるが、デフォルトの stdout 表示には含めない（デバッグ用）
- **インターフェース更新範囲**: `pipeline.py` と `mcp_server.py` のみ。`apps/skill/` は今回対象外

---

## Non-Goals

- `proofread-ocr` 内部（`context.py`, `chunker.py`, `proofreader.py`, `merger.py`）の変更
- `--phase` / `--concurrency` / `--chunk-size` 等のオプションを `pipeline.py` に露出させること
- `apps/skill/` の更新
- 旧 `analyze` ステップとの後方互換性維持（`--steps analyze` は廃止）

---

## Acceptance Criteria

- [ ] `python pipeline.py book.pdf` を実行すると `book/book.md`（清書済み）と `book/images/` が生成される
- [ ] `--steps` のデフォルト値が `ocr,cleanup,proofread` になっている（旧: `ocr,cleanup,analyze`）
- [ ] `--steps analyze` を指定するとエラーまたは警告になる（または無視される）
- [ ] `--preset dummit-foote` を指定すると `proofread-ocr` に `--preset dummit-foote` が渡される
- [ ] `python pipeline.py book.pdf --steps ocr,cleanup` は proofread をスキップして従来通り動く
- [ ] MCP の `convert_pdf(proofread=True)` が `proofread-ocr` subprocess を呼び出す
- [ ] MCP の戻り値に `proofread_path` が含まれる（= `{stem}.md` のパス）
- [ ] バッチモード（ディレクトリ入力）でも全PDFに対して proofread が走る

---

## Assumptions Exposed & Resolved

| Assumption | Challenge | Resolution |
|------------|-----------|------------|
| 既存 `analyze` step を残す | `proofread` と `analyze` は役割が違う、両立すべきでは | `analyze` を廃止、`proofread` に完全置き換え |
| proofread-ocr の全オプションを expose する | 最小限のコントロールで十分では？ | `--preset` のみ渡す。他オプションは不要 |
| 出力を `{stem}_proofread.md` にする | pipeline.py の既存命名と不整合 | `{stem}.md` を最終版として上書き |
| proofread-ocr を import で呼ぶ | subprocess のほうが cleanup と一貫性がある | subprocess（`uv run proofread-ocr ...`）を採用 |

---

## Technical Context

### 現在の pipeline.py Step 3 (analyze) — 廃止対象

```python
def run_analyze(md_path: Path, analysis_path: Path, timeout: int = 300):
    content = md_path.read_text(encoding="utf-8")
    prompt = _GEMINI_ANALYZE_PROMPT + "\n\n---\n\n" + content
    result = subprocess.run(
        ["gemini", "--yolo", "-p", prompt],
        capture_output=True, text=True, timeout=timeout,
    )
    analysis_path.write_text(result.stdout, encoding="utf-8")
```

### 新 Step 3 (proofread) — 実装イメージ

```python
def run_proofread(md_path: Path, preset: str | None, timeout: int = 600):
    cmd = [
        "uv", "run", "proofread-ocr",
        str(md_path),
        "-o", str(md_path),          # {stem}.md に上書き
        "-w", str(md_path.parent / ".proofread"),
        "--skip-context-review",
    ]
    if preset:
        cmd += ["--preset", preset]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError(f"proofread-ocr failed: {result.stderr.strip()}")
    if result.stdout.strip():
        print(result.stdout.rstrip())
```

### pipeline.py の --steps 変更点

```python
# Before
DEFAULT_STEPS = ["ocr", "cleanup", "analyze"]
ALL_STEPS     = ["ocr", "cleanup", "analyze"]

# After
DEFAULT_STEPS = ["ocr", "cleanup", "proofread"]
ALL_STEPS     = ["ocr", "cleanup", "proofread"]
```

### mcp_server.py の proofread パス変更点

```python
# Before (proofread=True 時)
result = subprocess.run(["gemini", "--yolo", "-p", prompt], ...)

# After
cmd = ["uv", "run", "proofread-ocr", md_path, "-o", md_path, "--skip-context-review"]
if preset:
    cmd += ["--preset", preset]
subprocess.run(cmd, ...)
```

### 変更対象ファイル一覧

| ファイル | 変更内容 |
|---------|---------|
| `apps/mistral-ocr-process/pipeline.py` | `run_analyze()` を `run_proofread()` に置き換え。`DEFAULT_STEPS`/`ALL_STEPS` 更新 |
| `apps/mcp-server/mcp_server.py` | `proofread=True` パスを `proofread-ocr` subprocess に変更 |

---

## Ontology (Key Entities)

| Entity | Type | Fields | Relationships |
|--------|------|--------|---------------|
| PDF | input | path, pages | 入力として pipeline が受け取る |
| Markdown | output | path, content | OCR, cleanup, proofread が順に変換 |
| pipeline.py | orchestrator | steps, preset, chunk_size | OCR/cleanup/proofread を順番に呼ぶ |
| convert_pdf_to_markdown | ocr-engine | pdf_path, output_path, chunk_size | Mistral OCR API を叩く |
| cleanup_ocr | cleanup-engine | mode, preset, header_patterns | ルールベースでアーティファクト除去 |
| proofread-ocr | proofread-engine | phase, model, preset, workdir | 4フェーズ Gemini 清書パイプライン |
| mcp_server | interface | convert_pdf tool | pipeline を MCP ツールとして公開 |

---

## Interview Transcript

<details>
<summary>Full Q&A (9 rounds)</summary>

### Round 0 (Topology)
**Q:** 以下2つのコンポーネントとして捉えていますか？（統合パイプライン本体 / インターフェース層）
**A:** 合っている

### Round 1 (Goal Clarity — 統合パイプライン本体)
**Q:** 「統合」の具体的なアプローチ（pipeline.py に組み込む / 新スクリプト / proofread-ocr 主軸 / お任せ）
**A:** どれでもいい、最適な方法で
**Ambiguity:** 65.5%

### Round 2 (Constraint Clarity)
**Q:** cleanup ステップは残しますか？
**A:** 残す（OCR → cleanup → Gemini）
**Ambiguity:** 56.5%

### Round 3 (Success Criteria)
**Q:** 完成の定義：出力内容 vs ワンコマンド完結
**A:** レポートはデバッグ用という体でオプションとして置く
**Ambiguity:** 43.0%

### Round 4 (Goal Clarity — インターフェース層)
**Q:** 更新が必要なインターフェース（CLI / MCP / skill）
**A:** CLI, MCP server
**Ambiguity:** 51.0%

### Round 5 (Constraint Clarity — 両コンポーネント)
**Q:** 全フェーズ統合 vs シンプル vs コントロール付き全フェーズ
**A:** 全フェーズだがコントロールしたい
**Ambiguity:** 42.5%

### Round 6 (Success Criteria — Simplifier Mode)
**Q:** 最小限のコントロールは何か（プリセット / --model 等 / 全オプション / 別途呼び出し）
**A:** プリセットだけでいい
**Ambiguity:** 32.5%

### Round 7 (Success Criteria)
**Q:** `analyze` ステップの扱い（置き換え / 追加 / 残しつつ proofread がデフォルト）
**A:** proofread に置き換える
**Ambiguity:** 26.3%

### Round 8 (Success Criteria — インターフェース層)
**Q:** 最終出力ファイル名（{stem}.md 上書き / {stem}_proofread.md 並存 / お任せ）
**A:** {stem}.md が最終版（内部で上書き）
**Ambiguity:** 20.4%

### Round 9 (Constraints)
**Q:** proofread-ocr の呼び出し方法（subprocess / import / お任せ）
**A:** どちらでもいい
**Ambiguity:** 17.6% ✅

</details>
