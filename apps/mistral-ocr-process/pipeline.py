#!/usr/bin/env python3
"""
PDF → Markdown 変換パイプライン（OCR → cleanup → Gemini分析）

単一ファイル:
    python pipeline.py <input.pdf> [output_dir] [options]

ディレクトリ（バッチ）:
    python pipeline.py <pdf_dir/> [output_dir] [options]

実行ステップ:
    ocr      : Mistral OCR APIでPDF → Markdown変換
    cleanup  : OCRアーティファクトをクリーンアップ（--mode で選択）
    analyze  : Gemini CLIで残存アーティファクトを検出してレポート生成

出力ディレクトリ構造:
    {output_dir}/{stem}/
      {stem}.md              # cleanup済みMarkdown
      {stem}.md.bak          # cleanup前バックアップ
      {stem}.analysis.md     # Gemini分析レポート
      images/                # 抽出画像
"""

import argparse
import subprocess
import sys
from pathlib import Path

DEFAULT_STEPS = ["ocr", "cleanup", "analyze"]
ALL_STEPS = ["ocr", "cleanup", "analyze"]

_GEMINI_ANALYZE_PROMPT = """\
以下のMarkdownファイルはPDFをOCRで変換したものです。
残存するOCRアーティファクトを検出してレポートを作成してください。

【出力形式】
## 残存OCRアーティファクト分析レポート

### 検出された問題
各問題につき以下を記述してください:
- 問題種別（例: ページ番号残存、ランニングヘッダー、LaTeXスペース崩れ等）
- 件数（概算）
- 具体的な箇所の例（前後の文脈付き）
- 正規表現修正パターン案（Pythonのre構文）

### 総評
修正スクリプトへの追加を推奨するルールのサマリー

【制約】
- ドキュメントの内容は一切修正しないこと（報告のみ）
- LaTeX数式（$...$、$$...$$）の誤検知に注意
- 数学的に正しい記述をアーティファクトとして誤報告しないこと
- 存在しない問題を作り出さないこと
"""


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


def run_analyze(md_path: Path, analysis_path: Path, timeout: int = 300):
    """Step 3: Gemini CLIで残存アーティファクトを検出してレポートを生成。"""
    content = md_path.read_text(encoding="utf-8")
    prompt = _GEMINI_ANALYZE_PROMPT + "\n\n---\n\n" + content

    result = subprocess.run(
        ["gemini", "--yolo", "-p", prompt],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0 or not result.stdout.strip():
        raise RuntimeError(
            f"gemini-cli failed (exit {result.returncode}): {result.stderr.strip()}"
        )

    analysis_path.write_text(result.stdout, encoding="utf-8")
    print(f"  Analysis report: {analysis_path}")


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
    analysis_path = dest / f"{stem}.analysis.md"

    if dry_run:
        statuses = []
        if "ocr" in steps:
            statuses.append(f"md={'EXISTS' if md_path.exists() else 'new'}")
        if "analyze" in steps:
            statuses.append(f"report={'EXISTS' if analysis_path.exists() else 'new'}")
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

    if "analyze" in steps:
        print("\n[Step 3/3] Gemini analysis...")
        run_analyze(md_path, analysis_path)
    else:
        print("[Step 3/3] Gemini analysis: skipped")

    print(f"\n✓ Done: {md_path}")


def main():
    parser = argparse.ArgumentParser(
        description="PDF → Markdown パイプライン（OCR → cleanup → Gemini分析）",
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
