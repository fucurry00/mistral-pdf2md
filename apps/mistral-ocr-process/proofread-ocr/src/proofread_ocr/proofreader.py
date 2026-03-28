"""Phase 3: Parallel proofreading of chunks using Gemini."""

from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path

from .gemini import GeminiResponse, launch_tmux_session, run_gemini
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

    # Resume support: skip if result already exists
    if not config.force and result_path.exists():
        try:
            existing = ProofreadResult.load(result_path)
            if existing.success:
                if config.verbose:
                    print(f"  Chunk {chunk_id}: skipped (cached)")
                return existing
        except Exception:
            pass  # Re-process if result file is corrupted

    async with semaphore:
        if config.verbose:
            print(f"  Chunk {chunk_id}: processing...")

        start = time.monotonic()
        response = await run_gemini(
            file_paths=[prompt_path, context_path, chunk_path],
            prompt="Proofread the following OCR text per the instructions provided via stdin.",
            model=config.model,
            output_format="json",
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
                    error="Empty response from Gemini",
                    duration_sec=duration,
                )
                print(f"  Chunk {chunk_id}: FAILED (empty response)", file=sys.stderr)
            else:
                result = ProofreadResult(
                    chunk_id=chunk_id,
                    success=True,
                    output_text=text,
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

    # tmux debug mode
    if config.debug:
        print(f"Phase 3: Launching tmux session with {len(chunk_paths)} panes...")
        launch_tmux_session(
            chunks=chunk_paths,
            context_path=context_path,
            prompt_path=prompt_path,
            results_dir=results_dir,
            model=config.model,
        )
        # After tmux detach, load results
        results = []
        for meta in manifest.chunks:
            result_path = results_dir / f"chunk_{meta.id}.json"
            if result_path.exists():
                results.append(ProofreadResult.load(result_path))
            else:
                results.append(ProofreadResult(
                    chunk_id=meta.id, success=False, error="No result after tmux session",
                ))
        return results

    # Async subprocess mode
    print(f"Phase 3: Proofreading {len(chunk_paths)} chunks (concurrency={config.concurrency})...")
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
