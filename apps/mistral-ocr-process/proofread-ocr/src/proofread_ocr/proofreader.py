"""Phase 3: Parallel proofreading of chunks using a completion API."""

from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path

from .hashline import (
    HashlineError,
    apply_hashline_patch,
    describe_target,
    extract_hashline_patch,
)
from .llm import run_llm
from .models import ChunkManifest, PipelineConfig, ProofreadResult


async def _proofread_chunk(
    chunk_path: Path,
    context_path: Path,
    prompt_path: Path,
    results_dir: Path,
    config: PipelineConfig,
    semaphore: asyncio.Semaphore,
) -> ProofreadResult:
    """Proofread a single chunk."""
    chunk_id = chunk_path.stem.replace("chunk_", "")
    result_path = results_dir / f"chunk_{chunk_id}.json"
    chunk_text = chunk_path.read_text(encoding="utf-8")
    hashline_patch_text: str | None = None

    # Resume support: skip if result already exists
    if not config.force and result_path.exists():
        try:
            existing = ProofreadResult.load(result_path)
            if existing.success and existing.edit_mode == config.edit_mode:
                if config.verbose:
                    print(f"  Chunk {chunk_id}: skipped (cached)")
                return existing
        except Exception:
            pass  # Re-process if result file is corrupted

    async with semaphore:
        if config.verbose:
            print(f"  Chunk {chunk_id}: processing...")

        start = time.monotonic()
        file_paths = [prompt_path, context_path, chunk_path]
        prompt = "Proofread the following OCR text per the instructions in the input."
        if config.edit_mode == "hashline":
            try:
                target = await describe_target(chunk_path.name, chunk_text, timeout=30)
            except HashlineError as exc:
                duration = time.monotonic() - start
                result = ProofreadResult(
                    chunk_id=chunk_id,
                    success=False,
                    edit_mode=config.edit_mode,
                    error=str(exc)[:500],
                    duration_sec=duration,
                )
                result.save(result_path)
                print(f"  Chunk {chunk_id}: FAILED ({str(exc)[:100]})", file=sys.stderr)
                return result

            target_dir = results_dir / "hashline_targets"
            target_dir.mkdir(parents=True, exist_ok=True)
            target_path = target_dir / f"chunk_{chunk_id}.hashline.md"
            target_path.write_text(
                "\n".join(
                    [
                        "## Hashline Target",
                        "",
                        f"Edit this exact chunk only. Use this section header in the patch: `{target.header}`",
                        "",
                        "```hashline-source",
                        target.header,
                        target.numbered_text,
                        "```",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            file_paths = [prompt_path, context_path, target_path]
            prompt = "Return only a Hashline patch for the OCR proofreading target."

        response = await run_llm(
            file_paths=file_paths,
            prompt=prompt,
            model=config.model,
            timeout=config.timeout,
        )
        duration = time.monotonic() - start

        if response.returncode != 0:
            result = ProofreadResult(
                chunk_id=chunk_id,
                success=False,
                error=response.stderr[:500],
                duration_sec=duration,
            )
            print(f"  Chunk {chunk_id}: FAILED ({response.stderr[:100]})", file=sys.stderr)
        else:
            text = response.text
            if not text.strip():
                result = ProofreadResult(
                    chunk_id=chunk_id,
                    success=False,
                    error="Empty response from LLM",
                    duration_sec=duration,
                )
                print(f"  Chunk {chunk_id}: FAILED (empty response)", file=sys.stderr)
            else:
                text = response.text
                if config.edit_mode == "hashline":
                    try:
                        hashline_patch_text = extract_hashline_patch(response.text)
                        text = await apply_hashline_patch(
                            chunk_path.name,
                            chunk_text,
                            hashline_patch_text,
                            timeout=30,
                        )
                    except HashlineError as exc:
                        result = ProofreadResult(
                            chunk_id=chunk_id,
                            success=False,
                            patch_text=hashline_patch_text or response.text[:2000],
                            edit_mode=config.edit_mode,
                            error=str(exc)[:500],
                            duration_sec=duration,
                            tokens_in=response.tokens_in,
                            tokens_out=response.tokens_out,
                        )
                        print(f"  Chunk {chunk_id}: FAILED ({str(exc)[:100]})", file=sys.stderr)
                        result.save(result_path)
                        return result

                result = ProofreadResult(
                    chunk_id=chunk_id,
                    success=True,
                    output_text=text,
                    patch_text=hashline_patch_text,
                    edit_mode=config.edit_mode,
                    duration_sec=duration,
                    tokens_in=response.tokens_in,
                    tokens_out=response.tokens_out,
                )
                if config.verbose:
                    tokens_info = ""
                    if response.tokens_in:
                        tokens_info = f" ({response.tokens_in} in / {response.tokens_out} out)"
                    print(f"  Chunk {chunk_id}: done in {duration:.1f}s{tokens_info}")

        # Save result
        result.save(result_path)
        return result


async def run_proofreading(
    manifest: ChunkManifest,
    chunks_dir: Path,
    context_path: Path,
    prompt_path: Path,
    results_dir: Path,
    config: PipelineConfig,
) -> list[ProofreadResult]:
    """Run parallel proofreading of all chunks.

    Returns list of ProofreadResult for each chunk.
    """
    results_dir.mkdir(parents=True, exist_ok=True)

    chunk_paths = [chunks_dir / f"chunk_{meta.id}.md" for meta in manifest.chunks]

    # Verify all chunk files exist
    missing = [p for p in chunk_paths if not p.exists()]
    if missing:
        print(f"Error: Missing chunk files: {missing}", file=sys.stderr)
        sys.exit(1)

    # Async HTTP completion mode
    print(
        f"Phase 3: Proofreading {len(chunk_paths)} chunks "
        f"(concurrency={config.concurrency}, edit_mode={config.edit_mode})..."
    )
    semaphore = asyncio.Semaphore(config.concurrency)

    tasks = [
        _proofread_chunk(
            chunk_path=path,
            context_path=context_path,
            prompt_path=prompt_path,
            results_dir=results_dir,
            config=config,
            semaphore=semaphore,
        )
        for path in chunk_paths
    ]

    results = await asyncio.gather(*tasks)

    # Summary
    succeeded = sum(1 for r in results if r.success)
    failed = sum(1 for r in results if not r.success)
    total_time = sum(r.duration_sec for r in results)
    print(f"  Completed: {succeeded} succeeded, {failed} failed, {total_time:.1f}s total")

    return list(results)
