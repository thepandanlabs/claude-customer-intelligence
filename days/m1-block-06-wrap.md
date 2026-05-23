# Module 1 · Block 6 — Wrap

**Time:** 01:50 – 02:00
**Goal:** Close cleanly. Every attendee names one thing they'll do differently. The room leaves with a shared memory of what it built and why.

<!-- participant-start -->
## Block 6 — What to do

Be ready to share one sentence with the room. No prep needed.

- What's one open commitment from your accounts right now that isn't written down anywhere?
- What rule would you add to `CLAUDE.md` before running this against your real inbox?
<!-- participant-end -->

## The shape

| Time | Activity |
|---|---|
| 01:50 – 01:55 | One-line takeaways from around the room. |
| 01:55 – 01:58 | The three files that mattered. |
| 01:58 – 02:00 | Where to read next. Open Q&A while people finish coffee. |

---

## Takeaways — go around the room

Read aloud:

> *"In one sentence: what's the one thing you're going to do differently the next time you finish a client call?"*

No editorialising. Just listen. Most answers will land in one of three buckets:

- *"I'm going to run the call notes through the tool."*
- *"I'm going to write down the right answer before I check the output."*
- *"I'm going to write a spec before I ask Claude to build anything."*

That's the workshop. If a third of the room says one of those three things, the session worked.

---

## The three files that mattered

Hold this up on screen or printed:

```
PRD.md
CLAUDE.md
accounts.db
```

> *"Everything you did today rotates around these three files.*
>
> *The PRD says what we're building — what commands exist, what they do, what the acceptance criteria are.*
>
> *The CLAUDE.md says how the tool recognises what matters: commitments, competitor mentions, risk signals, sentiment — in plain English, owned by you, not by a developer. If the tool gets something wrong, the fix belongs there.*
>
> *The database is the ledger that accumulates across every interaction you'll ever add — across accounts, across months, queryable any time.*
>
> *You didn't write a single line of code. You wrote the rules. Claude wrote the code. The discipline is in the spec, not the syntax. Steal that for the next tool you need."*

---

## Where to read next

Three things, no more:

1. **Anthropic's official Claude Code Quickstart** — `code.claude.com/docs/en/quickstart`. The canonical getting-started guide. 20 minutes.
2. **Hamel Husain's "Your AI Product Needs Evals"** — `hamel.dev/blog/posts/evals/`. The best 30-minute read on building tools that are verifiably correct, not just impressively fluent. Read before Module 2.
3. **Boris Cherny + Alex Albert, "A conversation on Claude Code"** — YouTube, ~21 minutes. The creator of Claude Code on how he uses it — the Plan Mode workflow in his own words.

That's about 90 minutes of reading and watching. Encourage it before Module 2.

---

## Open Q&A — until coffee runs out

Take any question that didn't fit earlier. Some that will land here:

- **"What about other AI tools — Copilot, Gemini, GPT-4?"** Same principle applies to any AI with tool-use capabilities. The discipline — write the spec, verify the output, accumulate in a ledger — transfers to any platform. Claude Code is the vehicle we used today; the methodology is the asset.
- **"How do I convince my manager or team?"** Show them `account query --open` pulling 7 open commitments across 4 accounts from the last month. Don't argue about AI — show the cross-account query. That's the gap that lands.
- **"How much does this cost?"** Claude Pro ($20/month) covers a tool this size comfortably. `account add` calls Claude once per interaction file — for a team processing 30 interactions a week, that's roughly 30 API calls. Well within Pro limits.
- **"Can I connect this to my real inbox?"** Not in v0.1 — it works from files you export and drop into the inbox folder. Track A (CRM sync) closes that gap: it pulls from Salesforce or HubSpot automatically. That's one of the extension tracks.
- **"What if I want to build something completely different?"** Same loop. Write a PRD for what you want. Write a CLAUDE.md for how the tool should behave. Run `/plan` → `/implement` → verify. The `account` tool was the worked example. Your problem is the next one.

If a question is too large — *"how do we build our entire sales operations on Claude Code?"* — defer to a follow-up conversation. *"That's a project, not a workshop question. Let's talk after."*

---

## The send-off

Read aloud, then stop:

> *"You came in this morning with a chat tab. You're leaving with a CLI that has a ledger, extraction rules for your domain, a verification discipline, and a direction for Monday. The tool is yours. From Pandan Labs — go build something."*

Photos. Done.

---

## Outputs from this block

- Every attendee has spoken one sentence aloud.
- Every attendee leaves with three reading recommendations.
- The room has a shared memory of the three files that anchored the work.

---

[← Back to home](../index.html)
