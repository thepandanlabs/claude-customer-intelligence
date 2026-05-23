# Seed Repo — What's in the Folder and Why

When you clone the workshop repo, you get a working starting point. You're not building from scratch — you're extending something that already runs. This page explains what's in each folder and what role it plays.

---

## The folder structure

```
account-seed-repo/
│
├── PRD.md                      ← The spec for what the tool must do
├── CLAUDE.md                   ← The extraction rules Claude reads on every session
│
├── inbox/                      ← Fictional client interaction files
│   ├── acme-software/          ← 8 files: emails, call notes, meeting transcripts
│   ├── globex-consulting/      ← 6 files: mostly call notes and follow-up emails
│   ├── initech-retail/         ← 4 files: two calls, two email chains
│   └── umbrella-corp/          ← 3 files: new prospect, early stage
│
├── capabilities/               ← Descriptions of what your company offers
│   ├── enterprise-integration.md
│   ├── managed-services.md
│   ├── professional-services.md
│   └── support-tiers.md
│
├── .claude/
│   └── commands/               ← Slash commands: /prime, /plan, /implement, /verify
│
├── account.py                  ← The CLI entry point (already written)
├── accounts.db                 ← The SQLite database (created on first run)
└── dashboard.html              ← Static HTML dashboard, reads from data.json
```

---

## PRD.md — the spec

PRD stands for Product Requirements Document (see Glossary). This one is one page — intentionally short.

It defines:

- What the `account` CLI must do (commands: `add`, `brief`, `query`, `list`, `export`, `pitch`)
- What it must not do (no CRM sync, no email sending — those are extension tracks)
- How you know when it's working (acceptance criteria — five checkable conditions)
- Five stub sections — clearly marked gaps that v0.1 does not yet fill

The stub sections are the raw material for Block 3. Each stub has a comment block explaining what's missing and what to add. You fill in the requirement; Claude builds to it.

**Stubs in v0.1:**

- **Stub A — Commitment extraction:** The tool logs interactions but doesn't extract structured commitments (who promised what by when). The open commitments section of every brief is currently empty.
- **Stub B — Sentiment per interaction:** No signal on whether a client conversation was positive, neutral, or negative. Brief can't flag declining trends.
- **Stub C — Competitive signal detection:** No tagging of competitor mentions. A client who names a rival three times in two months is a risk signal the brief currently misses.
- **Stub D — `account pitch` generation:** The pitch command is scaffolded — it accepts a file argument — but returns a placeholder. Module 2 builds this out fully.
- **Stub E — Capability library:** The `capabilities/` folder exists, but the tool doesn't yet read from it when generating briefs or pitches.

---

## CLAUDE.md — the extraction rules

Claude Code reads `CLAUDE.md` automatically at the start of every session. Think of it as the standing instructions you'd give a new analyst on their first week — except Claude re-reads it every single time, so the rules always apply.

The skeleton ships with four sections filled in:

- **Stack:** Python 3.11+, SQLite (via the `sqlite3` standard library), the Anthropic Python SDK. No external databases, no web frameworks.
- **Layout:** Which files do what. Where new code should go. What not to move.
- **Conventions:** How to name things, how to handle errors, what to print vs. what to log.
- **Determinism rules:** How to make the tool behave the same way every time — most importantly, how to skip files already processed.

And one section with one pre-written example rule:

- **Extraction rules:** One example showing the format. Space below it for you to add your own in Block 2.

The extraction rules section is where the workshop happens. The rules you write there — about commitments, competitor mentions, risk signals, sentiment — are what drive the tool's behaviour. Claude doesn't guess. It reads what you wrote and builds to it.

---

## inbox/ — the fictional accounts

Four fictional accounts, each with a realistic mix of file types. All files are plain text — no special format required. The tool reads whatever you drop in.

**Acme Software** (8 files)

A mid-size software company in an active sales cycle. The interactions include:

- 2026-02-10: Initial discovery call notes
- 2026-02-28: Follow-up email chain (3 emails)
- 2026-03-15: Technical scoping meeting notes
- 2026-04-21: Scoping session notes (Sarah commits to reference list; Ahmed commits to SLA review)
- 2026-05-04: Email — reference request follow-up (Salesforce mentioned)
- 2026-05-10: Internal handoff note
- 2026-05-18: Call notes — integration timeline review (Salesforce mentioned again; exec sponsor concern)

This is the primary verification account. The facilitator pre-labelled the correct commitments, risks, and competitor mentions from these files. Your tool's output is checked against that label in Block 4.

**Globex Consulting** (6 files)

An established consulting firm. Mostly in the renewal and upsell stage. Mix of call notes and short follow-up emails. One interaction flags a budget concern.

**Initech Retail** (4 files)

A retail company in the evaluation phase. Two recorded calls and two email chains. The interactions show increasing interest but no confirmed next step.

**Umbrella Corp** (3 files)

A new prospect — three introductory interactions only. The brief will be short; risk section will flag "early stage, limited data."

---

## capabilities/ — what your company offers

Four plain-text files describing service areas. These are written in the voice of someone who knows the product — not marketing copy, but clear descriptions of what you do and for whom.

- `enterprise-integration.md` — connecting the company's tools to large enterprise IT environments
- `managed-services.md` — ongoing management of deployed systems
- `professional-services.md` — implementation, training, and onboarding
- `support-tiers.md` — what each support level includes and who it's for

In v0.1, the tool doesn't read these. Stub E and Module 2 both build on this folder. When `account pitch --rfp <file>` is implemented in Module 2, it reads the relevant capability files and uses them to write the proposal.

---

## .claude/commands/ — the slash commands

Four files in plain text. Each one is a reusable prompt you can run inside Claude Code by typing its name with a `/` prefix.

| File | Command | What it does |
|---|---|---|
| `prime.md` | `/prime` | Reads `PRD.md` and `CLAUDE.md` and reads back what it understood. If the readback is wrong, fix the writing — not the prompt. |
| `plan.md` | `/plan` | Produces a written, numbered plan. Does not write code. Waits for your approval. |
| `implement.md` | `/implement` | Executes the approved plan step by step. |
| `verify.md` | `/verify` | Runs the verification checklist against the hand-labelled Acme answer and reports gaps. |

These are not magic. They are text files you can open, read, and edit. If you want `/prime` to do something slightly different, open `.claude/commands/prime.md` and change it.

---

## dashboard.html — the shared view

A static HTML file that reads from `data.json` (written by `account export`). No server required — open it directly in a browser.

It shows:

- All accounts in the ledger
- Open commitments, filterable by owner and account
- Interaction count per account
- (Module 2 only) Pitch status per account

Run `account export` first, then open `dashboard.html`. That's all it takes.

---

## What's already working in v0.1

- `account add <name> <folder>` — ingests all text files in the folder, logs each interaction, skips files already processed
- `account list` — shows all accounts with interaction counts and last contact date
- `account brief <name>` — generates a brief with last contact and interaction history (open commitments section is empty until Stub A is built)
- `account query --open` — returns open commitments (empty until Stub A is built)
- `account export` — writes `data.json` for `dashboard.html`

---

[← Back to home](../index.html)
