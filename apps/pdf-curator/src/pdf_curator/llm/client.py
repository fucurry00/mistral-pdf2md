"""Interface for future typed proposal providers."""

from __future__ import annotations

from typing import Protocol

from pdf_curator.models import Block, EditProposal


class ProposalClient(Protocol):
    def propose(self, blocks: list[Block]) -> list[EditProposal]: ...


class NoOpProposalClient:
    def propose(self, blocks: list[Block]) -> list[EditProposal]:
        return []
