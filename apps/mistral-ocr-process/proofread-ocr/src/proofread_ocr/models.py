"""Data models for the proofread-ocr pipeline."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class PipelineConfig:
    input_path: Path
    output_path: Path
    workdir: Path = Path(".proofread")
    model: str = "gemini-3-flash-preview"
    chunk_size: int = 20000
    overlap_lines: int = 5
    concurrency: int = 4
    timeout: int = 300
    phase: str | None = None
    skip_context_review: bool = False
    debug: bool = False
    force: bool = False
    dry_run: bool = False
    context_path: Path | None = None
    strip_annotations: bool = False
    thinking_level: str = "high"
    prompt_path: Path | None = None
    verbose: bool = False
    preset: str | None = None


@dataclass
class ChunkMeta:
    id: str
    section: str
    prev_section: str
    next_section: str
    line_start: int
    line_end: int
    estimated_tokens: int

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> ChunkMeta:
        return cls(**d)


@dataclass
class ChunkManifest:
    source: str
    total_chunks: int
    chunk_size_target: int
    overlap_lines: int
    chunks: list[ChunkMeta] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, d: dict) -> ChunkManifest:
        chunks = [ChunkMeta.from_dict(c) for c in d.get("chunks", [])]
        return cls(
            source=d["source"],
            total_chunks=d["total_chunks"],
            chunk_size_target=d["chunk_size_target"],
            overlap_lines=d["overlap_lines"],
            chunks=chunks,
        )

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> ChunkManifest:
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))


@dataclass
class ProofreadResult:
    chunk_id: str
    success: bool
    output_text: str | None = None
    error: str | None = None
    duration_sec: float = 0.0
    tokens_in: int | None = None
    tokens_out: int | None = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> ProofreadResult:
        return cls(**d)

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> ProofreadResult:
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))


@dataclass
class DiffEntry:
    section: str
    original: str
    corrected: str
    reason: str
    confidence: str  # "FIXED" or "UNCERTAIN"

    def to_dict(self) -> dict:
        return asdict(self)
