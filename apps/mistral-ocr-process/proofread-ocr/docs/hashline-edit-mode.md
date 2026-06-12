# Hashline Edit Mode

## 概要

`--edit-mode hashline` は、OCR 校正の Phase 3 で LLM に「校正済みチャンク全文」を出させる代わりに、Hashline patch を出させる実験的な編集方式です。

目的は、全文 rewrite による不要な改変や構造崩れを減らし、修正箇所だけを検証可能な patch として適用することです。既存の `rewrite` mode はデフォルトのまま残しており、Hashline mode は明示的に指定した場合だけ使われます。

```bash
uv run proofread-ocr input.md --edit-mode hashline
```

## 取り込んだ範囲

取り込んだのは full `oh-my-pi` agent ではなく、`@oh-my-pi/hashline` の patch applier だけです。

- Python 側は既存の chunking、context、agy 呼び出し、cache、merge、diff report を維持する。
- TypeScript sidecar は Hashline の `describe` と `apply` だけを担当する。
- LLM は numbered chunk と `[PATH#TAG]` を見て Hashline patch を返す。
- patch 適用に成功した場合だけ、既存の `ProofreadResult.output_text` に校正済み本文を保存する。

この切り分けにより、`oh-my-pi` の LSP、DAP、browser、subagent などの大きい実行面は校正パイプラインに持ち込まない設計にしています。

## 追加ファイル

| ファイル | 役割 |
| --- | --- |
| `package.json` / `bun.lock` | Bun sidecar 用の `@oh-my-pi/hashline` 依存定義 |
| `scripts/apply_hashline.ts` | stdin JSON を受け取り、Hashline target の生成または patch 適用を行う |
| `src/proofread_ocr/hashline.py` | Python から sidecar を呼ぶ wrapper |
| `prompts/proofread_hashline.md` | LLM に Hashline patch だけを出させる Phase 3 prompt |
| `tests/test_hashline.py` | LLM 応答から Hashline patch を抽出する処理の単体テスト |

既存ファイルでは、`PipelineConfig` と `ProofreadResult` に `edit_mode`/`patch_text` を追加し、`proofreader.py` が `hashline` mode のときだけ sidecar を経由します。

## 実行フロー

通常の `rewrite` mode:

```text
prompt + context + chunk
  -> agy
  -> corrected chunk text
  -> results/chunk_NNN.json
```

Hashline mode:

```text
chunk text
  -> scripts/apply_hashline.ts describe
  -> [chunk_NNN.md#TAG] + numbered lines
  -> prompt + context + numbered target
  -> agy
  -> Hashline patch
  -> scripts/apply_hashline.ts apply
  -> corrected chunk text
  -> results/chunk_NNN.json
```

`results/hashline_targets/chunk_NNN.hashline.md` には、LLM に渡した numbered target が保存されます。patch 適用に失敗した場合は chunk result が failure になり、merge では従来通り元 chunk に fallback します。

## Hashline patch の期待形式

LLM 出力は次のような形式です。

```hashline
[chunk_001.md#A1B2]
replace 12..12:
+homomorphism <!-- FIXED: homornorphism -> homomorphism | OCR: rn -> m -->
```

校正不要の場合は、ヘッダのみを許容します。

```hashline
[chunk_001.md#A1B2]
```

重要な制約:

- `[PATH#TAG]` は sidecar が生成したものをそのまま使う。
- line number は numbered target の元行番号を使う。
- body row は `+` で始める。
- `-` row や unified diff は使わない。
- 変更しない行は patch に含めない。
- 修正箇所には従来通り `FIXED` / `UNCERTAIN` コメントを付ける。

## 依存関係

Hashline mode を使う場合だけ Bun と npm package が必要です。

```bash
cd apps/mistral-ocr-process/proofread-ocr
bun install
```

`node_modules/` は追跡対象外です。`bun.lock` は再現性のために追跡対象にします。

## 失敗時の扱い

Hashline mode では、次のケースを failure として扱います。

- Bun が見つからない。
- `scripts/apply_hashline.ts` が見つからない。
- LLM 応答に `[PATH#TAG]` ヘッダがない。
- patch parse に失敗する。
- tag mismatch などで `@oh-my-pi/hashline` が patch を拒否する。
- sidecar が timeout する。

failure result には、可能な範囲で `patch_text` と `error` を保存します。Phase 4 の merge は既存仕様通り、失敗 chunk について元 chunk を使います。

## 現時点の制限

- `--debug` tmux mode とは併用不可です。
- `replace block` など tree-sitter block 解決が必要な操作は prompt で使わせていません。
- sidecar は in-memory FS だけを使い、実ファイルを直接書き換えません。
- Hashline mode は実験機能です。品質比較が済むまでは `rewrite` をデフォルトのまま維持します。

## 検証済み事項

実装時点で確認した内容:

- `uv run pytest` が成功する。
- `scripts/apply_hashline.ts describe` が `[PATH#TAG]` と numbered lines を返す。
- `scripts/apply_hashline.ts apply` が Hashline patch を適用し、修正済み text を返す。
- Python wrapper から sidecar 経由で `describe` / `apply` を呼べる。
- `--phase chunk --edit-mode hashline --dry-run` が Hashline prompt を選ぶ。

## 評価方針

本格投入前に、同じ入力で次を比較します。

- `rewrite`: 既存の全文校正方式。
- `hashline`: Hashline patch 方式。

見るべき指標:

- patch 適用成功率。
- 修正漏れ。
- 過剰修正。
- Markdown 構造の保持。
- LaTeX delimiter / environment の破損率。
- `FIXED` / `UNCERTAIN` annotation の品質。
- 再実行時の安定性。

Hashline mode の価値は、単純な出力 token 削減よりも、編集対象を狭くして構造崩れを減らせるかどうかで判断します。
