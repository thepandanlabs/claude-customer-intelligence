"""extract.py — Claude API calls for structured extraction and generation.

Rules:
- All Claude API calls live here. No Claude calls in ledger.py or report.py.
- No Claude calls in tests — tests use fixture data.
- The JSON schema returned by parse_interaction() must not change without
  a corresponding database migration. Ask before changing it.
"""

import json
from pathlib import Path

import anthropic


def parse_interaction(text: str, source_file: str) -> dict:
    """Call Claude to extract structured data from a single interaction file.

    Returns a dict with at minimum:
      {
        "date": "YYYY-MM-DD",          # date of the interaction
        "type": "email|call|meeting",  # interaction type
        "summary": "string",           # 1–2 sentence summary
      }

    After Stub A is implemented, also returns:
      "commitments": [
        {
          "owner": "string",
          "commitment": "string",
          "due_date": "YYYY-MM-DD | TBD | null",
        }
      ]

    After Stub B: also returns "sentiment": "positive|neutral|negative|escalated"
    After Stub C: also returns "competitors_mentioned": ["Workato", ...]
    """
    # TODO: implement
    #   1. Construct the extraction prompt. Extraction rules from CLAUDE.md apply here.
    #   2. Call anthropic.Anthropic().messages.create(...).
    #   3. Parse the JSON response.
    #   4. Return the dict.
    raise NotImplementedError


def generate_brief(account: str, interactions: list[dict]) -> str:
    """Call Claude to generate a markdown account brief.

    The brief must be deterministic for a fixed list of interactions.
    Sort interactions by (date ASC, source_file ASC) before passing here.

    Returns a markdown string.
    """
    # TODO: implement
    #   1. Build a prompt that includes account name and all interaction summaries.
    #   2. Call Claude with instructions from CLAUDE.md.
    #   3. Return the markdown string.
    raise NotImplementedError


def generate_pitch(
    account_brief: str,
    rfp_text: str,
    capabilities_dir: Path,
) -> str:
    """Call Claude to generate a section-by-section proposal draft. (Stub D)

    Args:
        account_brief: markdown brief for the account (from generate_brief or report.py)
        rfp_text: full text of the RFP file
        capabilities_dir: path to the capabilities/ folder

    Returns a markdown string — one section per RFP requirement.
    Flags [CAPABILITY-GAP: <requirement>] for any unmatched requirement.
    """
    # TODO: implement (Stub D)
    raise NotImplementedError
