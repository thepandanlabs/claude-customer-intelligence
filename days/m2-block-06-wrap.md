# Module 2, Block 6 — Wrap

**Time:** 01:45 – 02:00
**Goal:** Land the three claims. Answer deferred questions. Leave every attendee with a clear next action. 15 minutes.

<!-- participant-start -->
## Block 6 — What to do

You're done building for today. Three things before you leave:

1. Confirm your proposal draft is saved in `proposals/` and opens correctly
2. Write down one CLAUDE.md rule you want to add when you use this on real accounts — not the sample data, your actual account
3. Write down one capability you want to add to your library before you next write a proposal

These are your take-home actions. They don't require Claude Code. They're writing tasks — plain English.
<!-- participant-end -->

## Block shape

| Time | Activity |
|---|---|
| 01:45 – 01:52 | **Land the three claims.** One minute per claim. |
| 01:52 – 01:57 | **Q&A.** Open floor. |
| 01:57 – 02:00 | **Next action and close.** |

---

## The three claims (01:45 – 01:52)

### Claim 1

> *"A proposal that starts from scratch every time is a proposal that forgets what worked before. The capability library accumulates your best pitch language."*

Say it, then say this:

> *"You built a library today. It has a handful of entries. That's not failure — that's the start. Every deal you win, add the evidence. Every proposal section that landed well, refine the capability description. Six months from now, the library knows more than any single person on your team does about how to pitch what you do."*

### Claim 2

> *"The brief seeds the pitch. Account history isn't decoration — it's how you write a proposal that references the client's actual situation."*

Point to something specific from the demo:

> *"In the demo, the draft referenced Globex's Q3 deadline and the CFO budget pressure. That came from a meeting note from six weeks ago. Not because the tool is smart — because someone captured it. The brief made it searchable. The pitch tool read the brief. The output was personalised because the capture was specific.*
>
> *Generic proposals lose. They lose because the client reads them and thinks: they didn't listen. The brief is proof that you listened. The pitch tool is what makes the proof readable."*

### Claim 3

> *"The tool can be wrong. Hand-check whether it matched RFP requirements to real capabilities, or invented something. That check is the eval."*

> *"You ran the verify step. Some of you found a gap the tool didn't flag. Some of you found a claim the tool made that wasn't in the capability file. That finding is the point of the exercise — not a failure of the tool.*
>
> *The eval is permanent. You don't do it once and trust the tool forever. You do it before every proposal goes out. It takes five minutes when the proposal is 90% right. It saves hours when a client calls to ask about a capability you don't have."*

---

## Q&A (01:52 – 01:57)

Common questions. Answers below.

**"What happens if the RFP is 40 pages?"**
The tool reads the full text. Quality of matching depends on clarity of the requirements section. If the RFP mixes requirements with background narrative: add a CLAUDE.md rule that tells the tool to focus on sections headed "Requirements", "Scope of Work", or "Technical Specifications". You can also pre-process — extract just the requirements section manually, save it as a `.txt`, and pass that to `account pitch`.

**"Can I use this for bids we lost — to understand what capability gaps cost us?"**
Yes. Run `account pitch <lost-account> --rfp <past-rfp>`. Look at the gaps. If the tool flags something that was in the RFP and you didn't have a capability for it at the time: that's a capability investment conversation. Add the flag to your library as an evidence target — "we need two case studies in X before we can bid this type of work again."

**"What if two capability files match the same RFP requirement?"**
The tool picks the closest match by keyword and description relevance. If you want to control this: add a `priority` field to the capability YAML and update the CLAUDE.md rule to prefer higher-priority entries. Or write a rule: "When multiple capabilities match, prefer the one with more evidence entries." The spec is yours.

**"Should the capability library be in the repo or separate?"**
The seed puts it in the repo for portability. In practice, many teams prefer a shared capability library that multiple people can update — not tied to one person's laptop. Once the structure is working, consider moving `capabilities/` to a shared folder or a separate git repo that multiple account folders can reference. That's an extension beyond today's scope — but the format supports it.

**"Can multiple people use the same account database?"**
Yes, if the SQLite file is on shared storage (a network drive, Dropbox, a shared server). The tool doesn't lock the file between runs. Concurrent writes from two people simultaneously may cause errors — treat it as one writer at a time, or add explicit locking if your team is large.

---

## Next action and close (01:57 – 02:00)

Ask every person to say one sentence:

> *"What is one thing you will do with this tool in the next two weeks?"*

Go around the room. Examples:

- "I'll ingest the last three months of Acme interactions and run a brief."
- "I'll add five capability entries from our last proposal deck."
- "I'll run `account pitch` on the RFP we're currently bidding."
- "I'll set up the CRM export so my team sees briefs in Salesforce."

Close with this:

> *"Everything you built today is yours. The capability library is yours. The CLAUDE.md rules are yours. The tool doesn't improve on its own — but every proposal you run through it, every rule you write, every capability you document makes the next one faster and more specific.*
>
> *That is the discipline. Not the AI. The AI executes the discipline you define."*

[← Back to home](../index.html)
