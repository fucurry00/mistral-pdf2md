"""Contract text shared by future proposal backends."""

PROPOSAL_CONTRACT = """
Return typed edit proposals only. Do not return rewritten document text.
Every proposal must identify a block_id and exact before text from that block.
Summaries, paraphrases, and net-new body prose are forbidden.
""".strip()
