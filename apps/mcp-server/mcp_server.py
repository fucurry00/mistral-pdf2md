"""
MCP Server: PDF → Markdown pipeline

Tool: convert_pdf
  OCR (Mistral) → Cleanup → [proofread-ocr (Gemini)] → output_dir/{stem}/
"""

import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from convert_pdf_to_markdown import convert_pdf_to_markdown
from cleanup_ocr import clean, PRESETS

mcp = FastMCP("pdf2md")


@mcp.tool()
def convert_pdf(
    pdf_path: str,
    output_dir: str,
    preset: str = "dummit-foote",
    chunk_size: int = 20,
    pages: str | None = None,
    timeout: int = 120,
    proofread: bool = False,
) -> dict:
    """PDFをMarkdownに変換する（OCR → cleanup → Gemini校正）。

    Args:
        pdf_path: 入力PDFのパス
        output_dir: 出力先ディレクトリ（{output_dir}/{stem}/ に保存）
        preset: cleanupプリセット名（"dummit-foote" or ""）
        chunk_size: OCR APIのページ数/回（デフォルト20）
        pages: ページ選択 "1-5" or "1,3,5"（省略時は全ページ）
        timeout: Mistral APIタイムアウト秒（デフォルト120）
        proofread: Trueでproofread-ocr（Gemini 4フェーズ清書）を実行
    """
    pdf = Path(pdf_path).resolve()
    if not pdf.exists():
        raise FileNotFoundError(f"PDF not found: {pdf}")

    stem = pdf.stem
    dest_dir = Path(output_dir).resolve() / stem
    dest_dir.mkdir(parents=True, exist_ok=True)
    md_path = dest_dir / f"{stem}.md"

    steps_run = []

    # Step 1: OCR
    convert_pdf_to_markdown(
        pdf_path=str(pdf),
        output_path=str(md_path),
        page_selection=pages,
        chunk_size=chunk_size if chunk_size > 0 else None,
        timeout=timeout,
    )
    steps_run.append("ocr")

    # Step 2: Cleanup
    original = md_path.read_text(encoding="utf-8")
    bak_path = md_path.with_suffix(".md.bak")
    bak_path.write_text(original, encoding="utf-8")

    header_patterns = PRESETS.get(preset, []) if preset else []
    cleaned = clean(
        original,
        header_patterns=header_patterns,
        remove_separators=True,
        page_min=3,
        page_max=4,
    )
    md_path.write_text(cleaned, encoding="utf-8")
    steps_run.append("cleanup")

    # Step 3: proofread-ocr による Gemini 清書（optional）
    if proofread:
        cmd = [
            "uv", "run", "proofread-ocr",
            str(md_path),
            "-o", str(md_path),
            "-w", str(dest_dir / ".proofread"),
            "--skip-context-review",
        ]
        if preset:
            cmd += ["--preset", preset]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if result.returncode != 0:
            raise RuntimeError(
                f"proofread-ocr failed (exit {result.returncode}): {result.stderr.strip()}"
            )
        steps_run.append("proofread")

    images_dir = dest_dir / "images"
    image_paths = sorted(str(p) for p in images_dir.glob("*.jpeg")) if images_dir.exists() else []

    return {
        "md_path": str(md_path),
        "image_paths": image_paths,
        "steps_run": steps_run,
        "backup_path": str(bak_path),
        "proofread_path": str(md_path) if proofread else None,
    }


if __name__ == "__main__":
    mcp.run()
