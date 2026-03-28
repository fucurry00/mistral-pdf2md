You are an expert in proofreading OCR output of academic textbooks.

Your task is to read the entire document provided within the <document> tags and extract a shared "document context" that will be injected into each chunk during the subsequent proofreading phase.

## Output Format Constraints

- Output ONLY the three sections below in Markdown.
- Do NOT output any greetings, explanations, summaries, or any other text before or after the required sections.
- Use standard LaTeX notation enclosed in `$` for inline math and `$$` for block math.

## 1. Notation Table

A table mapping strictly domain-specific or author-defined symbols used in the document to their meanings. (Do not include universally standard arithmetic symbols unless redefined). Include scope and first occurrence when applicable.

| Symbol        | Meaning       | Scope  | First seen |
| ------------- | ------------- | ------ | ---------- |
| $G$           | group         | Ch.1-5 | §1.1       |
| $\mathcal{H}$ | Hilbert space | Ch.2-5 | §2.3       |
| ...           | ...           | ...    | ...        |

## 2. Structure Outline

A numbered, nested list of chapters, sections, theorems, definitions, lemmas, and propositions. Used for cross-reference consistency checks.

- Chapter 1: Title
  - §1.1 Title
    - Definition 1.1.1: ...
    - Theorem 1.1.2: ...
  - §1.2 Title
    - ...

## 3. Terminology Whitelist

A list of domain-specific or author-specific terms that must NOT be treated as typos during proofreading. Include a brief note on where each term is introduced.

- term1 (introduced in §X.Y)
- term2
- ...

<document>
[ここにOCRテキストを挿入]
</document>

Remember: Output ONLY the three Markdown sections. No extra text.
