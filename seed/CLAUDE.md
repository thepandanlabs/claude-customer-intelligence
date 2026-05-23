# CLAUDE.md — account CLI

## What this is

A local Python CLI that ingests client emails, call notes, and transcripts into a SQLite ledger, then surfaces account briefs, open commitments, and proposal drafts via Claude. Read PRD.md before planning any implementation work.

## Stack

- Python 3.11+
- Click for the CLI interface (handles subcommands and flags)
- SQLite via the stdlib `sqlite3` module (no ORM — no SQLAlchemy, no Peewee)
- `anthropic` Python SDK for extraction and generation
- `pytest` for tests
- `uv` for dependency management

## Layout

```
src/account/
  cli.py          — Click entry points (add, brief, query, list, export, pitch, capability)
  ledger.py       — SQLite read/write, deduplication, schema migration
  extract.py      — Claude API calls for extraction and generation
  report.py       — Markdown brief and JSON export generation
migrations/
  001_init.sql    — Database schema
tests/
  test_idempotency.py
inbox/
  acme-software/
  globex-consulting/
  initech-retail/
  umbrella-corp/
capabilities/
  delivery.txt
  integrations.txt
  security.txt
  support.txt
```

## Conventions

- Data output to stdout. Logs and progress messages to stderr.
- Exit code 0 on success. Exit code 1 on user error (bad account name, missing file). Exit code 2 on unexpected runtime error.
- Deduplication: SHA-256 hash of the source file bytes. Same file processed twice = zero new rows the second time.
- Never call Claude inside a test. Tests use fixture data and stub functions.
- No network calls in `ledger.py` or `report.py`. Those modules are pure SQLite and string rendering.
- Type hints on every function signature.

## Determinism

Sort interactions by `(date ASC, source_file ASC)` everywhere — in briefs, in query output, in exports. No wall-clock timestamps in output. Running `account brief` twice on the same ledger must produce identical output.

## Extraction rules

These rules tell Claude what to extract from each interaction file, and how to handle edge cases. Write them in plain English — you don't need to know Python to own this section. If the tool gets something wrong, the fix belongs here, not in the prompt code.

One rule is pre-written as an example of the format:

- **Capture WHO made each commitment, not just what was committed.** If the owner is not explicitly named, use their job title or company role (e.g., "Acme CFO") and flag `[UNCLEAR-OWNER]`. Never leave the owner field blank.

```
# Add your extraction rules below. Plain English. Claude will follow them.

# Rule 1:

# Rule 2:

# Rule 3:

# Rule 4:
```

## Competitive signals

Competitors to flag when mentioned in interactions:

- Workato
- Zapier
- MuleSoft
- Boomi
- ServiceNow (when mentioned as a competing workflow platform, not as an integration target)
- Microsoft Power Automate

```
# Add competitors below, one per line.
```

## Pitch rules

These rules govern how `account pitch` generates proposals. They apply after capability matching, before the draft is written.

One rule is pre-written as an example:

- **Only reference capabilities found in the `capabilities/` folder. Never invent a capability.** If an RFP requirement has no matching capability, output `[CAPABILITY-GAP: <requirement summary>]` and continue — do not skip the requirement silently.

```
# Add pitch rules below.

# Rule 1:

# Rule 2:

# Rule 3:
```

## When to ask — never assume

- Any new dependency (add to `pyproject.toml` and tell me why)
- Any change to the database schema (update `migrations/001_init.sql` and confirm before applying)
- Any change to the JSON schema returned by `extract.py` (existing records in the ledger use the old schema — migration needed)
- Anything that would change what existing account briefs look like
