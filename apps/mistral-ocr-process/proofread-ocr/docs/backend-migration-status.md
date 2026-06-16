# Backend Migration Status — agy → completion API

ステータス: **構造的に完成・`uv run pytest` 32 passed・ライブ未検証**（2026-06-16）

このドキュメントは引き継ぎ用。実 API を1回も叩いていない状態で止まっているので、
次の担当者は「ライブ検証」から再開する。

## 何をしたか

proofread-ocr の LLM バックエンドを Antigravity CLI (`agy`) subprocess から
**completion API 直叩き**（Anthropic / Google Gemini）へ全面移行した。

- 唯一の seam: `src/proofread_ocr/llm.py` の `run_llm()` → `LLMResponse`
  - プロバイダは `--model` 名から判定（`gemini*`→google-genai, `claude/haiku/sonnet/opus`→anthropic）
  - 旧 `gemini.py`（agy ラッパー）は削除
- リネームは「ツール名でなくロール」で実施: `gemini.py`→`llm.py`, `run_gemini`→`run_llm`,
  `GeminiResponse`→`LLMResponse`。デフォルト `gemini-3.1-flash-lite-preview`
- cleanup planner（`pipeline.py`、最後の agy 呼び出し）→ 新 console script
  `proofread-llm`（`src/proofread_ocr/llm_cli.py`, stdin→completion→stdout）を
  `uv run --project proofread-ocr proofread-llm` で再利用。親プロジェクトに SDK 依存を持たせない
- 削除: `--debug`/tmux mode, `launch_tmux_session`, Gemini-CLI 用 JSON 救済コード
- `.env` 読み込み: proofread-ocr は nested uv project で親の `.env` を自動継承しないため、
  `llm.py _ensure_env_loaded()` が親プロジェクト → standalone → cwd の順で `.env` を読む
  （既存の export 済み env は上書きしない）。機構は probe 検証済み
- 依存追加: `anthropic`, `google-genai`, `python-dotenv`（stdlib-only 方針は放棄）
- README×4 / SPEC / CLAUDE.md / hashline-edit-mode.md の agy 記述を更新

## 検証済み（オフラインのみ）

- import 疎通 / `_provider_for` ルーティング（gemini→Gemini, claude/haiku→Anthropic）
- `uv run pytest` → 32 passed
- `proofread-llm` console script 登録、`--help` 動作
- `pipeline.py` 構文 OK
- `.env` ローダー機構（probe 変数が `uv run --project` subprocess 内で None→値）

## 未検証（要ライブ実行）= 次の一歩

実 API キー（`GEMINI_API_KEY` 等を `.env` に。`.env.example` 参照）を入れて、
**1チャンクだけライブ実行**する。確認点:

- `resp.text` が実際に埋まるか
- hashline patch が parse / apply されるか（`--edit-mode hashline`）
- token 数が返るか
- 校正品質（過剰修正・LaTeX 破損の有無）

最小コマンド例（小さい入力で）:

```bash
cd apps/mistral-ocr-process/proofread-ocr
uv run proofread-ocr <small_input>.md --skip-context-review --phase proofread --force
# hashline を見るなら: --edit-mode hashline
```

## 既知の残課題（要判断）

1. **hashline がデフォルトで効かない**: `--edit-mode` は `rewrite` デフォルトで、
   `pipeline.py run_proofread` も `--edit-mode hashline` を渡していない。
   hashline の「出力削減」メリットは通常パイプラインでは未適用。
   → hashline をデフォルト化するか、`run_proofread` に渡すか要判断
2. **`max_tokens=32000`**（`run_llm` デフォルト）: flash-lite は問題ないが、
   `--model claude-haiku-*` で使う前に Anthropic 側の出力上限を確認
   （上限超過リクエストはエラーになる）
3. **selective-send は却下済み**: real_analysis 全文 ≈ 12.7k token と小さく、
   全文送信で十分という実測結論。校正漏れリスクを負う価値なしと判断

## 関連ファイル

- `src/proofread_ocr/llm.py` — completion API seam（`run_llm`, provider routing, dotenv loader）
- `src/proofread_ocr/llm_cli.py` — `proofread-llm` console script
- `src/proofread_ocr/proofreader.py` — Phase 3（rewrite / hashline 分岐）
- `src/proofread_ocr/hashline.py` + `scripts/apply_hashline.ts` — hashline sidecar（@oh-my-pi/hashline）
- `../pipeline.py` — cleanup planner が `proofread-llm` を呼ぶ
- `docs/hashline-edit-mode.md` — hashline モード設計
