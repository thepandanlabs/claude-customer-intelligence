# account CLI — Product Requirements Document

## What it is

A local Python CLI that ingests client emails, call notes, and transcripts into a SQLite ledger, then surfaces account briefs, open commitments, and proposal drafts via Claude. It gives a sales team a single place to track every client interaction and never start a proposal from scratch.

## Why it exists

Client history lives in email threads and call notes that nobody has time to re-read before a meeting. The AI chat window has no memory of what was promised last quarter. Proposals get written without knowing what the client already told you they care about. The result: reps walk into meetings cold, miss commitments, and send proposals that don't match what the client actually said.

## In scope (v0.1)

1. `account add <name> <folder>` — read every `.txt` file in the folder, extract structured interaction records via Claude, write to ledger, skip files already processed (SHA-256 dedup).
2. `account list` — print all known accounts to stdout.
3. `account brief <name>` — produce a markdown brief for the named account: last contact date, total interaction count, open commitments (stub), key risks.
4. `account query [--open] [--account <name>]` — query commitments across all accounts or for a named account; `--open` filters to unresolved only. (Commitments table is a stub in v0.1 — the flag is wired up but returns empty until Stub A is implemented.)
5. `account export [--account <name>] [--output PATH]` — write a `data.json` file loadable by `dashboard.html`. If `--account` is given, export that account only; otherwise export all.

## Out of scope (v0.1)

- Web UI or hosted dashboard (dashboard.html is a static file opened locally)
- Real-time sync or email server integration (reads exported `.txt` files only)
- Mobile client
- Audio transcription
- Multi-user auth or cloud storage
- Automatic parsing of `.eml`, `.msg`, or PDF formats

## Acceptance criteria

- [ ] `account add acme inbox/acme-software/` processes all `.txt` files in the folder and writes one row per file to the interactions table.
- [ ] Running `account add acme inbox/acme-software/` a second time adds zero rows and reports how many files were skipped.
- [ ] `account brief acme` produces a markdown file that includes: last contact date, total interaction count, and a "Key Risks" section.
- [ ] `account list` prints at least the accounts that have been ingested.
- [ ] `account export --account acme` writes `data.json` that can be opened by `dashboard.html` without errors.
- [ ] `pytest tests/` is green.
- [ ] `--help` is informative on every subcommand.

---

## Stub A — Commitment Extraction

v0.1 records that interactions happened. Stub A extracts WHO committed to WHAT and by WHEN from each interaction.

Add a `commitments` table with columns: `id`, `account`, `source_file`, `owner`, `commitment`, `due_date`, `resolved` (boolean, default false).

Update `extract.py` to return a second JSON array alongside the interaction record — a list of commitments found in each file.

`account query --open` should list all rows where `resolved = false`, sorted by `due_date ASC`.

`account query --account <name> --open` filters to one account.

`account brief` should include an "Open Commitments" section once this stub is implemented.

---

## Stub B — Sentiment Tracking

Tag each interaction as one of: `positive`, `neutral`, `negative`, `escalated` — based on tone and language in the interaction text.

Add a `sentiment` column to the `interactions` table. Update `extract.py` to return a `sentiment` field alongside the interaction record.

`account brief` should include a "Sentiment Trend" section showing how sentiment has shifted across the interaction history (e.g., started positive, turned neutral after negotiation).

A single interaction tagged `escalated` should be surfaced prominently in the brief regardless of recency.

---

## Stub C — Competitive Signals

Flag interactions that mention named competitors by name. Competitors to track are listed in `CLAUDE.md` under "Competitive signals."

Add a `competitors_mentioned` column to the `interactions` table (comma-separated list, or empty string).

Update `extract.py` to return a `competitors_mentioned` field.

`account brief` should surface any competitive mentions in a "Competitive Signals" section, including which competitor and which interaction it appeared in.

---

## Stub D — Pitch Generation

Implement `account pitch --rfp <file> [--account <name>]`.

Steps:
1. Read the account brief for context (what the client cares about, open commitments, sentiment, competitive signals).
2. Read all files from the `capabilities/` folder.
3. Parse the RFP file to extract each stated requirement.
4. For each requirement, find the best matching capability. If no match exists, flag `[CAPABILITY-GAP]` and note what capability is missing.
5. Generate a section-by-section proposal draft as a markdown file. Each section maps to one RFP requirement.

The proposal must only reference capabilities found in the `capabilities/` folder. Never invent a capability. The account context (what the client said they care about) must influence how capabilities are framed.

---

## Stub E — Capability Library Management

Implement `account capability add <file>` and `account capability list`.

Currently capabilities are plain `.txt` files in the `capabilities/` folder. Stub E moves them into SQLite so they can be queried, versioned, and referenced by source file.

`account capability add <file>` reads the file, extracts a structured capability record (name, description, category, keywords), and writes it to a `capabilities` table.

`account capability list` prints all capabilities in the table.

`account pitch` (Stub D) should query the `capabilities` table when it is available, falling back to the flat files if the table is empty.
