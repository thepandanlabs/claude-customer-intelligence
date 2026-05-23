# Track B — Email Watch

**Goal:** A script watches a folder for `.eml` files (the format Outlook and Gmail use when you export an email conversation). When a new file appears, it auto-runs `account add` on the email. No manual copy-paste. No forgetting to log the conversation. An evening of work.

## What changes

Add a `watch-email` script that monitors a designated folder for new `.eml` files. When one appears: extract the sender, recipient, subject, date, and body from the email; match it to an account; run `account add` with the extracted text as an interaction; log what happened. Three parts: the folder watcher (detects new files), the email parser (reads `.eml` format), and the account matcher (decides which account the email belongs to).

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift + Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're adding an email watch script to the account tool.

What to add:
1. A script `scripts/watch-email.py` that:
   - Watches a folder for new .eml files (folder path from config, see below)
   - When a new .eml file appears:
     a. Parses the email: extract From, To, Subject, Date, and plain-text body
        (use Python's built-in `email` library — no external dependencies)
     b. Determines the account: look for the email domain in
        ~/.account-cli/email-accounts.json (a JSON file mapping domains to
        account names, e.g. {"acme.com": "acme", "globex.sa": "globex"})
     c. If the domain matches a known account: write the email content to a
        temp .txt file and run `account add <account-name> <temp-file>`
     d. If the domain is unknown: log the email as UNMATCHED with the From
        address and subject — do not fail silently
     e. Move the processed .eml file to a `processed/` subfolder inside the
        watch folder — don't leave it in the inbox or delete it

2. A `watch-email --setup` sub-command that:
   - Prompts for the watch folder path
   - Creates ~/.account-cli/email-accounts.json with a placeholder entry
     if it doesn't exist
   - Prints instructions for adding domain-to-account mappings
   - Verifies the watch folder is readable

3. A `watch-email --add-account <domain> <account-name>` sub-command that:
   - Adds one entry to ~/.account-cli/email-accounts.json
   - Prints a confirmation

Watch config (from ~/.account-cli/watch-config.json):
- watch_folder — absolute path to the folder to monitor
- poll_interval_seconds — how often to check for new files (default: 30)
- processed_subfolder — name of the subfolder for processed files (default: "processed")

Constraints:
- Use Python's built-in `email` library for .eml parsing. No pip packages
  required for this feature beyond what the account tool already uses.
- If the .eml file is malformed (not a valid email format): log the error
  with the filename and skip. Do not crash the watcher.
- The watcher is a long-running process. Ctrl+C should exit cleanly.
- Log every event to ~/.account-cli/email-watch-log.jsonl:
  timestamp, filename, account_matched (or UNMATCHED), success boolean,
  error if any.
- Processed files move to processed/ — never delete originals.

Plan first. Do not write code yet.
```

## Milestones

1. **`watch-email --setup` completes without error.** Config files created. Watch folder confirmed readable.
2. **`watch-email --add-account acme.com acme` adds the mapping.** Confirm by opening `~/.account-cli/email-accounts.json`.
3. **One .eml file processed correctly.** Export a real email from Outlook or Gmail as `.eml`. Drop it into the watch folder. Within 30 seconds, `account brief <account-name>` shows the interaction.
4. **Unmatched domain is logged, not crashed.** Drop a `.eml` from an unknown domain. Confirm the log entry appears and the watcher keeps running.
5. **Processed file moved.** After step 3, confirm the `.eml` is in the `processed/` subfolder, not still in the watch folder.

## Definition of done

- New `.eml` files in the watch folder are ingested within one poll cycle.
- Known domains are matched to accounts automatically.
- Unknown domains are logged with enough information to add them manually.
- Ctrl+C exits cleanly — no traceback, no zombie process.
- `~/.account-cli/email-watch-log.jsonl` has a valid record for every processed file.
- Original `.eml` files are preserved in `processed/` — never deleted.

## How to export a .eml file

**Outlook (Windows and Mac):** Select an email → drag it to the desktop (or a folder). Outlook saves it as `.msg` on Windows and `.eml` on Mac. On Windows, use File → Save As and choose "Outlook Message Format (.msg)" — note this is different from `.eml`. To get true `.eml` from Outlook on Windows, use the "Save as" option in webmail (Outlook.com → … menu → Save) or use Outlook's export feature with "Text Only" then rename.

**Gmail:** Open the email → three-dot menu (top right) → Download message. Gmail saves as `.eml` directly.

**Apple Mail:** File → Save As → choose Format: Raw Message Source. Saves as `.eml`.

## Things to watch for

- **`.msg` vs `.eml`.** Outlook on Windows often saves as `.msg`, not `.eml`. The Python `email` library does not read `.msg` files — they use a proprietary Microsoft format. If your team uses Outlook on Windows, the script may need a separate `.msg` handler or you may need to convert first. The simplest workaround: use Outlook webmail to download as `.eml`, or forward to a Gmail account and download from there.
- **Multipart emails.** Most emails have both a plain-text and an HTML version. The parser should prefer plain-text (simpler, less noise) and fall back to HTML if plain-text is missing. The prompt specifies "plain-text body" — make sure the implementation strips HTML tags before passing to `account add`.
- **Email threads.** A single `.eml` file may contain a long quoted thread. The parser will pass the full thread text to `account add`. The CLAUDE.md extraction rules will handle most of it — but if the extraction is noisy (capturing old content as new commitments), add a rule: "For email threads, extract commitments and contacts from the most recent message only (the top of the thread)."
- **Large attachments.** `.eml` files with embedded images or attachments can be large. The body extraction should skip non-text attachments — don't try to parse PDFs or images attached to the email.
- **Poll vs filesystem events.** The prompt uses polling (check every N seconds). On macOS and Linux, `watchdog` (a Python library) can provide event-driven file detection (instant, no poll delay) — but requires `pip install watchdog`. The polling approach needs no extra dependencies and is reliable enough for most use cases.

## Read next

- **Python `email` library** — `docs.python.org/3/library/email.html`. The standard library module for parsing `.eml` files. The `email.policy.default` policy handles modern email formats correctly.
- **Python `watchdog` library** — `pypi.org/project/watchdog/`. For event-driven file watching (no polling delay). Optional for this track but useful if your team exports emails frequently.
- **Gmail filters + auto-export** — Gmail does not natively auto-export emails to a folder. A workaround: use Google Apps Script to export matching emails to Google Drive, then sync the Drive folder locally.

[← Back to home](../index.html)
