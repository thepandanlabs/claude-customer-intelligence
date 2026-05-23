# Module 1 · Block 5 — Pick Your Track

**Time:** 01:40 – 01:50
**Goal:** Every attendee leaves with a clear next step — one extension track chosen, a starting prompt read, and a direction for the evening or weekend.

<!-- participant-start -->
## Block 5 — What to do

10 minutes. Pick one track and start reading.

1. Choose by what you'd actually use in your work:
   - **Module 2** — Build the pitch generator (`account pitch --rfp <file>`)
   - **Track A** — CRM sync (pull account history automatically from Salesforce or HubSpot)
   - **Track B** — Email drafting (generate follow-up emails from the brief)
   - **Track C** — Dashboard (share a live HTML dashboard with your manager or team)
2. Open the track page from the workshop home
3. Enable Plan Mode (Shift + Tab twice) and run `/plan` with the track's starting prompt
4. Read the plan that comes back — don't implement yet
<!-- participant-end -->

## The options

Each one extends the `account` tool you built today. Pick by what you'd actually use — not by what sounds most impressive.

| Option | What it is | What it unlocks | Time at home |
|---|---|---|---|
| **Module 2** | Build `account pitch --rfp <file>`. Takes an RFP (request for proposal — a formal document from a potential client asking you to bid for work) and your capability library, and generates a structured proposal draft. | Turn RFP response from a two-day scramble to a starting point in 20 minutes. | Full 2-hour session. |
| **Track A — CRM sync** | Pull account history automatically from Salesforce or HubSpot into the ledger. No manual export. | Zero data entry. New interaction logged in CRM → brief updates automatically. | A weekend. |
| **Track B — Email drafting** | Generate a draft follow-up email from the account brief — next steps, open commitments, tone matched to the relationship. | Never start a follow-up from scratch again. Edit the draft, don't write from zero. | An evening. |
| **Track C — Dashboard** | `account export` already writes `data.json`. This track builds a shareable `dashboard.html` with filters by account, owner, and commitment status. | Share pipeline health with your manager without building a slide deck. | An evening. |

Full details for each option are in the [extension tracks section](../index.html#tracks) of the home page.

---

## What to say in this block

Read aloud:

> *"You ran the tool, you saw the gaps, you closed one, you verified it. Same loop, every time — spec, build, verify. The four options are not difficulty levels. They're four different shapes of useful. Pick the one you'd actually open on Monday morning."*

Then:

> *"In the next five minutes: open the option page, read the brief, copy the starting prompt, and paste it into a fresh Claude Code session in your repo. Enable Plan Mode. Run `/plan`. Read what comes back. Don't implement — just read the plan. That plan is a 5-minute preview of what an evening of building looks like."*

---

## What attendees do

1. Open the track or Module 2 page from the home grid.
2. Read the one-paragraph brief.
3. Copy the starting prompt.
4. Open a fresh Claude session in their repo.
5. Enable Plan Mode (Shift + Tab twice).
6. Paste the prompt and run it.
7. Read the plan.

Stop there. Don't approve. Don't implement. The plan is the takeaway — not the code.

---

## Common questions in this block

- **"Can I do Module 2 now?"** You can start it — the plan will come back in a few minutes. But the full build is a 2-hour session. Read the plan, then schedule time for the full module.
- **"Which track is fastest?"** Track B (email drafting) and Track C (dashboard) are each an evening. Track A (CRM sync) depends on your CRM's API access — could be an evening or a weekend. Module 2 is the full next session.
- **"What if I want to build something completely different?"** Same loop. Write a PRD for your idea. Write a CLAUDE.md with the rules for your domain. Run `/plan` → `/implement` → verify. The `account` tool was the worked example, not the limit. The methodology transfers to any tool you'd want to build.
- **"Do I need to know how to code to do these at home?"** No. You need to know what you want and how to write it down. The PRD and CLAUDE.md carry the knowledge; Claude Code carries the execution.

---

## Facilitator note — read the room

If two minutes in, half the room is still deciding without committing, lean in:

> *"Pick the one that solves the problem you felt most acutely in the last month. The plan is free — you can read it and throw it away."*

If the room is moving fast and everyone's on a track by 01:43, use the remaining time for Q&A you parked from Block 1 or Block 2.

If someone chooses Module 2 and wants to run `/plan` on it now: let them. The plan for Module 2 is a useful preview of what's coming and it reinforces that the same loop applies at the next level.

---

## Outputs from this block

- Every attendee has read a starting prompt for one track or module.
- Every attendee has seen a plan generated by Claude for that next step.
- Every attendee leaves with a concrete next action — not *"explore Claude Code more."*

---

[← Back to home](../index.html)
