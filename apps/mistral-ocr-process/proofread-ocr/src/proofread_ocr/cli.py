"""CLI entry point for proofread-ocr."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from . import __version__


def _resolve_prompt_dir() -> Path:
    """Locate the prompts/ directory relative to the package."""
    # Try relative to this file's package
    pkg_dir = Path(__file__).resolve().parent
    candidates = [
        pkg_dir.parent.parent / "prompts",  # src layout: src/proofread_ocr/../../prompts
        pkg_dir / "prompts",
    ]
    for d in candidates:
        if d.is_dir():
            return d
    # Fallback: current working directory
    return Path("prompts")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="proofread-ocr",
        description="LLMベースOCR校正パイプライン",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  proofread-ocr input.md\n"
            "  proofread-ocr input.md --phase context\n"
            "  proofread-ocr input.md --dry-run --verbose\n"
            "  proofread-ocr input.md --context context.md --phase proofread --force\n"
            "  proofread-ocr docs/ -o output/\n"
        ),
    )
    parser.add_argument("input", help="入力Markdownファイルまたはディレクトリ")
    parser.add_argument(
        "-o", "--output", default=None,
        help="出力先ファイルパス（デフォルト: {input}_proofread.md）",
    )
    parser.add_argument(
        "-w", "--workdir", default=".proofread",
        help="作業ディレクトリ（デフォルト: .proofread/）",
    )
    parser.add_argument(
        "-m", "--model", default="gemini-3-flash-preview",
        help="Geminiモデル（デフォルト: gemini-3-flash-preview）",
    )

    # Phase selection
    parser.add_argument(
        "--phase", choices=["context", "chunk", "proofread", "merge"],
        default=None, help="特定フェーズのみ実行",
    )

    # Chunking options
    parser.add_argument(
        "--chunk-size", type=int, default=20000,
        help="チャンクサイズ上限（トークン、デフォルト: 20000）",
    )
    parser.add_argument(
        "--overlap-lines", type=int, default=5,
        help="オーバーラップ行数（デフォルト: 5）",
    )

    # Execution options
    parser.add_argument("--concurrency", type=int, default=4, help="並列度（デフォルト: 4）")
    parser.add_argument("--timeout", type=int, default=300, help="チャンクあたりのタイムアウト秒（デフォルト: 300）")
    parser.add_argument("--skip-context-review", action="store_true", help="Phase 1後の人間レビューをスキップ")
    parser.add_argument("--debug", action="store_true", help="tmuxモードで実行")
    parser.add_argument("--force", action="store_true", help="既存の結果を無視して再実行")
    parser.add_argument("--dry-run", action="store_true", help="実行せず、チャンク分割結果のみ表示")
    parser.add_argument("--verbose", action="store_true", help="詳細ログ出力")

    # Context options
    parser.add_argument(
        "--context", default=None,
        help="既存のcontext.mdを指定（Phase 1をスキップ）",
    )
    parser.add_argument("--preset", default=None, help="書籍プリセット")

    # Prompt options
    parser.add_argument("--prompt", default=None, help="カスタム校正プロンプトを指定")
    parser.add_argument(
        "--thinking-level", default="high",
        choices=["minimal", "low", "medium", "high"],
        help="Gemini thinking level（デフォルト: high）",
    )

    # Output options
    parser.add_argument("--strip-annotations", action="store_true", help="出力からアノテーションを除去")

    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    return parser


async def _run_pipeline(args: argparse.Namespace) -> None:
    from .chunker import chunk_document, write_chunks
    from .context import extract_context
    from .merger import merge_results
    from .models import ChunkManifest, PipelineConfig
    from .proofreader import run_proofreading

    input_path = Path(args.input).resolve()
    workdir = Path(args.workdir).resolve()
    prompt_dir = _resolve_prompt_dir()

    # Determine output path
    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = input_path.parent / f"{input_path.stem}_proofread.md"

    config = PipelineConfig(
        input_path=input_path,
        output_path=output_path,
        workdir=workdir,
        model=args.model,
        chunk_size=args.chunk_size,
        overlap_lines=args.overlap_lines,
        concurrency=args.concurrency,
        timeout=args.timeout,
        phase=args.phase,
        skip_context_review=args.skip_context_review,
        debug=args.debug,
        force=args.force,
        dry_run=args.dry_run,
        context_path=Path(args.context).resolve() if args.context else None,
        strip_annotations=args.strip_annotations,
        thinking_level=args.thinking_level,
        prompt_path=Path(args.prompt).resolve() if args.prompt else None,
        verbose=args.verbose,
        preset=args.preset,
    )

    chunks_dir = workdir / "chunks"
    results_dir = workdir / "results"
    output_dir = output_path.parent / "output"
    context_prompt = config.prompt_path or (prompt_dir / "extract_context.md")
    proofread_prompt = config.prompt_path or (prompt_dir / "proofread.md")

    phase = config.phase
    context_path = config.context_path
    context_duration: float | None = None

    # Handle directory input
    if input_path.is_dir():
        md_files = sorted(input_path.glob("*.md"))
        if not md_files:
            print(f"Error: No .md files found in {input_path}", file=sys.stderr)
            sys.exit(1)
        print(f"Found {len(md_files)} markdown files in {input_path}")
        for md_file in md_files:
            print(f"\n{'='*60}")
            print(f"Processing: {md_file.name}")
            # Recurse with single file
            file_args = argparse.Namespace(**vars(args))
            file_args.input = str(md_file)
            file_args.output = str(
                Path(args.output or input_path.parent) / f"{md_file.stem}_proofread.md"
            )
            file_args.workdir = str(workdir / md_file.stem)
            await _run_pipeline(file_args)
        return

    # Validate input
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    print(f"Input: {input_path} ({len(text)} chars)")

    # --- Phase 1: Context Extraction ---
    if phase is None or phase == "context":
        if context_path and context_path.exists():
            print(f"Using existing context: {context_path}")
        else:
            context_path, context_duration = await extract_context(
                input_path=input_path,
                workdir=workdir,
                prompt_path=context_prompt,
                model=config.model,
                skip_review=config.skip_context_review,
                verbose=config.verbose,
            )
        if phase == "context":
            print(f"\nPhase 1 complete. Context: {context_path}")
            return
    else:
        # Load existing context for later phases
        if context_path is None:
            context_path = workdir / "context.md"
        if not context_path.exists():
            print(f"Error: context.md not found at {context_path}. Run --phase context first.", file=sys.stderr)
            sys.exit(1)

    # --- Phase 2: Chunking ---
    if phase is None or phase == "chunk":
        print(f"\nPhase 2: Chunking (target={config.chunk_size} tokens, overlap={config.overlap_lines} lines)...")
        chunk_contents, manifest = chunk_document(
            text=text,
            chunk_size_tokens=config.chunk_size,
            overlap_lines=config.overlap_lines,
            source_name=input_path.name,
        )
        write_chunks(chunk_contents, manifest, chunks_dir)
        print(f"  Created {manifest.total_chunks} chunks in {chunks_dir}")

        if config.dry_run:
            print(f"\n--- Dry Run: Chunk Summary ---")
            for meta in manifest.chunks:
                print(f"  chunk_{meta.id}: {meta.section} ({meta.estimated_tokens} tokens, "
                      f"lines {meta.line_start}-{meta.line_end})")
            print(f"\nGemini commands that would be executed:")
            for meta in manifest.chunks:
                print(f"  cat {proofread_prompt} {context_path} {chunks_dir}/chunk_{meta.id}.md "
                      f"| gemini -p 'Proofread the following OCR text per the instructions provided via stdin.' "
                      f"--output-format json -m {config.model}")
            return

        if phase == "chunk":
            print(f"\nPhase 2 complete. Chunks: {chunks_dir}")
            return
    else:
        # Load existing manifest
        manifest_path = chunks_dir / "chunk_manifest.json"
        if not manifest_path.exists():
            print(f"Error: chunk_manifest.json not found. Run --phase chunk first.", file=sys.stderr)
            sys.exit(1)
        manifest = ChunkManifest.load(manifest_path)

    # --- Phase 3: Parallel Proofreading ---
    if phase is None or phase == "proofread":
        if config.dry_run:
            return

        results = await run_proofreading(
            manifest=manifest,
            chunks_dir=chunks_dir,
            context_path=context_path,
            prompt_path=proofread_prompt,
            results_dir=results_dir,
            config=config,
        )
        if phase == "proofread":
            succeeded = sum(1 for r in results if r.success)
            print(f"\nPhase 3 complete. {succeeded}/{len(results)} chunks proofread.")
            return
    else:
        results = None  # merger will load from disk

    # --- Phase 4: Merge + Review ---
    if phase is None or phase == "merge":
        print(f"\nPhase 4: Merging results...")
        out_path, diff_path, stats_path = merge_results(
            manifest=manifest,
            results_dir=results_dir,
            chunks_dir=chunks_dir,
            output_path=output_path,
            model=config.model,
            strip_annotations=config.strip_annotations,
            results=results,
            context_duration=context_duration,
        )
        print(f"\n{'='*60}")
        print(f"Output:      {out_path}")
        print(f"Diff report: {diff_path}")
        print(f"Stats:       {stats_path}")


def main():
    parser = build_parser()
    args = parser.parse_args()
    asyncio.run(_run_pipeline(args))


if __name__ == "__main__":
    main()
