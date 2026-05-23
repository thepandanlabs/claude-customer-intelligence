# Bad Prompt vs. Good Prompt — Preparing for a Client Meeting

This page shows two ways to use AI before an account review. The difference is not which AI tool you use — it's what you give it and what stays around afterwards.

---

## The bad prompt

**What you type into Claude.ai (or any chat tab):**

```
Help me prepare for my Acme meeting tomorrow.
I want to know where we stand on open items.
```

**What you get back:**

> *Here's a preparation checklist for your Acme meeting:*
>
> *1. Review recent communications — check your email thread with the client for any outstanding action items.*
> *2. Confirm the agenda — make sure all participants know what will be discussed.*
> *3. Open items — consider what commitments were made on the last call and whether they've been fulfilled.*
> *4. Next steps — think about what outcomes you want from this meeting.*
>
> *Would you like help drafting specific talking points?*

**What's wrong with that output:**

- It knows nothing about Acme. It generated a generic template that applies to any meeting with any client.
- The three "open items" you actually have — the reference list Sarah owes them, the SLA redline Ahmed is sitting on, the integration concern flagged on the last call — are not in there. They couldn't be. You didn't give them.
- Tomorrow you'll do this again. The chat tab will still know nothing. Every session starts blank. There is no accumulation.

**The structural problem:**

A chat tab has no memory between sessions. Whatever you paste in today is gone when you close the tab. The "preparation" you got required you to already know everything — which is the opposite of what you needed.

---

## The good prompt (with the right setup)

**What you've done first:**

1. Written a `PRD.md` — one page defining what the `account` tool must extract: commitments, risk signals, competitor mentions.
2. Written extraction rules in `CLAUDE.md` — plain English, covering your domain. For example:
   - *"An account team commitment is any sentence where someone on our side promises an action or delivery to the client. Fields: content, owner, deadline."*
   - *"Flag any competitor mentioned by name. Record: competitor name, interaction date."*
3. Run `account add acme-software inbox/acme-software/` — ingested 8 emails, call notes, and meeting transcripts into the ledger.

**What you type into the terminal:**

```bash
account brief acme-software
```

**What you get back, in about 3 seconds:**

```
## Acme Software — Account Brief
Generated: 2026-05-22

**Last contact:** 2026-05-18 (call — integration timeline review)
**Relationship owner:** Sarah Okafor
**Account status:** Active — 8 interactions logged

### Open commitments (account team → client)
- [ ] Send revised SLA terms after legal review — Ahmed — deadline: TBD
- [ ] Provide reference customer list (similar verticals) — Sarah — deadline: TBD
- [ ] Share integration architecture diagram — Sarah — deadline: 2026-05-30

### Key risks
- Integration timeline concern: flagged in 3 of 8 interactions
- No confirmed exec sponsor on client side (flagged 2026-05-18)

### Competitor mentions
- Salesforce: mentioned in 2 interactions (2026-05-04, 2026-05-18)

### Recent interactions
- 2026-05-18: Call — integration timeline, SLA discussion
- 2026-05-04: Email — reference request, follow-up outstanding
- 2026-04-21: Meeting notes — scoping session, 3 open items logged
```

**What's different:**

- It knows Acme specifically — because you ingested the actual interactions.
- The three open commitments are real — they came from reading the source files against your extraction rules.
- The competitor mentions are sourced — Salesforce appears in two real files, not invented.
- This brief still works tomorrow. Next week. If you add a new call note tonight, you run `account add` and the brief updates. The ledger accumulates.

**What you could add now:**

```bash
account query --open
```

Shows open commitments across all accounts — not just Acme. Every promise your team has made, across every client you've added, in one view. No copy-paste, no manual tracking, no memory required.

---

## The difference, stated simply

| | Bad prompt | Good prompt (with tool) |
|---|---|---|
| Knows your client | No — generic output | Yes — ingested real interactions |
| Finds open commitments | No — you have to supply them | Yes — extracted from source files |
| Works next week | No — session forgets | Yes — ledger accumulates |
| Scales to 10 accounts | No | Yes — `account query --open` |
| Needs code knowledge | No | No — you write rules, Claude writes code |

The bad prompt is not bad because Claude is unintelligent. It's bad because you gave it nothing to work with and no way to remember. The good approach is not clever — it's structured. PRD says what to build. CLAUDE.md says how to recognise what matters. The tool accumulates. The brief is always current.

---

[← Back to home](../index.html)
