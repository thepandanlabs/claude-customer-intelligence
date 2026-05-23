# Module 2, Block 1 — Recap & Setup

**Time:** 00:00 – 00:10
**Goal:** Everyone is oriented, the tool is running on their laptop, and the session objective is clear. Ten minutes. No new concepts yet.

<!-- participant-start -->
## Block 1 — What to do

Get the tool running before anything else starts.

**If you did Module 1:**
1. Open your terminal in the `claude-customer-intelligence/seed` folder
2. Run `account brief <your-account-name>` — confirm the brief still appears
3. Confirm you have a `capabilities/` folder: `ls capabilities/`

**If you are joining fresh today:**
1. Clone the seed repo:
   ```bash
   git clone https://github.com/thepandanlabs/claude-customer-intelligence
   cd claude-customer-intelligence/seed
   ```
2. Install and verify:
   ```bash
   uv tool install --editable .
   account --help
   ```
3. Run a quick demo ingest on the sample data:
   ```bash
   account add acme interactions/sample-acme/
   account brief acme
   ```

Either path ends in the same place: a working `account` CLI and a `capabilities/` folder you can see. If you don't have both, raise your hand now — don't wait.
<!-- participant-end -->

## Block shape

| Time | Activity |
|---|---|
| 00:00 – 00:03 | **30-second orientation.** What this module builds and why. |
| 00:03 – 00:08 | **Demo or recap.** Demo `account add` + `account brief` if standalone; 5-min recap of Module 1 output if sequential. |
| 00:08 – 00:10 | **Tool check.** Everyone confirms `account --help` and `ls capabilities/` both work. |

---

## The 30-second orientation (00:00 – 00:03)

Say this, then stop:

> *"Module 1 was about understanding accounts — ingesting interactions, tracking commitments, knowing where things stand. Module 2 is about using that understanding to win business. We're building a pitch tool: one command that reads an RFP, reads your account history, reads your capability library, and drafts a tailored proposal.*
>
> *By the end of this session: you type `account pitch --rfp rfp-globex.pdf` and a structured first draft comes back. It references the client's actual situation. It uses language that already worked for you before. It flags where you don't have a capability to match what they're asking for.*
>
> *That last part — the flag — is why this tool is trustworthy. It doesn't invent things."*

---

## If standalone: the `account add` demo (00:03 – 00:08)

Run this live, projecting the screen. Narrate every command.

```bash
account add acme interactions/sample-acme/
```

> *"This reads the interaction files in that folder — emails, meeting notes, call logs — and extracts the account intelligence into a local database. No server. A file on your machine.*
>
> *Now: the brief."*

```bash
account brief acme
```

> *"Last contact, open commitments, key contacts, risks. This is what the pitch tool reads before it touches the RFP. The brief is the context. Without it, a proposal is generic. With it, it can say: 'As discussed in your March board meeting, your procurement deadline is Q3 — here is how our delivery schedule maps to that.'"*

> *"We haven't written that. Claude wrote it from the brief. Your job today is to build the part that does this reliably."*

---

## If after Module 1: the 5-minute recap (00:03 – 00:08)

Go fast. This is a memory jog, not a lesson.

- `account add` — ingests interaction files, extracts intelligence to SQLite
- `account brief` — generates a markdown summary: last contact, commitments, risks
- `account query --open` — shows open commitments across all accounts
- `CLAUDE.md` — the extraction rules that govern what Claude captures and how it's labelled

Ask the room:

> *"What did you notice about the output? Where did it get something wrong?"*

Take two answers. Park the thread. That's what today's verify block addresses.

---

## Tool check (00:08 – 00:10)

Every attendee runs:

```bash
account --help
ls capabilities/
```

`capabilities/` should exist and contain at least the seed entries (`.yaml` files — plain text capability definitions). If it's empty or missing:

```bash
account capability list
```

If that errors: they did not install the full seed. Walk them through:

```bash
cd claude-customer-intelligence/seed
uv tool install --editable .
```

Two minutes to resolve. If it takes longer, park it — they can pair with a neighbour for the next block and catch up.

[← Back to home](../index.html)
