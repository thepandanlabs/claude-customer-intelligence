# Glossary — Plain-Language Definitions

Every term used in this workshop, defined for non-technical readers. No assumed knowledge. Use this as a reference during any block.

---

## Workshop-specific terms

**PRD (Product Requirements Document)**
A short spec — usually one page — that says what the tool must do, what it must not do, and how you know when it's done. Think of it as the brief you hand a contractor before building work starts. Claude reads it on every turn. Without it, Claude guesses.

**CLAUDE.md**
A plain-text instruction file that lives in your project folder. Claude reads it automatically at the start of every session. It contains your rules: what to extract, how to recognise commitments, what signals to flag, what never to invent. Think of it as the onboarding memo for a new analyst — except Claude re-reads it on every turn, so your rules always apply.

**Account ledger**
The database file (`accounts.db`) that accumulates every interaction you process. Unlike a chat session that forgets when you close the tab, the ledger is permanent. Add an email today, a call note next week, a meeting transcript next month — the ledger grows and every query reflects the full history. The brief you generate in six months is built from everything you ever added, not just what you can remember.

**Brief**
The structured summary that `account brief <name>` generates. It covers: last contact date, relationship owner, open commitments (things the account team has promised the client), key risks, competitor mentions, and recent interaction history. The brief is generated fresh each time you run it — always based on the current state of the ledger, not cached from last week.

**Commitment (client-facing)**
In this workshop, a commitment is something the *account team* promised the *client* — a deliverable, a follow-up, a piece of information, a deadline. It is distinct from a decision (which is internal — something your organisation agreed to do internally). A commitment involves two parties: you made a promise to someone outside your organisation, and they're waiting for it. Open commitments are the most important thing the tool tracks, because they're the ones that damage relationships if missed.

**Capability library**
The `capabilities/` folder — four plain-text files describing what your organisation offers (enterprise integration, managed services, professional services, support tiers). In v0.1, the tool doesn't read from it. Stub E and Module 2 use it: when generating a pitch or proposal, the tool reads the relevant capability files and includes them in the response.

**RFP (Request for Proposal)**
A formal document a potential client sends when they want to buy something. It describes what they need, the timeline, the selection criteria, and often the budget range. Responding to an RFP — writing a proposal that addresses every requirement, frames your capabilities correctly, and sounds like you understand their problem — is typically a multi-day task. Module 2 builds `account pitch --rfp <file>`, which takes the RFP and the account brief and generates a structured starting draft.

**Pipeline**
The set of client accounts currently in active sales conversations — not yet customers, but progressing through discussions. In the context of this tool, pipeline accounts are the ones where `account brief` is most valuable: they're live, time-sensitive, and have open commitments that need tracking.

**Eval (evaluation)**
A saved test case. Three parts: (1) an input you prepared, (2) the correct output you labelled by hand, (3) a comparison. If the output matches your label, the test passes. If not, it fails. The Block 4 verification is an eval: you read the Acme Software files by hand, wrote down the correct commitments and risks, then checked whether the tool found them. Business translation: evals are the difference between "the demo worked" and "it works every time."

**Golden file**
The "correct answer" for a test — a file you labelled by hand, containing exactly what the tool should output for a given input. Future runs are compared against it. If the tool changes its output, you find out immediately rather than six months later when a client says "you promised us that."

**Deterministic**
A fancy word for "same input → same output, always." The account tool is deterministic: the same set of interaction files always produces the same brief. This is what makes the tool trustworthy over time — you can run it tomorrow and know it will give you the same answer as today, assuming no new files were added.

**Acceptance criteria**
The specific, checkable conditions in the PRD that define when the tool is "done." Example: *"Running `account add inbox/acme-software/` twice adds zero new records the second time."* Either it does that or it doesn't. No ambiguity, no judgment call.

**Schema**
The shape of the data — the list of fields a record contains and what type each is. A commitment schema might be: content (text), owner (text), deadline (date or "TBD"), status (open/closed). Claude needs to know the schema before it extracts data; otherwise it invents one, and you get inconsistent output across accounts.

**Idempotent / Idempotency**
An operation is idempotent if you can run it multiple times and get the same result as running it once. `account add inbox/acme-software/` is idempotent: running it a second time adds zero new records and reports all 8 files skipped. A chat interface has no memory between sessions, so it can't guarantee this. A proper database tool can.

---

## Claude Code concepts

**Plan Mode**
A special Claude Code mode where Claude can only *read and plan* — it cannot write files or run commands. You turn it on with **Shift + Tab** (twice). Claude produces a numbered plan; you review it, push back on anything wrong, then approve. Only then does Claude start building. Think of it as "talk before touching anything."

**Auto-accept mode**
The opposite of Plan Mode. Claude runs through its plan and makes changes without stopping after each step. You switch to this after approving the plan, so Claude can execute without asking for permission at every step.

**Agentic loop**
The cycle Claude Code runs on every turn: read your context files → act through tools → show you what it did → wait for your input. It is not a chatbot that just answers questions. It reads, acts, and pauses for review.

**Tool (in Claude Code)**
A capability Claude Code can use: Read a file, Edit a file, run a Bash command, search the codebase. Each tool call is visible to you before it runs. In Plan Mode, Edit and Bash are disabled — Claude can only Read and Search.

**Context window**
The amount of text Claude can "see" at once in a single session. Think of it as working memory. If your CLAUDE.md, PRD, and conversation history together fill the window, older parts get pushed out. This is why a short, focused CLAUDE.md works better than a long one — every line competes for the same limited attention.

**Subagent**
A separate Claude session with a narrower brief and its own fresh context. Used for isolated tasks where you want clean, unbiased attention.

---

## Software terms you'll encounter

**CLI (Command Line Interface)**
A program you control by typing commands in a terminal instead of clicking buttons. The `account` tool is a CLI: you type `account brief acme-software` and it runs. CLIs can be automated, piped together, and scheduled in ways that a UI with buttons cannot.

**Terminal**
The black (or dark) window where you type commands. On Mac: open Spotlight (Cmd+Space), type "Terminal," press Enter. On Windows: search for "PowerShell" or "Command Prompt." If you can open one and type `ls` (Mac/Linux) or `dir` (Windows), you're ready for this workshop.

**SQLite**
A lightweight database that lives as a single file on your machine — no server, no login, no installation beyond Python. The account ledger (`accounts.db`) is a SQLite database. You can query it, back it up by copying the file, and carry it on a USB stick. It's the right choice for a tool one person runs on their own laptop.

**Python**
The programming language the `account` tool is written in. You do not need to know Python to use or extend the tool — Claude writes Python based on the rules you write in plain English. Python 3.11 or higher is required to run it.

**API (Application Programming Interface)**
A way for two software programs to talk to each other. When `account add` processes a file, it sends the file content to the Claude API and receives a structured response back. Think of it as a telephone line between your tool and Claude's brain.

**MCP (Model Context Protocol)**
An open standard for connecting AI models to external tools and data sources. An MCP server exposes capabilities that any MCP-compatible AI client (Claude Desktop, Cursor, etc.) can call. Extension Track A uses MCP to connect the `account` tool to Claude Desktop — so you can ask Claude directly: *"What's open on the Acme account?"* and it queries the real ledger.

**Exit code**
The number a program sends back to the terminal when it finishes. `0` means success. Any other number means something went wrong. Automated tools read exit codes to know whether to proceed or alert someone.

**Static HTML**
A web page that runs entirely in your browser with no server. `dashboard.html` is static HTML — you open it by double-clicking the file. No login, no hosting, no server required. It reads from `data.json` (written by `account export`) and displays your pipeline data.

---

*Anything missing? Something still confusing? The facilitator notes have contact details.*

[← Back to home](../index.html)
