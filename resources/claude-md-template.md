# CLAUDE.md — Account Intelligence & Pitch Suite

Copy this file to the root of your seed repo and rename it `CLAUDE.md`. Fill in the blank spaces with rules that match your accounts, your industry, and your company's commitments. Keep it under 100 lines — a memo, not a manual.

---

```markdown
# CLAUDE.md — Account Intelligence & Pitch Suite

## Stack

- Language: Python 3.11+
- Database: SQLite via the built-in `sqlite3` module (a lightweight database
  that lives as a single file on your machine — no server needed)
- Package manager: uv (or pip as fallback)
- CLI framework: Click
- Data format: YAML for capability files, Markdown for briefs and proposals

## Layout

```
claude-customer-intelligence/seed/
├── CLAUDE.md               ← you are here
├── PRD.md                  ← the spec; stubs D and E are the pitch features
├── capabilities/           ← one .yaml file per company capability
├── interactions/           ← raw account interaction files (emails, notes)
├── rfp/                    ← RFP files to pitch against
├── proposals/              ← generated proposal drafts (output)
├── src/account/            ← source code
└── .claude/commands/       ← /prime /plan /implement /verify
```

## Conventions

- Capability IDs use lowercase kebab-case: `managed-cloud-migration`, `regulatory-advisory`
- Account names match the folder name under `interactions/` and the name used in `account add`
- Proposal output files are named: `proposals/<account-name>-<YYYY-MM-DD>.md`
- All dates stored as ISO 8601: `YYYY-MM-DD`. Never store relative dates ("next week", "after Eid")
- Commitments have two states: `open` or `closed`. Nothing else.
- A risk is any statement indicating delay, hesitation, competing priority, or executive-level concern

## Extraction rules

Rules that govern what Claude captures from interaction files (emails, meeting notes, call records).

- Capture WHO made each commitment, not just what was committed. If no clear owner
  is named, use the person's job title or function and flag [UNCLEAR-OWNER].
  Example: "The procurement team will review by end of month" → owner: Procurement Team [UNCLEAR-OWNER]

<!-- Add your extraction rules below. Write in plain English — one rule per bullet.
     Rules you might consider:
     - How should the tool handle commitments made by your own team vs by the client?
     - What counts as a risk in your industry or sales context?
     - Are there confidentiality constraints (e.g., do not log pricing discussions, internal deal terms)?
     - What date formats appear in your interactions that need normalising?
-->

-

-

-

-

## Pitch rules

Rules that govern how Claude generates proposal content using the account brief and capability library.

- Only match RFP requirements to capabilities that exist in the capabilities/ folder.
  Never invent a capability. If no matching capability file exists: output
  [CAPABILITY-GAP: <requirement summary>]. Do not draft a section for a capability
  the company does not have documented.

<!-- Add your pitch rules below. Write in plain English — one rule per bullet.
     Rules you might consider:
     - How should the tool handle partial matches (a capability that partially covers an RFP requirement)?
     - What tone or language constraints apply to proposals from your company?
     - Are there requirements you should always flag for human review before submitting?
-->

-

-

-
```

---

## How to use this template

**Section 1 — Extraction rules** governs what the tool captures when it reads interaction files. The pre-filled example enforces owner attribution — one of the most common gaps in account intelligence. Add rules for anything the tool currently gets wrong or misses entirely.

**Section 2 — Pitch rules** governs what the tool claims when it writes proposals. The pre-filled example enforces the [CAPABILITY-GAP] flag — the most important guard against a proposal that promises something you cannot deliver. Add rules for edge cases you discover in the verify step.

**When to add a rule:**
- The tool produces output you would not sign off on
- A verify check finds an invented claim or a missed requirement
- A new account type or RFP format introduces behaviour the existing rules don't cover

**When to remove a rule:**
- It has been in the file for three months and has never changed the output
- It describes something so obvious the tool gets right without being told

**Keep it under 100 lines.** A CLAUDE.md that takes more than two minutes to read is a CLAUDE.md that Claude will partially ignore. Short, specific rules outperform long, comprehensive ones.

[← Back to home](../index.html)
