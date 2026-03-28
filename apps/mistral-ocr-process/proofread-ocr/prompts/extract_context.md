You are an expert in proofreading OCR output of academic textbooks.

Read the entire document below and extract a shared "document context" that will be injected into each chunk during the proofreading phase.

## Output Format

Output ONLY the three sections below in Markdown. No greetings, explanations, summaries, or any other text.

## Notation Table

A table mapping every symbol defined or used in the document to its meaning. Include scope and first occurrence when applicable.

| Symbol | Meaning | Scope | First seen |
| --- | --- | --- | --- |
| $G$ | group | Ch.1-5 | §1.1 |
| ... | ... | ... | ... |

## Structure Outline

A numbered, nested list of chapters, sections, theorems, definitions, lemmas, and propositions. Used for cross-reference consistency checks.

- Chapter 1: Title
  - §1.1 Title
    - Definition 1.1.1: ...
    - Theorem 1.1.2: ...
  - §1.2 Title
    - ...

## Terminology Whitelist

A list of domain-specific or author-specific terms that must NOT be treated as typos during proofreading. Include a brief note on where each term is introduced.

- term1 (introduced in §X.Y)
- term2
- ...
