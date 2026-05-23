# Prerequisites

**Read this before you arrive. Plan 30 minutes of setup at home.**

Two hours in a room is not enough time to debug a broken install. Everyone needs the four things below working *before* walking in.

## 1. A paid Claude subscription

The $20/month Claude Pro plan is enough for this workshop. Monthly billing is fully supported as of May 2026 — annual is optional ($17/month if you prefer to pre-pay).

- Subscribe at `claude.com/pricing` → pick **Pro**.
- Claude Code is included with Pro at no extra cost.
- The free plan will **not** work — Claude Code requires a paid subscription.

For Saudi Arabia specifically: Anthropic officially supports Saudi Arabia for both Claude.ai and the API. No VPN needed. If your card is declined, see the payment notes page.

## 2. Claude Code installed

Two install paths. Pick one. The native installer is the current recommendation.

**Native installer (no Node.js needed):**

```bash
# macOS / Linux / WSL (Windows Subsystem for Linux)
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

The `curl` / `irm` commands download and run the installer automatically — same idea as a web-based setup wizard, just in the terminal.

**npm fallback (if you prefer Node.js):**

```bash
npm install -g @anthropic-ai/claude-code
```

`npm` is the package manager that comes with Node.js — a way to install command-line tools with one command.

If you hit `EACCES` errors on npm (a permission error meaning "this installer doesn't have write access to the system folder"), **do not use `sudo`**. Set up a user-local prefix instead:

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc   # or ~/.zshrc
source ~/.bashrc
```

Then retry.

**Verify it works:**

```bash
claude --version    # should print a version number
claude doctor       # should show green checkmarks
```

Run `claude` once in any folder. You will be prompted to log in via browser. Use your paid Claude account.

## 3. Python 3.11 or higher

The workshop tool is built in Python. Check:

```bash
python --version   # or: python3 --version
```

If you are below 3.11, install via [python.org](https://www.python.org/downloads/), Homebrew (`brew install python@3.12` on macOS — Homebrew is a popular tool installer for macOS), or your operating system's package manager.

## 4. The seed repo cloned and the tool installed

Don't try to clone at the venue on shared Wi-Fi — do this at home.

```bash
git clone https://github.com/thepandanlabs/claude-customer-intelligence
cd claude-customer-intelligence/seed
```

Install the tool and verify it runs:

```bash
uv tool install --editable .   # or: pip install -e .
account --help
```

Then run the tool check:

```bash
account add acme interactions/sample-acme/
account brief acme
```

The first command should process the sample interaction files without error. The second should produce a brief showing last contact date, open commitments, and key contacts. If you see both outputs: you are ready.

The seed folder ships with:

- `PRD.md` — the one-page spec for the account CLI, with two stub sections (Stub D: pitch command, Stub E: capability library).
- `CLAUDE.md` — the extraction rules and pitch rules.
- `.claude/commands/` — the four slash commands (`/prime`, `/plan`, `/implement`, `/verify`).
- `interactions/sample-acme/` and `interactions/sample-globex/` — sample account interaction files.
- `rfp/sample-rfp-globex.txt` — a sample RFP for the pitch exercise.
- `capabilities/` — seed capability library with two pre-filled entries.
- `src/account/` — stub source files (Claude builds the implementation during the workshop).

## Also helpful

- **Git installed.** Windows: install [Git for Windows](https://git-scm.com/download/win) so Claude Code's Bash tool works correctly.
- **A code editor.** VS Code, Cursor, or whatever you already use. Not strictly required — Claude Code edits files for you — but useful for reading the diffs (the change summaries Claude shows as it builds).
- **A real interaction file** (an anonymised email, meeting note, or call record as a `.txt` file) if you want to test the tool on your own account beyond the sample data. Optional — the samples are enough for the exercises.

## Module 2 only? Here is what to check

If you are joining Module 2 without having done Module 1, the tool check above is enough. You do not need an account brief from a previous session — the sample data gives you one to work with.

If you did Module 1 and want to continue with your own accounts: bring your laptop with the repo already open and `account brief <your-account>` running. No extra setup needed.

## Day-of setup

Arrive at 100% battery. Venue power outlets fill up fast. A 2-hour session running Claude Code on Sonnet will drain a laptop to around 30%.

Bring your phone with mobile hotspot ready. Venue Wi-Fi is the single most common failure mode in every workshop we run.

## If something is broken the morning of the workshop

Run `claude doctor` and read the output. If it doesn't fix itself, message the facilitator with the **exact** error text — not a paraphrase. Don't show up with nothing installed; the room has 6–12 people and one facilitator, and one broken laptop can swallow ten minutes from everyone.

[← Back to home](../index.html)
