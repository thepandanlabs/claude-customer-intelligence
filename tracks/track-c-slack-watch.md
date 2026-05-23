# Track C — Slack Watch

**Goal:** An agent monitors a Slack channel for account mentions and deal updates. When someone posts a meeting note, a call summary, or a client update in the channel, the agent extracts the account intelligence and runs `account add` automatically — no manual logging. A weekend project.

## What changes

Add a `account watch-slack` command that runs an agent loop: poll a Slack channel, detect new messages containing account-relevant content, extract the intelligence via the existing pipeline, add it to the correct account's database, and post a structured reply to the thread confirming what was captured. Three parts: the Slack connector (reads messages), the account matcher (identifies which account the message refers to), and the extraction trigger (runs `account add` on the message text).

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift + Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're adding a Slack watch agent to the account tool.

What to add:
1. A `account watch-slack` command that:
   - Polls a configured Slack channel every 60 seconds
   - Detects messages that look like account updates (heuristic: message
     length > 200 characters, or contains keywords like "met with", "call with",
     "committed", "follow up", "next step", "they said", "risk", "opportunity",
     or any known account name from the local account database)
   - For each matching message:
     a. Identifies the account: scan message text for account names from the
        database; if multiple match, pick the most frequently mentioned; if
        none match, flag as UNMATCHED
     b. Writes the message text to a temp file and runs
        `account add <account-name> <temp-file>`
     c. Posts a structured reply in the Slack thread confirming what was
        captured (see reply format below)
   - Marks processed messages so it does not re-process on the next poll cycle
     (store processed message timestamps in ~/.account-cli/slack-processed.json)

2. A `account watch-slack --setup` sub-command that:
   - Prompts for a Slack bot token and the channel ID to watch
   - Writes them to ~/.account-cli/slack-config.json (not tracked by git)
   - Posts a test message to the channel to confirm the connection works
   - Prints the required bot scopes for the user to verify

Slack reply format (block message):
- Header: "Account intelligence captured"
- Line 1: Account: [account name] (or UNMATCHED — please tag an account name)
- Line 2: Captured: [brief summary of what was extracted — 1 sentence]
- Line 3: Run `account brief <name>` to see the updated brief
- If nothing matched the heuristic: no reply (silent pass — don't spam the channel)

Slack config (from ~/.account-cli/slack-config.json):
- bot_token — Slack bot token (starts with xoxb-)
- channel_id — the channel to watch
- poll_interval_seconds — how often to check (default: 60)

Constraints:
- Bot token must not appear in any file tracked by git.
- If Slack is unreachable, log the error and retry on next poll — do not crash.
- `account watch-slack` is a long-running process. Ctrl+C should exit cleanly.
- Log each event to ~/.account-cli/slack-watch-log.jsonl:
  timestamp, message_ts, account_matched (or UNMATCHED), extracted_items_count,
  error if any.
- Do not re-process messages already in the processed list.
- Detection heuristic: prefer false negatives over false positives. It is
  better to miss an update than to flood threads with extraction replies on
  casual messages.

Plan first. Do not write code yet.
```

## Milestones

1. **`account watch-slack --setup` connects successfully.** Bot posts a test message to the channel. You see it in Slack.
2. **Bot detects and replies to one account update.** Post a message like: "Just got off a call with Acme — Yusuf confirmed they're extending the contract but need pricing revised before June 30th. He flagged the CFO still needs to sign off." Within 60 seconds, the bot replies in the thread. `account brief acme` shows the new commitment.
3. **Unmatched messages are logged, not replied to.** Post a casual message ("lunch at 1?"). Confirm the bot does not reply. Confirm the log shows the message was evaluated and skipped.
4. **Idempotency holds.** The bot does not reply twice to a message it has already processed.

## Definition of done

- `account watch-slack` runs without error and polls on schedule.
- An account update message produces a structured thread reply within 90 seconds.
- The account database is updated correctly — `account brief <name>` shows the new interaction.
- The bot does not reply to casual messages (false-positive rate is low in the first 10 messages).
- Ctrl+C exits cleanly — no traceback, no zombie process.
- `~/.account-cli/slack-watch-log.jsonl` has a valid record for each evaluated message.

## Things to watch for

- **Slack bot scopes.** Your bot needs: `channels:history` (to read messages), `chat:write` (to post replies), and either `channels:join` or be manually added to the channel. Missing scopes produce `not_in_channel` or `missing_scope` errors from the Slack API — read the error response carefully, it tells you exactly which scope is missing.
- **Socket Mode vs polling.** The starting prompt uses polling via the Slack Web API (simpler, no public URL needed). Slack also supports Socket Mode — a persistent WebSocket connection that delivers events in real time without polling. Socket Mode requires the `connections:write` scope and the `websockets-client` Python package, but removes the 60-second delay. If your team wants faster responses, switch to Socket Mode after the basic polling version works.
- **Account name detection.** The heuristic scans for account names from the database. If an account is named "Acme Corp" but people write "Acme" in Slack, the match may fail. The tool should match partial names — check that the account matcher compares normalised lowercase strings and handles common shortenings.
- **Rate limits.** The Slack Web API allows roughly 1 request per second on most endpoints. Polling every 60 seconds on one channel is well within limits. Don't reduce the poll interval below 10 seconds.
- **Message edits and deletions.** The polling approach reads new messages since the last check. Edited messages use the same timestamp as the original — if someone edits a message after processing, the bot won't re-process it (by design). Deleted messages may cause API errors if you try to post a reply — add error handling for deleted message threads.
- **Thread replies vs top-level messages.** The detection heuristic should check both top-level messages and thread replies. A deal update often appears as a reply to an earlier message. Decide whether to watch threads in the starting prompt configuration — the default Slack API call (`conversations.history`) returns top-level messages only; add `conversations.replies` calls if you need threads.

## Read next

- **Slack Bolt for Python** — the official Slack SDK. Search "Slack Bolt Python" in Slack's developer documentation. Much simpler than raw Web API calls, and handles token storage, event routing, and Socket Mode out of the box.
- **Slack app creation** — `api.slack.com/apps`. You need to create a Slack app, add the required bot scopes, install it to your workspace, and copy the bot token. The setup wizard takes about 10 minutes.
- **"Building effective agents"** (Anthropic) — the evaluator-optimiser pattern applies directly to this track: the agent evaluates each message (is this an account update?) then routes to the optimiser (which account? what was captured?). Link in Further Reading.

[← Back to home](../index.html)
