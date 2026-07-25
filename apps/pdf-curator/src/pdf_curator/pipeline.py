"""End-to-end provenance-first OCR curation pipeline."""

from __future__ import annotations

import json
import re
from collections import Counter
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pdf_curator.blocks.prepass import propose_prepass
from pdf_curator.blocks.split import split_pages_into_blocks
from pdf_curator.config import load_mistral_api_key
from pdf_curator.editing.orchestrator import process_proposals
from pdf_curator.editing.planning import build_global_plan, reconcile_document
from pdf_curator.errors import ValidationError
from pdf_curator.llm.client import NoOpProposalClient, ProposalClient
from pdf_curator.models import (
    BlockType,
    DocumentModel,
    EditProposal,
    EditTrigger,
    GateStatus,
)
from pdf_curator.ocr.mistral_adapter import run_mistral_ocr
from pdf_curator.ocr.response_normalizer import normalize_ocr_response, response_to_dict
from pdf_curator.render.debug_bundle import write_debug_bundle
from pdf_curator.render.markdown import render_curated_markdown


@dataclass(slots=True)
class PipelineResult:
    curated_path: Path
    debug_dir: Path | None
    document: DocumentModel


def parse_page_selection(value: str | None) -> list[int] | None:
    if value is None:
        return None
    selected: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            raise ValidationError("page selection contains an empty item")
        if "-" in part:
            try:
                start, end = (int(item) for item in part.split("-", 1))
            except ValueError as error:
                raise ValidationError(f"invalid page range: {part}") from error
            if start <= 0 or end < start:
                raise ValidationError(f"invalid page range: {part}")
            selected.update(range(start, end + 1))
        else:
            try:
                page = int(part)
            except ValueError as error:
                raise ValidationError(f"invalid page number: {part}") from error
            if page <= 0:
                raise ValidationError("page numbers must be positive")
            selected.add(page)
    return sorted(selected)


def _retention_words(texts: list[str]) -> Counter[str]:
    return Counter(
        token.casefold()
        for text in texts
        for token in re.findall(r"[\w\u3040-\u30ff\u3400-\u9fff]+", text)
    )


def _client_proposals(
    client: ProposalClient, document: DocumentModel
) -> list[EditProposal]:
    proposed = client.propose(deepcopy(document.emitted_blocks()))
    if not isinstance(proposed, list) or not all(
        isinstance(proposal, EditProposal) for proposal in proposed
    ):
        raise ValidationError("ProposalClient must return list[EditProposal]")
    if any(proposal.trigger is EditTrigger.AUTO_PREPASS for proposal in proposed):
        raise ValidationError("ProposalClient cannot issue auto_prepass proposals")
    return proposed


def _enforce_success_metrics(
    *,
    retention: float,
    minimum_retention: float,
    accepted_content_add: int,
) -> None:
    if not 0.0 <= minimum_retention <= 1.0:
        raise ValidationError("minimum content retention must be between 0 and 1")
    if accepted_content_add != 0:
        raise ValidationError("accepted content_add count must remain zero")
    if retention < minimum_retention:
        raise ValidationError(
            f"source content-word retention {retention:.4f} is below "
            f"required floor {minimum_retention:.4f}"
        )


def run_pipeline(
    input_pdf: Path,
    output_dir: Path,
    *,
    from_ocr_json: Path | None = None,
    pages: str | None = None,
    debug: bool = False,
    proposal_client: ProposalClient | None = None,
    min_content_word_retention: float = 0.7,
) -> PipelineResult:
    if not input_pdf.is_file():
        raise ValidationError(f"input PDF does not exist: {input_pdf}")
    if input_pdf.suffix.casefold() != ".pdf":
        raise ValidationError(f"input must be a PDF file: {input_pdf}")
    output_dir.mkdir(parents=True, exist_ok=True)
    selected_pages = parse_page_selection(pages)

    raw: dict[str, Any] = {}
    normalized_pages: list[Any] = []
    blocks: list[Any] = []
    proposals: list[Any] = []
    decisions: list[Any] = []
    applied_diffs: list[Any] = []
    warnings: list[Any] = []
    try:
        if from_ocr_json is not None:
            if not from_ocr_json.is_file():
                raise ValidationError(f"OCR fixture does not exist: {from_ocr_json}")
            loaded = json.loads(from_ocr_json.read_text(encoding="utf-8"))
            if not isinstance(loaded, dict):
                raise ValidationError("OCR fixture root must be an object")
            raw = loaded
        else:
            response = run_mistral_ocr(
                input_pdf,
                api_key=load_mistral_api_key(),
                selected_pages=selected_pages,
            )
            raw = response_to_dict(response)

        normalized_pages = normalize_ocr_response(raw)
        if selected_pages is not None and from_ocr_json is not None:
            normalized_pages = [page for page in normalized_pages if page.index in selected_pages]
            missing = sorted(set(selected_pages) - {page.index for page in normalized_pages})
            if missing:
                raise ValidationError(f"selected pages are absent from OCR input: {missing}")
        elif selected_pages is not None:
            if len(normalized_pages) != len(selected_pages):
                raise ValidationError(
                    "live OCR response page count does not match the selected PDF pages"
                )
            for normalized_page, source_page in zip(
                normalized_pages, selected_pages, strict=True
            ):
                normalized_page.index = source_page
        if not normalized_pages:
            raise ValidationError("page selection produced no OCR pages")

        blocks = split_pages_into_blocks(normalized_pages)
        metadata = raw.get("metadata", {})
        if not isinstance(metadata, dict):
            raise ValidationError("fixture metadata must be an object")
        document = DocumentModel(
            source_pdf=str(input_pdf),
            page_count=len(normalized_pages),
            pages=normalized_pages,
            blocks=blocks,
            metadata=metadata,
            warnings=warnings,
        )
        prepass_proposals = propose_prepass(
            document.blocks, page_count=len(normalized_pages)
        )
        prepass_decisions, prepass_diffs = process_proposals(
            document, prepass_proposals
        )
        pre_edit_texts = [block.text for block in document.emitted_blocks()]

        for block in document.active_blocks():
            if block.type is BlockType.UNKNOWN:
                warnings.append(
                    {
                        "type": "unknown_block",
                        "block_id": block.id,
                        "pages": block.require_provenance().label(),
                    }
                )
            elif block.type is BlockType.TABLE and block.attrs.get("broken"):
                warnings.append(
                    {
                        "type": "unresolved_table",
                        "block_id": block.id,
                        "pages": block.require_provenance().label(),
                    }
                )
            elif block.attrs.get("visual_type") == "formula" and block.attrs.get("low_confidence"):
                warnings.append(
                    {
                        "type": "uncertain_formula",
                        "block_id": block.id,
                        "pages": block.require_provenance().label(),
                    }
                )

        global_plan = build_global_plan(document)
        client = proposal_client or NoOpProposalClient()
        chunk_proposals = _client_proposals(client, document)
        chunk_decisions, chunk_diffs = process_proposals(document, chunk_proposals)

        reconciliation_plan = build_global_plan(document)
        reconciliation = reconcile_document(document, reconciliation_plan)
        reconciliation_decisions, reconciliation_diffs = process_proposals(
            document, reconciliation.proposals
        )
        warnings.extend(reconciliation.warnings)

        proposals = [
            *prepass_proposals,
            *chunk_proposals,
            *reconciliation.proposals,
        ]
        decisions = [
            *prepass_decisions,
            *chunk_decisions,
            *reconciliation_decisions,
        ]
        applied_diffs = [*prepass_diffs, *chunk_diffs, *reconciliation_diffs]
        counts = Counter(decision.status.value for decision in decisions)
        accepted_content_add = sum(
            decision.status is GateStatus.ACCEPTED
            and decision.proposal.type.value == "content_add"
            for decision in decisions
        )
        source_words = _retention_words(pre_edit_texts)
        output_words = _retention_words(
            [block.text for block in document.emitted_blocks()]
        )
        retained = sum((source_words & output_words).values())
        retention = retained / max(1, sum(source_words.values()))
        _enforce_success_metrics(
            retention=retention,
            minimum_retention=min_content_word_retention,
            accepted_content_add=accepted_content_add,
        )
        prepass_changes = sum(
            decision.status is GateStatus.ACCEPTED
            and decision.proposal.trigger is EditTrigger.AUTO_PREPASS
            for decision in prepass_decisions
        )
        document.processing_summary = {
            "ocr": "mistral-ocr-latest" if from_ocr_json is None else "recorded-mistral-ocr",
            "llm_editing": type(client).__name__,
            "prepass_changes": prepass_changes,
            "global_planning": {
                "outline_sections": len(global_plan.outline),
                "noise_candidates": len(global_plan.noise_candidates),
                "chunks": len(global_plan.chunks),
            },
            "global_reconciliation": {
                "proposals": len(reconciliation.proposals),
                "warnings": len(reconciliation.warnings),
            },
            "gate": {
                "accepted": counts[GateStatus.ACCEPTED.value],
                "isolated": counts[GateStatus.ISOLATED.value],
                "rejected": counts[GateStatus.REJECTED.value],
                "accepted_content_add": accepted_content_add,
            },
            "source_content_word_retention": round(retention, 4),
            "minimum_content_word_retention": min_content_word_retention,
        }
        curated = render_curated_markdown(document)
        curated_path = output_dir / "curated.md"
        curated_path.write_text(curated, encoding="utf-8")

        debug_dir = None
        if debug:
            debug_dir = write_debug_bundle(
                output_dir,
                raw_ocr=raw,
                pages=normalized_pages,
                blocks=blocks,
                proposals=proposals,
                decisions=decisions,
                applied_diffs=applied_diffs,
                warnings=warnings,
            )
        return PipelineResult(curated_path=curated_path, debug_dir=debug_dir, document=document)
    except Exception as error:
        warnings.append({"type": "pipeline_error", "message": str(error)})
        write_debug_bundle(
            output_dir,
            raw_ocr=raw,
            pages=normalized_pages,
            blocks=blocks,
            proposals=proposals,
            decisions=decisions,
            applied_diffs=applied_diffs,
            warnings=warnings,
        )
        raise
