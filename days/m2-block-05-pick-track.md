# Module 2, Block 5 — Full Pipeline Demo + Pick an Extension Track

**Time:** 01:30 – 01:45
**Goal:** The room sees the complete pipeline run end to end. Each attendee picks an extension track to work on independently. 15 minutes.

<!-- participant-start -->
## Block 5 — What to do

Watch the demo. Then pick one extension track.

**After the demo, choose:**

| Track | What it adds | Who it's for |
|---|---|---|
| [Track A — CRM Export](../tracks/track-a-crm-export.md) | `account export --format salesforce` outputs a CSV for Salesforce or HubSpot import | Sales teams who need account intelligence in the CRM, not the CLI |
| [Track B — Email Watch](../tracks/track-b-email-watch.md) | Watches a folder for `.eml` exports and auto-runs `account add` | Anyone who exports email conversations as .eml files |
| [Track C — Slack Watch](../tracks/track-c-slack-watch.md) | Monitors a Slack channel for account mentions and auto-ingests updates | Teams that post meeting notes or deal updates in Slack |
| [Track D — MCP + Claude Desktop](../tracks/track-d-mcp.md) | Natural-language queries: "What's open with Acme this week?" | Anyone who wants to query accounts in plain English from Claude Desktop |

Each track has a starting prompt. Open the track file, copy the prompt, paste it into a fresh Claude Code session with Plan Mode on. The track guides you from there.
<!-- participant-end -->

## Block shape

| Time | Activity |
|---|---|
| 01:30 – 01:42 | **Full pipeline demo.** Facilitator runs end to end, narrating each step. |
| 01:42 – 01:45 | **Pick a track.** Each attendee decides. Brief show-of-hands — who's on what. |

---

## The full pipeline demo (01:30 – 01:42)

Project the screen. Run this live. Narrate every step.

### Step 1 — Ingest

```bash
account add globex interactions/sample-globex/
```

> *"This reads all the interaction files for Globex — emails, meeting notes, call records — and extracts the intelligence into a local database. 30 seconds. No server."*

### Step 2 — Brief

```bash
account brief globex
```

> *"Here's what the tool knows: last contact was April 28th, the procurement lead is Yusuf Al-Hamdan, there are two open commitments — a pricing model revision due May 15th and a technical architecture walk-through scheduled for early June. One risk: Globex's internal champion flagged budget pressure from the CFO in the last call.*
>
> *That risk line came from a meeting note. The tool read it and flagged it as a risk because the CLAUDE.md extraction rule says: 'Any reference to budget pressure, delayed sign-off, or executive-level concern should be categorised as risk.' That rule is 12 words. It produces that result every time."*

### Step 3 — Check open commitments

```bash
account query --open
```

> *"All accounts with open commitments. Across every ingested account. One command instead of five open spreadsheets and a memory test."*

### Step 4 — Pitch

```bash
account pitch globex --rfp rfp/sample-rfp-globex.txt
```

> *"Now watch. It reads the Globex brief. It reads the RFP. It reads every file in capabilities/. It produces a draft.*
>
> *First section — cloud migration. It found our capability file. It cited the Aramco Digital case study — a real project in the evidence field. It mentioned Globex's Q3 deadline from the brief. That sentence was not in the RFP and was not in the capability file — it came from the interaction history.*
>
> *Third section — on-site technical lead. No capability file. The output says: [CAPABILITY-GAP: dedicated on-site technical lead, 60 days]. Correct. We don't have a file for that. If we did, it would be matched. If we don't, it should say so.*
>
> *That flag will be in the draft you send to your proposal team. They'll see it before the client does. That's the pipeline working."*

### Step 5 — Open the output

```bash
open proposals/globex-$(date +%Y-%m-%d).md
```

Or in the editor:

> *"This is the file. A first draft. A sales person without this tool would have spent two to three hours producing something similar — and might have missed the budget risk from the April call, because it was in a note they took six weeks ago.*
>
> *This draft took 90 seconds. The quality depends on: how complete the interaction history is, how precise the CLAUDE.md rules are, and how well-documented the capability library is. All three are yours to own and improve."*

### The pipeline as a sentence

End the demo with this:

> *"Ingest → brief → pitch → verify. That's the pipeline. The data comes from your work. The rules come from your judgment. The draft comes from Claude. The send decision comes from you."*

---

## Pick a track (01:42 – 01:45)

Put the four tracks on screen. One sentence per track:

- **Track A — CRM Export:** You already have CRM workflows. This brings account intelligence into them without copy-paste.
- **Track B — Email Watch:** You export email conversations from Outlook or Gmail. This auto-ingests them when they land in a folder.
- **Track C — Slack Watch:** Your team posts deal updates in Slack. This reads those posts and captures the intelligence automatically.
- **Track D — MCP:** You want to ask questions about your accounts in plain English from Claude Desktop. This makes that work.

Ask for a show of hands — which track is each person picking. Call it out and note it. This is useful to know for troubleshooting: Track D takes the longest to configure; if three people picked D, you may want to check in on them early.

Then say:

> *"Open the track file now. Read the starting prompt. Start a fresh Claude Code session. Plan Mode on. Paste the prompt. You have the rest of the session plus take-home time."*

[← Back to home](../index.html)
