"""Objective two-layer gate for all proposed content mutations."""

from __future__ import annotations

import re
from collections import Counter
from difflib import SequenceMatcher

from pdf_curator.models import (
    Block,
    EditProposal,
    EditTrigger,
    GateDecision,
    GateStatus,
    MutationType,
)

_WORD_RE = re.compile(r"[\w\u3040-\u30ff\u3400-\u9fff]+", re.UNICODE)
_LIST_MARKER_RE = re.compile(r"(?m)^\s*(?:[-*+] |\d+[.)] )")
_PROVENANCE_RE = re.compile(
    r"^(?:Source: PDF p\.\d+(?:-\d+)?|<!-- PDF p\.\d+ -->)\s*$"
)


def _words(text: str) -> list[str]:
    return [token.casefold() for token in _WORD_RE.findall(text)]


def _levenshtein(left: str, right: str) -> int:
    if len(left) < len(right):
        left, right = right, left
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, 1):
        current = [left_index]
        for right_index, right_char in enumerate(right, 1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[right_index] + 1,
                    previous[right_index - 1] + (left_char != right_char),
                )
            )
        previous = current
    return previous[-1]


def diff_stats(before: str, after: str) -> dict[str, object]:
    before_words = Counter(_words(before))
    after_words = Counter(_words(after))
    return {
        "edit_distance": _levenshtein(before, after),
        "similarity": round(SequenceMatcher(None, before, after).ratio(), 4),
        "word_count_before": sum(before_words.values()),
        "word_count_after": sum(after_words.values()),
        "words_added": sorted((after_words - before_words).elements()),
        "words_removed": sorted((before_words - after_words).elements()),
        "hunk_size": max(len(before), len(after)),
    }


def _decision(
    status: GateStatus,
    proposal: EditProposal,
    reason: str,
    stats: dict[str, object],
) -> GateDecision:
    return GateDecision(status=status, proposal=proposal, reason=reason, diff_stats=stats)


def _is_local_ocr_fix(before: str, after: str) -> bool:
    before_words = _words(before)
    after_words = _words(after)
    if len(before_words) != len(after_words) or not before_words:
        return False
    changed_pairs = [
        (left, right)
        for left, right in zip(before_words, after_words, strict=True)
        if left != right
    ]
    return bool(changed_pairs) and len(changed_pairs) <= 2 and all(
        _levenshtein(left, right) <= max(1, min(2, len(left) // 4 + 1))
        and SequenceMatcher(None, left, right).ratio() >= 0.7
        for left, right in changed_pairs
    )


def evaluate_proposal(proposal: EditProposal, block: Block | None) -> GateDecision:
    if block is None:
        return _decision(GateStatus.REJECTED, proposal, "referenced block does not exist", {})

    if proposal.type is MutationType.PROVENANCE_ANNOTATION:
        stats = diff_stats(proposal.before, proposal.after)
        if (
            proposal.trigger is EditTrigger.EDIT
            and proposal.scope == "system"
            and _PROVENANCE_RE.fullmatch(proposal.after)
        ):
            return _decision(
                GateStatus.ACCEPTED,
                proposal,
                "system provenance annotation derived from page tags",
                stats,
            )
        return _decision(
            GateStatus.REJECTED, proposal, "invalid system provenance annotation", stats
        )

    if not proposal.before or proposal.before not in block.text:
        return _decision(
            GateStatus.REJECTED,
            proposal,
            "before text is absent from the referenced source block",
            {},
        )

    stats = diff_stats(proposal.before, proposal.after)
    mutation = proposal.type

    if mutation in {
        MutationType.HEADER_FOOTER_REMOVE,
        MutationType.PAGE_NUMBER_REMOVE,
    }:
        evidence = block.attrs.get("prepass_evidence")
        valid = (
            proposal.trigger is EditTrigger.AUTO_PREPASS
            and proposal.after == ""
            and isinstance(evidence, dict)
            and evidence.get("mutation") == mutation.value
        )
        return _decision(
            GateStatus.ACCEPTED if valid else GateStatus.REJECTED,
            proposal,
            "validated deterministic pre-pass evidence"
            if valid
            else "missing deterministic pre-pass evidence",
            stats,
        )
    if mutation is MutationType.CONTENT_ADD:
        return _decision(GateStatus.REJECTED, proposal, "net-new body prose is forbidden", stats)
    if mutation in {MutationType.SUMMARIZE, MutationType.PARAPHRASE}:
        return _decision(
            GateStatus.REJECTED, proposal, f"{mutation.value} is outside the v1 contract", stats
        )
    if mutation in {MutationType.PARAGRAPH_RESTRUCTURE, MutationType.CONTENT_DELETE}:
        return _decision(
            GateStatus.ISOLATED,
            proposal,
            "grey-zone restructure or unpatterned deletion requires review",
            stats,
        )
    if mutation is MutationType.LINEBREAK_REPAIR:
        same_content = (
            re.sub(r"\s+", "", proposal.before)
            == re.sub(r"\s+", "", proposal.after)
            and Counter(_words(proposal.before)) == Counter(_words(proposal.after))
        )
        same_content = same_content and proposal.trigger is EditTrigger.EDIT
        status = GateStatus.ACCEPTED if same_content else GateStatus.REJECTED
        reason = "whitespace-only repair" if same_content else "content changed"
        return _decision(status, proposal, reason, stats)
    if mutation is MutationType.LIST_RESTORE:
        before = _LIST_MARKER_RE.sub("", proposal.before).strip()
        after = _LIST_MARKER_RE.sub("", proposal.after).strip()
        marker_only = (
            before == after
            and proposal.before != proposal.after
            and proposal.trigger is EditTrigger.EDIT
        )
        status = GateStatus.ACCEPTED if marker_only else GateStatus.REJECTED
        reason = "list markers only" if marker_only else "list content changed"
        return _decision(status, proposal, reason, stats)
    if mutation in {MutationType.OCR_CHAR_FIX, MutationType.BULK_OCR_FIX}:
        local = _is_local_ocr_fix(proposal.before, proposal.after)
        if mutation is MutationType.BULK_OCR_FIX:
            local = (
                local
                and proposal.trigger is EditTrigger.REPLACE_ALL
                and block.text.count(proposal.before) >= 1
            )
        else:
            local = local and proposal.trigger is EditTrigger.EDIT
        status = GateStatus.ACCEPTED if local else GateStatus.ISOLATED
        reason = (
            "local OCR character repair"
            if local
            else "OCR edit exceeds local threshold"
        )
        return _decision(status, proposal, reason, stats)
    if mutation is MutationType.HEADING_LEVEL_NORMALIZE:
        before_match = re.match(r"^(#{1,6})\s+(.+)$", proposal.before, re.DOTALL)
        after_match = re.match(r"^(#{1,6})\s+(.+)$", proposal.after, re.DOTALL)
        safe = (
            proposal.trigger is EditTrigger.EDIT
            and before_match is not None
            and after_match is not None
            and before_match.group(2) == after_match.group(2)
        )
        return _decision(
            GateStatus.ACCEPTED if safe else GateStatus.REJECTED,
            proposal,
            "heading markers only" if safe else "heading content changed",
            stats,
        )
    return _decision(GateStatus.REJECTED, proposal, "unsupported mutation", stats)
