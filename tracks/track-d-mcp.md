# Track D — MCP + Claude Desktop

**Goal:** Ask Claude Desktop natural-language questions about your accounts and get real answers — not summaries of a document you pasted, but live queries against your actual database. "What's open with Acme this week?" → real results, instantly. "Which accounts have we not contacted in 30 days?" → a list, from the database. "Draft a follow-up for Globex." → a draft seeded from the account brief. A weekend project.

## What changes

Build an MCP server (a small program that runs locally and gives Claude Desktop structured access to tools) that exposes the account database as a set of queryable tools. Claude Desktop calls these tools when you ask questions about your accounts. Four tools: `get_account_brief` (the brief for one account), `query_open_commitments` (all open commitments, optionally filtered by account), `list_inactive_accounts` (accounts not contacted in N days), and `draft_followup` (a draft follow-up email seeded from the account brief).

## What MCP is

MCP stands for Model Context Protocol — an open standard that lets Claude (and other AI assistants) call tools you define on your local machine. Instead of pasting data into the chat, Claude queries your data source directly through a secure local connection. No data leaves your machine.

When Claude Desktop has an MCP server configured, you see it listed under "Available Tools" in the interface. When you ask a question that seems to need that tool, Claude calls it automatically — you don't have to invoke it manually.

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift + Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're building an MCP server that gives Claude Desktop access to the
account intelligence database.

What to build:
1. An MCP server in src/account_mcp/ that:
   - Uses the Python MCP SDK (pip install mcp)
   - Connects to ~/.account-cli/accounts.db (the SQLite database)
   - Exposes four tools:

   Tool 1: get_account_brief
   - Parameters: account_name (required, string)
   - Returns: the formatted account brief for that account — last contact,
     open commitments, key contacts, risks. Same content as `account brief`.
   - If account not found: return "No account named '[name]'. Run
     `account add <name> <folder>` to ingest interactions."

   Tool 2: query_open_commitments
   - Parameters: account_name (optional, string)
   - Returns: all open commitments. If account_name is given: for that
     account only. If omitted: across all accounts, grouped by account,
     sorted by due date ascending (nulls last).

   Tool 3: list_inactive_accounts
   - Parameters: days (optional, integer, default: 30)
   - Returns: accounts where last_contact_date is more than <days> days ago,
     sorted by last_contact_date ascending (longest inactive first).
     Includes: account name, last contact date, days since contact, and
     count of open commitments.

   Tool 4: draft_followup
   - Parameters: account_name (required), context (optional, string — any
     specific topic or commitment to focus on)
   - Returns: a draft follow-up email (plain text). Uses the account brief
     as context. References the most recent open commitment if context is
     not provided. If context is provided: focuses the draft on that topic.
   - Note: this tool generates draft text using the MCP server's access to
     the brief — it does not call Claude again. It uses a fixed template
     with brief data substituted in.

2. A Claude Desktop config snippet (claude_desktop_config.json format)
   that the user can paste to register the server.

MCP server config block (example):
{
  "mcpServers": {
    "account-intelligence": {
      "command": "python",
      "args": ["-m", "account_mcp"],
      "cwd": "/absolute/path/to/claude-customer-intelligence/seed"
    }
  }
}

Constraints:
- The server reads the database — no writes. Read-only.
- If the database doesn't exist: return "No database found at
  ~/.account-cli/accounts.db. Run `account add <name> <folder>` first."
- All tools must return results within 3 seconds on a database with up
  to 500 accounts and 5000 interaction records.
- Server must start and stop cleanly — no zombie processes.
- draft_followup must not hallucinate details not present in the account
  brief. Stick to the template. Leave placeholders ([DATE], [YOUR NAME])
  for the human to fill in.

Plan first. Do not write code yet.
```

## Milestones

1. **MCP server starts without error.** Run `python -m account_mcp` — no errors, process stays alive.
2. **Claude Desktop lists the server under Available Tools.** After pasting the config snippet and restarting Claude Desktop, open the tool list and confirm "account-intelligence" appears.
3. **`get_account_brief` works.** Ask Claude Desktop: "What's the brief for Acme?" — Claude calls the tool, returns results from your actual database.
4. **`query_open_commitments` works.** Ask: "What commitments do I have open with Globex?" — results from the database, not from anything you typed.
5. **`list_inactive_accounts` works.** Ask: "Which accounts have I not contacted in the last 30 days?" — a real list.
6. **`draft_followup` works.** Ask: "Draft a follow-up for Acme." — a draft email using brief data, with clear placeholders.

## Definition of done

- Claude Desktop can answer account questions without any copy-paste.
- All four tools return correct results for a database with at least 5 accounts.
- `draft_followup` output contains no invented facts — only content from the brief, plus placeholders.
- The server exits cleanly when Claude Desktop is closed.
- No database writes happen through the MCP interface.

## Things to watch for

- **Claude Desktop subscription.** MCP tools require Claude Desktop (free download), but using them requires a Claude Pro subscription. The same subscription that covers the workshop covers this track.
- **Config file location.** `claude_desktop_config.json` lives at:
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
  Paste the server block inside the `"mcpServers"` key — don't replace the whole file. If the file doesn't exist yet, create it with the full structure:
  ```json
  {
    "mcpServers": {
      "account-intelligence": { ... }
    }
  }
  ```
- **Absolute paths in config.** The `"cwd"` value must be an absolute path. A relative path will silently fail — the server won't start and Claude Desktop will show no error. If the tool doesn't appear under Available Tools, the path is wrong.
- **MCP SDK version.** Use v1.x of the Python MCP SDK (`pip install mcp>=1.0`). Examples online may be for v0 — the API changed significantly between versions.
- **Read-only discipline.** The `draft_followup` tool generates text from a template — it should not write that draft to the database or to a file. If the user wants to save the draft, they copy it from Claude Desktop. Keeping the MCP server read-only prevents accidental data modification through the chat interface.
- **`draft_followup` scope creep.** If users start asking "draft a proposal" through MCP, the tool will try to comply using only brief data — which is not the same as the full pitch pipeline. Be explicit in the tool description that `draft_followup` produces a follow-up email only, not a proposal. Proposals use `account pitch` from the CLI.

## Going further

Once the four core tools work, natural extensions are:

- **`search_interactions` tool** — full-text search across all interaction history for a keyword or phrase. Useful for: "Did we ever discuss pricing with Globex?" without knowing which account brief to look in.
- **`get_pitch_draft` tool** — connects to the proposals/ folder and returns the most recent pitch draft for an account. Now Claude Desktop can answer: "What did we last propose to Acme?"
- **`flag_at_risk` tool** — a write operation (carefully): marks an account as at-risk in the database. Enables: "Flag Globex as at-risk — CFO is pushing back." Use with explicit write permission in the MCP server config.
- **Multi-account briefing** — ask "Brief me on all accounts I'm meeting this week" and have the tool read calendar context (passed in as a parameter) against the account database. A more advanced workflow, but the tool infrastructure is the same.

## Read next

- **MCP spec home** — `modelcontextprotocol.io`. Read "Concepts" first, then "Python SDK".
- **Python MCP SDK** — `github.com/modelcontextprotocol/python-sdk`. v1.x is current stable as of May 2026.
- **Claude Desktop config docs** — search `claude_desktop_config.json` in the Anthropic documentation for the exact file path and format on your platform.
- **"Building effective agents"** (Anthropic) — the tool-use patterns in this guide describe exactly what happens when Claude Desktop calls your MCP tools. The account intelligence MCP is a direct implementation of the tool-augmented agent pattern.

[← Back to home](../index.html)
