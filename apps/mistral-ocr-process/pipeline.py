#!/usr/bin/env python3
"""
PDF → Markdown 変換パイプライン（OCR → cleanup → Gemini清書）

単一ファイル:
    python pipeline.py <input.pdf> [output_dir] [options]

ディレクトリ（バッチ）:
    python pipeline.py <pdf_dir/> [output_dir] [options]

実行ステップ:
    ocr      : Mistral OCR APIでPDF → Markdown変換
    cleanup  : OCRアーティファクトをクリーンアップ（--mode で選択）
    proofread: proofread-ocr（Gemini）でLLMベース清書

出力ディレクトリ構造:
    {output_dir}/{stem}/
      {stem}.md              # 清書済みMarkdown（proofread実行時は上書き）
      {stem}.md.bak          # cleanup前バックアップ
      images/                # 抽出画像
"""

import argparse
import subprocess
import sys
from pathlib import Path

DEFAULT_STEPS = ["ocr", "cleanup", "proofread"]
ALL_STEPS = ["ocr", "cleanup", "proofread"]


def run_ocr(pdf_path: Path, md_path: Path, pages, chunk_size, timeout):
    """Step 1: Mistral OCRでPDF → Markdown変換。"""
    from convert_pdf_to_markdown import convert_pdf_to_markdown
    md_path.parent.mkdir(parents=True, exist_ok=True)
    convert_pdf_to_markdown(
        pdf_path=str(pdf_path),
        output_path=str(md_path),
        page_selection=pages,
        chunk_size=chunk_size if chunk_size and chunk_size > 0 else None,
        timeout=timeout,
    )


def run_cleanup(md_path: Path, mode: str, preset: str | None):
    """Step 2: クリーンアップスクリプトを subprocess で実行。"""
    script_dir = Path(__file__).parent
    script_path = script_dir / "cleanup_ocr.py"

    cmd = [sys.executable, str(script_path), str(md_path), "--mode", mode]
    if preset:
        cmd += ["--preset", preset]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"{script} failed (exit {result.returncode}):\n{result.stderr.strip()}"
        )
    if result.stdout.strip():
        print(result.stdout.rstrip())


def run_proofread(md_path: Path, preset: str | None, timeout: int = 600):
    """Step 3: proofread-ocr で Gemini 清書を実行。md_path を上書きする。"""
    cmd = [
        "uv", "run", "proofread-ocr",
        str(md_path),
        "-o", str(md_path),
        "-w", str(md_path.parent / ".proofread"),
        "--skip-context-review",
    ]
    if preset:
        cmd += ["--preset", preset]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError(
            f"proofread-ocr failed (exit {result.returncode}):\n{result.stderr.strip()}"
        )
    if result.stdout.strip():
        print(result.stdout.rstrip())


def process_single(
    pdf_path: Path,
    output_dir: Path,
    steps: list[str],
    mode: str,
    preset: str | None,
    pages: str | None,
    chunk_size: int,
    timeout: int,
    dry_run: bool,
):
    """1つのPDFをパイプラインで処理する。"""
    stem = pdf_path.stem
    dest = output_dir / stem
    md_path = dest / f"{stem}.md"

    if dry_run:
        statuses = []
        if "ocr" in steps:
            statuses.append(f"md={'EXISTS' if md_path.exists() else 'new'}")
        if "proofread" in steps:
            statuses.append("proofread=pending")
        print(f"  [dry-run] {pdf_path.name}  →  {dest}/  ({', '.join(statuses)})")
        return

    print(f"\n{'='*60}")
    print(f"Processing: {pdf_path.name}")
    print(f"Output:     {dest}/")
    if steps != ALL_STEPS:
        print(f"Steps:      {', '.join(steps)}")

    if "ocr" in steps:
        print("\n[Step 1/3] OCR...")
        run_ocr(pdf_path, md_path, pages, chunk_size, timeout)
    else:
        print("[Step 1/3] OCR: skipped")
        if not md_path.exists():
            raise FileNotFoundError(
                f"OCR step skipped but {md_path} does not exist. "
                "Run with --steps ocr first."
            )

    if "cleanup" in steps:
        print(f"\n[Step 2/3] Cleanup (mode={mode})...")
        run_cleanup(md_path, mode, preset)
    else:
        print("[Step 2/3] Cleanup: skipped")

    if "proofread" in steps:
        print("\n[Step 3/3] Gemini proofreading...")
        run_proofread(md_path, preset)
    else:
        print("[Step 3/3] Proofreading: skipped")

    print(f"\n✓ Done: {md_path}")


def main():
    parser = argparse.ArgumentParser(
        description="PDF → Markdown パイプライン（OCR → cleanup → Gemini清書）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        help="入力PDFファイル、またはPDFが入ったディレクトリ（バッチモード）",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=None,
        help="出力先ディレクトリ（省略時は入力と同じ場所に {stem}/ を作成）",
    )
    parser.add_argument(
        "--mode",
        choices=["math", "general"],
        default="math",
        help="クリーンアップモード: math（数学特化）または general（汎用）（デフォルト: math）",
    )
    parser.add_argument(
        "--steps",
        default=",".join(DEFAULT_STEPS),
        metavar="STEPS",
        help=f"実行するステップをカンマ区切りで指定（デフォルト: {','.join(DEFAULT_STEPS)}）"
        f"\n選択肢: {', '.join(ALL_STEPS)}",
    )
    parser.add_argument(
        "--preset",
        default=None,
        metavar="NAME",
        help="クリーンアップのpresetを指定（例: dummit-foote）",
    )
    parser.add_argument(
        "--pages",
        default=None,
        help='OCR対象ページ選択（単一ファイル時のみ有効）: "1-5" または "1,3,5"',
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=20,
        help="OCR APIの1回あたりのページ数（デフォルト: 20、0=チャンキングなし）",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Mistral APIタイムアウト秒（デフォルト: 120）",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="実際の処理を行わず、対象ファイルと出力先のみ表示する",
    )

    args = parser.parse_args()

    # ステップ解析
    steps = [s.strip() for s in args.steps.split(",")]
    invalid = [s for s in steps if s not in ALL_STEPS]
    if invalid:
        print(f"Error: 不明なステップ: {invalid}. 有効なステップ: {ALL_STEPS}", file=sys.stderr)
        sys.exit(1)

    input_path = Path(args.input)
    chunk_size = args.chunk_size if args.chunk_size > 0 else None

    # ── ディレクトリ（バッチ）モード ──────────────────────────────────
    if input_path.is_dir():
        pdf_files = sorted(input_path.glob("*.pdf"))
        if not pdf_files:
            print(f"Error: PDFファイルが見つかりません: {input_path}", file=sys.stderr)
            sys.exit(1)

        output_dir = Path(args.output_dir) if args.output_dir else input_path

        if args.dry_run:
            print(f"[dry-run] {len(pdf_files)} 件のPDFを検出: {input_path}")
            for pdf in pdf_files:
                process_single(
                    pdf, output_dir, steps, args.mode, args.preset,
                    None, chunk_size, args.timeout, dry_run=True,
                )
            return

        if args.pages:
            print(
                "Warning: --pages はバッチモードでは無視されます。",
                file=sys.stderr,
            )

        output_dir.mkdir(parents=True, exist_ok=True)
        errors = []
        for i, pdf in enumerate(pdf_files, 1):
            print(f"\n[{i}/{len(pdf_files)}] {pdf.name}")
            try:
                process_single(
                    pdf, output_dir, steps, args.mode, args.preset,
                    None, chunk_size, args.timeout, dry_run=False,
                )
            except Exception as e:
                print(f"  Error: {e}", file=sys.stderr)
                errors.append((pdf.name, str(e)))

        print(f"\nバッチ完了: {len(pdf_files) - len(errors)}/{len(pdf_files)} 件成功。")
        if errors:
            print("失敗したファイル:", file=sys.stderr)
            for name, msg in errors:
                print(f"  {name}: {msg}", file=sys.stderr)
            sys.exit(1)

    # ── 単一ファイルモード ────────────────────────────────────────────
    else:
        if not input_path.exists():
            print(f"Error: ファイルが見つかりません: {input_path}", file=sys.stderr)
            sys.exit(1)
        if input_path.suffix.lower() != ".pdf":
            print(f"Error: PDFファイルを指定してください: {input_path}", file=sys.stderr)
            sys.exit(1)

        output_dir = Path(args.output_dir) if args.output_dir else input_path.parent

        if args.dry_run:
            process_single(
                input_path, output_dir, steps, args.mode, args.preset,
                args.pages, chunk_size, args.timeout, dry_run=True,
            )
            return

        try:
            process_single(
                input_path, output_dir, steps, args.mode, args.preset,
                args.pages, chunk_size, args.timeout, dry_run=False,
            )
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
