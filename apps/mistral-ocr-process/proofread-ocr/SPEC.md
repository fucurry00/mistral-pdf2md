# proofread-ocr Specification

`proofread-ocr` proofreads OCR-converted Markdown while preserving the source
meaning. The implementation is the authority; this file summarizes the current
contract.

## Command

```bash
uv run proofread-ocr <input.md> [options]
uv run proofread-ocr <directory/> -o <output_dir/>
```

Important options:

| Option | Default | Purpose |
| --- | --- | --- |
| `-o, --output` | `{input}_proofread.md` | Output path |
| `-w, --workdir` | `.proofread/` | Intermediate files |
| `--phase` | all | One of `context`, `chunk`, `proofread`, `merge` |
| `--chunk-size` | `20000` | Approximate token target |
| `--overlap-lines` | `5` | Context overlap between chunks |
| `--concurrency` | `10` | Parallel `agy` invocations |
| `--timeout` | `300` | Per-chunk timeout in seconds |
| `--model` | `gemini-3.5-flash` | Gemini model passed to the backend |
| `--edit-mode` | `rewrite` | `rewrite` or experimental `hashline` |
| `--strip-annotations` | off | Remove correction comments from output |

## Phases

1. `context`: extract notation, structure, and terminology into `context.md`.
2. `chunk`: split Markdown at heading boundaries into chunk files and a
   manifest.
3. `proofread`: run parallel Antigravity CLI (`agy`) jobs for each chunk.
4. `merge`: combine results, strip overlaps, and write reports.

## Workdir Layout

```text
.proofread/
├── context.md
├── chunks/
│   ├── chunk_manifest.json
│   └── chunk_*.md
└── results/
    └── result_*.md
```

Merge writes:

```text
proofread.md or requested output path
output/diff_report.md
output/stats.json
```

## Backends

The current backend is Antigravity CLI (`agy`). The stable boundary is around
the `run_gemini()` behavior in `src/proofread_ocr/gemini.py`: prompt, context,
and chunk text go in; corrected Markdown comes out.

Future provider support should keep that boundary small. The first OpenAI
backend should be synchronous per-chunk Responses API execution. Batch API
support should remain future-only until there is a concrete operational need.

Codex App Server is not the proofreading backend because this package needs a
deterministic text-to-text batch executor, not a threaded agent client.

## Edit Modes

- `rewrite`: the model returns the full corrected chunk.
- `hashline`: the model returns a Hashline patch; a Bun sidecar applies it to
  the original numbered chunk snapshot.

Hashline mode requires Bun and the sidecar dependencies. See
`docs/hashline-edit-mode.md`.

## Invariants

- Preserve the author's meaning.
- Annotate corrections unless `--strip-annotations` is requested.
- Re-runs should reuse cached chunk results unless `--force` is set.
- Inputs and outputs are UTF-8 Markdown.
