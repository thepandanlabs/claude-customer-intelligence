# Customer Intelligence & Pitch Suite

**"How to Code with AI using Claude Code"** — a workshop by Pandan Labs.

A 4-hour workshop (or two standalone 2-hour modules) for managers and sales teams who want to build tools with AI — without learning to code.

Attendees build `account`: a CLI that accumulates client interaction history, generates structured account briefs, and drafts tailored proposals from RFPs. Two things a chat tab structurally cannot do: **persistent per-account memory** and a **capability library that improves with every proposal generated**.

---

## Format

| Format | Duration | Who |
|---|---|---|
| Combined | 4h + 15-min break | Any group: run both modules back-to-back |
| Module 1 standalone | 2h | Account Intelligence only — `account add` + `account brief` |
| Module 2 standalone | 2h | Pitch Suite only — `account pitch` + capability library (requires Module 1 prereqs) |

---

## What attendees build

**Module 1 — Account Intelligence**
- `account add <name> <folder>` — ingest emails, call notes, transcripts into a SQLite ledger
- `account brief <name>` — generate a structured markdown brief: last contact, open commitments, key risks
- `account query --open` — list all open commitments across accounts
- `account export` — write `data.json` for `dashboard.html`

**Module 2 — Pitch Suite** (extends Module 1)
- `account pitch --rfp <file>` — generate a tailored proposal draft using account brief + capability library
- Capability library: approved content blocks that grow richer with every proposal

---

## Repository structure

```
claude-customer-intelligence/
├── index.html          # Workshop landing page
├── viewer.html         # Markdown renderer (viewer.html?file=...)
├── days/               # 12 facilitation block files (6 per module)
│   ├── m1-block-*.md   # Module 1 blocks
│   └── m2-block-*.md   # Module 2 blocks
├── resources/          # Reference materials
├── tracks/             # Four post-workshop extension tracks
└── seed/               # The starter repo attendees clone and build on
    ├── PRD.md          # Spec with 5 stubs
    ├── CLAUDE.md       # Extraction + pitch rules (skeleton)
    ├── inbox/          # 4 fictional accounts with interaction histories
    ├── capabilities/   # Fictional company capability library (4 files)
    ├── sample-rfp.txt  # RFP for the pitch exercise
    └── src/account/    # Python CLI stubs
```

---

## Running locally

```bash
git clone https://github.com/thepandanlabs/claude-customer-intelligence.git
cd claude-customer-intelligence
python3 -m http.server 8080
# open http://localhost:8080
```

Requires no build step. Tailwind via CDN. Content files are plain Markdown rendered by `viewer.html`.

---

## Deploying

See [DEPLOY.md](DEPLOY.md) for the full GitHub Pages flow.

Live site: https://thepandanlabs.github.io/claude-customer-intelligence/

---

## Workshop kit

The `seed/` folder is the starter repo attendees clone at the start of the session. It contains:
- A working v0.1 `account` CLI (`account add`, `account brief`, `account list`)
- A PRD with 5 stubs marking what's missing — attendees pick one stub and implement it
- A CLAUDE.md skeleton — attendees write their own extraction rules live in Block 2
- 4 fictional accounts (Acme Software, Globex Consulting, Initech Retail, Umbrella Corp) with realistic interaction histories
- A fictional capability library for a software company called Meridian Systems
- A sample RFP for the pitch exercise

---

From Pandan Labs with ♥
