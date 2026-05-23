"""report.py — Markdown brief and JSON export generation.

Rules:
- No network calls in this module.
- No Claude API calls in this module.
- All output must be deterministic for a fixed set of interactions.
  Sort by (date ASC, source_file ASC) before rendering.
"""

import json
from datetime import date


def render_brief(account: str, interactions: list[dict]) -> str:
    """Render a markdown account brief from a list of interaction dicts.

    The brief includes:
      - Account name and summary stats (last contact date, interaction count)
      - Interaction history (one line per interaction, sorted by date)
      - Open Commitments section (populated after Stub A)
      - Key Risks section
      - Sentiment Trend section (populated after Stub B)
      - Competitive Signals section (populated after Stub C)

    Returns a markdown string. Must produce identical output for identical input.
    """
    # TODO: implement
    #   1. Sort interactions by (date ASC, source_file ASC) — defensive sort.
    #   2. Compute: last contact date, interaction count.
    #   3. Build markdown sections.
    #   4. Return the full markdown string.
    raise NotImplementedError


def render_json(interactions: list[dict]) -> str:
    """Render interactions as a JSON string suitable for dashboard.html.

    Returns a JSON string. The schema must match what dashboard.html expects.
    Sort interactions by (date ASC, source_file ASC) before serialising.
    """
    # TODO: implement
    #   1. Sort interactions by (date ASC, source_file ASC).
    #   2. Build the output structure: {"generated": "YYYY-MM-DD", "interactions": [...]}
    #   3. Return json.dumps(output, indent=2).
    raise NotImplementedError
