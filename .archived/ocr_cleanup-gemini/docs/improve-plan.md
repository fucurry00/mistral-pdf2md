Model: claude-opus-4.6

---

User:

![./Ch2-Real_Analysis_Folland/main.md]

このファイルのようなpdfをocrしたものを読みやすい形に変えるというタスクについて考えよう。これをllmに任せるタスクとするとどのような前処理、中間処理、後処理が必要になるだろうか？

現在のアプローチは、2パス（辞書作成 → 個別処理）方式になっている。一度AIに全体をサッと読ませて「表記ルールや重 要な定義のリスト」を作らせ、それを各チャンクの処理時に渡す方式。

1. ステップ1:
   「この文書全体を読んで、表記ルール、全体像、重要な内容（頻出する数式記号、
   定義、定理）のリスト（Glossary）を作って」
1. ステップ2:
   チャンクごとの処理時、プロンプトに「このGlossaryを前提知識として使って整形して」と指
   示する。

---

Model:

まずファイルの中身を確認させてください。中身を確認しました。実解析の講義スライドPDFをOCRしたもので、典型的なOCRアーティファクトが見えますね。このケースを具体例にして議論しましょう。

---

まず、このファイルに見える**典型的な問題**を整理すると：

1. **スライドのヘッダー/フッター繰り返し** — 「Bara Kim 2026, Spring, Korea University」「Real Analysis」が全ページに出現
2. **目次＋プログレスドット繰り返し** — 「2.1 Measurable functions 000000000」のようなナビゲーション要素がスライドごとに出現
3. **スライド区切りの消失** — ページ境界が失われ、本文と繰り返し要素が混在
4. **数式のOCR品質** — このケースはかなり良好（LaTeX化済み）だが、一部にスペーシングの乱れあり

---

現在の2パスアプローチは筋が良いと思います。その上で、パイプライン全体を**前処理 → パス1 → 中間処理 → パス2 → 後処理**に分解して考えると：

**前処理（LLM不要・ルールベース）**

ここが実はかなり重要で、LLMに投げる前にノイズを減らせばトークンコストも品質も改善されます。

- **繰り返しパターンの除去**: 正規表現で「Bara Kim 2026, Spring...」のようなヘッダー/フッター行、「2.1 Measurable functions 0000...」のようなプログレスインジケーター行を一括除去できる。パターンが文書ごとに違うので、最初に数行サンプリングして頻出行を特定→除去、というアプローチが現実的
- **ページ境界マーカーの挿入**: 元PDFのページ番号情報があれば`<!-- page N -->`のようなマーカーを入れておく。後でLLMが「ここはページ境界のノイズ」と判断する材料になる
- **空行・連続空白の正規化**: OCR出力の無意味な空白を統一

**パス1: Glossary / スタイルガイド生成（現行アプローチ）**

ここの設計で考慮すべき点がいくつかあります：

- **Glossaryに何を含めるか**: 数式記号の表記規約（例: この文書では $\mathcal{M}$ がσ-algebraを指す、$\chi_E$ が指示関数）だけでなく、**文書の構造パターン**も抽出すべき。例えば「Definition → Proposition → Corollary → Remarkの順で展開」「Propositionには番号が振られている（2.1, 2.2...）」など
- **コンテキストウィンドウ問題**: この文書は1500行超。全体を一度に読ませるのが現実的かどうかはモデルに依存する。全体を投げられるなら一発、投げられないなら冒頭N%+末尾N%のサンプリングで代替
- **出力フォーマット**: Glossaryは構造化データ（JSON/YAML）にした方がパス2での参照が安定する

**中間処理（パス1→パス2の間）**

- **チャンキング戦略**: これが一番難しい。数学文書では「Theorem → Proof」が分離されると意味が壊れるので、単純なトークン数分割ではなくセマンティックな区切り（Definition/Theorem/Proof/Remark単位）で切るべき。前処理でページ境界を入れておけば、これがヒューリスティックに使える
- **チャンク間オーバーラップ**: 前のチャンクの末尾数行を次のチャンクの冒頭に含める。LLMが文脈をつなげるために必要
- **Glossaryのチャンク固有フィルタリング**: 全Glossaryが全チャンクに必要なわけではない。チャンクが2.5 Product measuresの話をしているなら、2.1の記号定義は含めるが2.4のConvergence特有の用語は省略できる、等。ただしこれはオプティマイズの話で、最初はGlossary全投入で十分

**パス2: チャンクごとの整形**

- **プロンプト設計**: 「Glossaryに従って整形して」だけでなく、具体的な指示が必要。例えば「重複するスライドナビゲーション行は削除」「Definition/Theorem/Propositionは見出しレベル3で統一」「数式ブロックは$$で囲む」等のフォーマットルール
- **忠実性制約**: 数学文書では「内容を追加・修正するな、整形のみしろ」という強い制約が重要。LLMは親切心で証明を補完しようとする
- **前チャンクの出力サマリー**: 連続性のために、前のチャンクの最後のセクションが何だったかを渡す

**後処理（LLM不要・ルールベース）**

- **チャンク結合 + 重複除去**: オーバーラップ部分の重複を検出・除去
- **相互参照・番号の整合性チェック**: Proposition 2.7の次がProposition 2.8になっているか等
- **LaTeX数式のバリデーション**: 括弧の対応、`\begin{}`/`\end{}`の対応チェック（これはルールベースでできる）
- **最終フォーマット変換**: Markdown → Obsidianノート、LaTeX、HTML等

---

議論を深めたいポイントはどのあたりですか？

---

User:
Q: どの部分を深掘りする？（該当するものをすべて選択）
A: 前処理の自動化（繰り返しパターン検出）, チャンキング戦略の詳細, パス1 Glossary生成のプロンプト設計, パス2 整形プロンプトの設計と忠実性制約

---

Model:

全部ですね。では各パートを具体的に掘り下げていきましょう。この文書の実データを使って議論します。

---

## 1. 前処理の自動化（繰り返しパターン検出）

この文書を見ると、ルールベースで除去できるノイズが大量にあります。戦略は「完全一致の除去」ではなく「ファジーな繰り返し検出」が必要です。

**具体的に除去すべきパターン群：**

まず**完全一致系**。「Bara Kim 2026, Spring, Korea University」と「Real Analysis」は全ページに出現するフッター/タイトルで、完全一致の行なので単純な文字列マッチで消せます。

次に**ファジー一致系**。目次＋プログレスドットの行がやっかいで、同じ行が微妙に違う形で出現しています：

```
2.1 Measurable functions 000000000    ← 9個
2.1 Measurable functions 00000000     ← 8個
2.1 Measurable functions 000000●000   ← ●混じり
2.1 Measurable functions              ← ドットなし
```

これは「セクション番号 + タイトル + (任意の0●の連続)?」というパターンで正規表現 `^2\.\d+\s+[A-Z].*[0●]+$` 的なもので捕捉できますが、問題は**本文中の正規のセクション見出し**（`# 2.1 Measurable functions`）と区別する必要があること。Markdownの`#`がついているかどうかが手がかりになります。

**自動検出アルゴリズムの設計：**

汎用的にやるなら、文書ごとにパターンが違うので、事前にルールをハードコードするのではなく「繰り返し行の自動検出」が必要です。アルゴリズムとしては：

1. 全行をトークン化して、出現回数が閾値（例: 文書の推定ページ数の50%以上）を超える行を候補にする
2. 候補行を正規化（末尾の数字・記号列を除去、空白を正規化）してからグルーピング
3. 連続して出現する候補行のブロック（例: 5行連続で全部候補）を「スライドナビゲーションブロック」と判定
4. ブロックごと除去

ポイントは「5行まとまって繰り返し出現する」というブロック単位の検出です。この文書では：

```
2.1 Measurable functions 000000000
2.2 Nonnegative functions 0000000
2.3 Complex functions 000000000
2.4 Mode of Convergence 0000
2.5 Product measures 000000000000
```

この5行セットが20回以上出現しています。個別行だと本文のセクション見出しと混同するリスクがありますが、「この5行が固まって出現する」なら確実にナビゲーション要素です。

**実装の判断ポイント：** この前処理をPythonスクリプトで書くか、それともLLMに「まずノイズ行を特定して」と頼むか。コスト的にはPythonスクリプトが圧倒的に安いし確実。ただし汎用性を考えると、最初の1回だけLLMに「この文書の繰り返しパターンを列挙して」と頼んで正規表現を生成させ、それを前処理スクリプトに渡す、というハイブリッドも面白い。

---

## 2. チャンキング戦略の詳細

数学文書のチャンキングは、一般的なRAGのチャンキングとは要件が根本的に違います。

**なぜ単純分割がダメか：**

この文書で `Theorem 2.10` を見ると、定理の記述がページをまたいでいます。さらに重要なのは、`Theorem 2.37 Fubini-Tonelli` の証明が `Theorem 2.36` の結果を使っており、`2.36` 自体が `2.35 Monotone class lemma` に依存している。つまり「論理的依存チェーン」があります。

**推奨するチャンキング戦略：**

まず**セマンティック単位の定義**として、数学文書における自然な単位は：

- Definition（単独で完結）
- Proposition / Theorem / Lemma + その Proof（必ずセットで1チャンク）
- Corollary + 親 Theorem への言及
- Remark（直前の定理/定義への補足）
- Exercise（独立性が高い）

次に**境界検出のヒューリスティック**。前処理でスライドナビゲーションブロックを除去した後、残るのは本文のみ。その中で：

```
# で始まる行 → セクション見出し（大区切り）
"Definition" / "Theorem" / "Proposition" / "Lemma" / "Corollary" / "Remark" / "Proof" / "Exercise"
で始まる行 → 意味単位の境界（小区切り）
```

これらをマーカーにして、**グルーピングルール**を適用します：

- `Theorem N` の直後に `Proof` が来たら → 同一チャンク
- `Corollary` は直前の `Theorem/Proposition` と同一チャンクにするか、単独チャンクにするかは文脈次第（トークン数で判断）
- `Remark` は直前の要素に付属

**チャンクサイズの管理：**

理想的には1チャンク = 1000〜3000トークン程度。ただし `Theorem + 長い Proof` が5000トークンを超える場合は、Proofを内部で分割する必要がある。その場合は Proof 内の論理ステップ（「(i)」「(ii)」「First,」「Next,」等）を境界にする。

**オーバーラップの設計：**

チャンク間オーバーラップは、単純な「末尾N行を次に含める」ではなく：

- 前チャンクの**最後のDefinition/Theorem/Propositionのステートメント**（証明ではなく）を、次チャンクの冒頭にコンテキストとして含める
- これにより、次チャンクのProofが参照する定理文が必ず含まれる

実装としては、各チャンクに `context_from_previous` というフィールドを持たせて、本文とは分離しておくのが扱いやすいです。

---

## 3. パス1: Glossary生成のプロンプト設計

Glossaryに含めるべき情報は4層あります。

**Layer 1: 文書メタデータ**

```yaml
title: "Real Analysis - Chapter 2: Integration"
author: "Bara Kim"
source: "Korea University, 2026 Spring"
textbook: "Real Analysis, Gerald B. Folland (2nd Ed.)"
document_type: "lecture_slides"
```

**Layer 2: 記号辞書（Symbol Dictionary）**

```yaml
symbols:
  - notation: "$\\mathcal{M}$"
    meaning: "σ-algebra on X"
    first_appears: "Definition (§2.1)"
  - notation: "$\\chi_E$"
    meaning: "characteristic (indicator) function of set E"
    first_appears: "Definition (§2.1)"
  - notation: "$f^+, f^-$"
    meaning: "positive/negative parts of f"
    definition: "$f^+ = \\max\\{f, 0\\}$, $f^- = \\max\\{-f, 0\\}$"
  - notation: "$L^+(X)$"
    meaning: "nonnegative measurable functions on X"
  # ...
```

**Layer 3: 構造パターン**

```yaml
structure:
  numbering: "Chapter.Item (e.g., 2.1, 2.2, ...)"
  element_types:
    - "Definition (unnumbered)"
    - "Proposition (numbered: 2.1, 2.3, 2.6, ...)"
    - "Theorem (numbered: 2.10, ...)"
    - "Corollary (numbered: 2.2, 2.5, ...)"
    - "Remark (unnumbered)"
    - "Exercise (numbered: 49, ...)"
  progression: "Definition → Proposition → Corollary → Remark, with proofs after theorems"
```

**Layer 4: 表記ルール（Style Rules）**

```yaml
style_rules:
  - "Measurable means (M,N)-measurable unless context specifies otherwise"
  - "a.e. = almost everywhere"
  - "'simple function' always refers to finite linear combination of characteristic functions"
  - "ν and μ are used consistently for measures on Y and X respectively"
```

**プロンプト設計：**

```
You are analyzing an OCR'd mathematical document to create a reference glossary.

## Task
Read the entire document and extract:
1. Document metadata (title, author, source, type)
2. Symbol dictionary: every mathematical symbol/notation with its meaning and where it's first defined
3. Structural patterns: numbering scheme, element types (Definition, Theorem, etc.), logical flow
4. Style rules: notational conventions, abbreviations, implicit assumptions

## Output format
Return YAML (not Markdown). Be exhaustive for symbols — missing a symbol definition
will cause errors in downstream processing.

## Important
- Only extract what IS in the document. Do not infer or add standard definitions
  that aren't explicitly stated.
- For symbols that are used but never formally defined in THIS document
  (e.g., standard notation assumed from prerequisites), list them separately
  under "assumed_notation".

<document>
{full_document_text}
</document>
```

ポイントは「assumed_notation」の分離です。数学文書では $\mathbb{R}$, $\sigma$-algebra 等の「定義なしで使われる標準記法」が大量にあり、これとこの文書で新たに定義される記法を区別しないと、Glossaryが肥大化してパス2のプロンプトを圧迫します。

---

## 4. パス2: 整形プロンプトの設計と忠実性制約

ここが最もデリケートな部分です。

**プロンプトの構造：**

```
You are reformatting an OCR'd mathematical document chunk into clean Markdown.

## Glossary (reference only — do not modify content based on this)
{glossary_yaml}

## Context from previous chunk
{context_from_previous}

## STRICT RULES

### Faithfulness constraints
1. NEVER add, remove, or modify mathematical content. Your job is FORMATTING ONLY.
2. Do not "fix" what looks like a mathematical error — it may be intentional or
   you may be wrong.
3. Do not expand abbreviations in mathematical statements (e.g., keep "a.e." as is).
4. Do not add explanatory text, transitions, or commentary.
5. If something is ambiguous, preserve the original OCR text and add a comment:
   `<!-- OCR-UNCERTAIN: original text was "..." -->`

### Formatting rules
1. Section headings: Use ## for section numbers (## 2.1 Measurable functions)
2. Named elements: Use ### for Definition, Theorem, Proposition, Corollary, Lemma, Remark
   Format: ### Proposition 2.6 or ### Definition (if unnumbered)
3. Proofs: Start with **Proof.** and end with $\square$
4. Display math: Use $$ blocks. One equation per block.
5. Inline math: Use single $ delimiters.
6. Enumerated items within theorems: Use (a), (b), (c) or (i), (ii), (iii) as in original.

### Noise removal
1. Remove slide navigation elements (repeated section listings with dots/bullets)
2. Remove repeated headers/footers (author, university, course title)
3. Remove page numbers and progress indicators
4. Do NOT remove: section headings that appear as part of document structure

### What to flag
If you encounter any of these, add an HTML comment:
- Broken LaTeX that you cannot confidently reconstruct
- Text that appears garbled or truncated
- Equations that seem incomplete (e.g., cut off at chunk boundary)

## Chunk to process
{chunk_text}
```

**忠実性制約の設計思想：**

ここでの核心的な問題は、LLMが「親切にしすぎる」ことです。具体的に起こりがちな事故：

1. **証明の補完**: Proof が途中で切れていると、LLMが「...したがって証明が完了する。□」と勝手に書き足す
2. **数式の「修正」**: OCRで `f^{-1}` が `f^{-l}` になっていた場合、LLMは正しく直すかもしれないが、元文書で本当に `f^{-l}` と書かれていた可能性もゼロではない
3. **記法の統一**: 文書内で `\nu` と `\mu` のタイポがあっても（この文書のL1436で実際に $\nu$ であるべきところに $\mu$ と書かれている）、LLMが「修正」すべきではない
4. **構造の再解釈**: Remarkの範囲がどこまでかをLLMが独自に判断して、次のDefinitionの一部をRemarkに含めてしまう

これらを防ぐために、プロンプトでは**「何をするか」より「何をしないか」を多く指定**するのが効果的です。上のプロンプトで Faithfulness constraints が Formatting rules より先に来ているのは意図的で、LLMはプロンプトの前半に書かれた制約をより強く遵守する傾向があります。

**`<!-- OCR-UNCERTAIN -->`コメントの重要性：**

これが地味に強力な仕組みで、LLMに「確信がないなら勝手に直すな、フラグを立てろ」という逃げ道を与えることで、誤修正を防ぎます。後処理でこのコメントを検索して、人間がレビューすべき箇所のリストを自動生成できます。

---

## パイプライン全体の統合

全体をまとめると：

```
PDF → OCR → raw_markdown
       ↓
[前処理] 繰り返しパターン検出・除去、ページマーカー挿入
       ↓
   cleaned_markdown
       ↓
[パス1] LLMでGlossary生成 (全文 or サンプリング)
       ↓
   glossary.yaml
       ↓
[中間処理] セマンティックチャンキング (Definition/Theorem単位)
       ↓
   chunks[] + context_from_previous[]
       ↓
[パス2] 各チャンクをLLMで整形 (glossary + context + chunk → formatted_chunk)
       ↓
   formatted_chunks[]
       ↓
[後処理] チャンク結合、重複除去、LaTeX検証、番号整合性チェック
       ↓
   final_document.md
```

次のステップとして、このパイプラインの一部を実際にこの文書で試してみますか？例えば前処理スクリプトのプロトタイプを書いて、ノイズ除去の効果を確認するとか、パス1のGlossary生成を実際に走らせてみるとか。
