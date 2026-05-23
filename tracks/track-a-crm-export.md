# Track A — CRM Export

**Goal:** `account export --format salesforce` outputs a CSV that imports directly into Salesforce or HubSpot — account name, last contact date, open commitments, risk flags, key contacts. Your account intelligence lives in the CLI, but your sales team works in the CRM. This closes the gap without copy-paste. An evening of work.

## What changes

Add an `--format` option to `account export` that maps the SQLite account data to the field structure Salesforce and HubSpot expect for contact and account records. Two parts: a field mapper (translates the account brief fields to CRM column names) and a CSV writer (produces a file you can import directly from the CRM's import wizard).

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift + Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're adding CRM export to the account tool.

What to add:
1. Extend `account export` with a `--format` option that accepts
   "salesforce" or "hubspot".

2. For `--format salesforce`: output a CSV with these columns:
   - Account Name (maps to: account name in our database)
   - Account Owner (maps to: key_contacts[0].name if available, else "")
   - Last Activity Date (maps to: last_contact_date, formatted YYYY-MM-DD)
   - Description (maps to: a one-paragraph summary of open commitments and risks,
     max 255 characters — Salesforce field limit)
   - Account Source (hardcoded: "account-cli")
   - Custom field: Open_Commitments__c (maps to: count of open commitments)
   - Custom field: Risk_Flag__c (maps to: "HIGH" if any risk entries exist, else "NONE")

3. For `--format hubspot`: output a CSV with these columns:
   - Company name (maps to: account name)
   - Company owner (maps to: key_contacts[0].name if available, else "")
   - Last contacted (maps to: last_contact_date, formatted YYYY-MM-DD)
   - Description (maps to: same summary as Salesforce, max 255 characters)
   - Open commitments (maps to: count of open commitments — use HubSpot
     custom property name open_commitments)
   - Risk flag (maps to: "HIGH" or "NONE" — use HubSpot custom property
     name risk_flag)

4. Output file: `exports/crm-<format>-<date>.csv`
   Confirm path printed to stdout after export.

Constraints:
- Export all accounts by default. Support `--account <name>` to export
  one account only.
- Description field must be truncated at the character limit — no silent
  overflow. Append "…" if truncated.
- If an account has no brief data yet (never run `account brief`): skip
  with a warning, don't fail silently.
- The CSV must open correctly in Excel and Google Sheets without encoding
  issues — use UTF-8 with BOM (byte order mark) for Windows compatibility.

Plan first. Do not write code yet.
```

## Milestones

1. **`account export --format salesforce` produces a valid CSV.** Open it in Excel or Google Sheets — no encoding errors, columns match the field list.
2. **Import succeeds in Salesforce (or HubSpot sandbox).** Use the CRM's import wizard. Map the columns. Confirm records appear correctly.
3. **Multi-account export works.** Run on all accounts. Confirm one row per account, no duplicates.
4. **Single-account export works.** `account export --format salesforce --account acme` — one row, Acme only.

## Definition of done

- CSV imports into Salesforce or HubSpot without mapping errors.
- Description field is within character limits — no truncation errors on import.
- Risk flags appear correctly on records where risks exist.
- Accounts with no brief are skipped with a warning printed to the terminal — not a crash.
- The export file is saved to `exports/` and the path is printed after the run.

## Things to watch for

- **Custom fields must exist first.** `Open_Commitments__c` and `Risk_Flag__c` in Salesforce, and their HubSpot equivalents, need to be created in the CRM before import. Use the CRM's field manager to add them as number and text fields respectively. Importing a CSV with unrecognised column headers won't fail — the columns are just silently ignored.
- **Salesforce record types.** Salesforce distinguishes between Leads, Contacts, and Accounts. The export targets Account records. If your org uses Leads instead, the column names differ. Adjust the `--format salesforce` mapper to match your CRM setup.
- **HubSpot property names are lowercase with underscores.** Unlike Salesforce's `__c` suffix convention, HubSpot uses lowercase snake_case for custom properties. If the import fails with "property not found" errors, the property name in the CSV header doesn't match the property name in HubSpot. Check both.
- **UTF-8 BOM.** Windows Excel opens UTF-8 files incorrectly unless the file starts with a byte-order mark (`﻿`). The starting prompt includes this — don't remove it.
- **One row per account, not one row per commitment.** The CRM import expects one record per account. If an account has five open commitments, those go into the Description and Open_Commitments__c fields — not five rows.

## Read next

- **Salesforce Data Import Wizard** — search "Data Import Wizard" in Salesforce Help. The wizard handles up to 50,000 records and provides column mapping before committing.
- **HubSpot import documentation** — search "Import records" in HubSpot Knowledge Base. Step-by-step for CSV imports with custom properties.
- **Python `csv` module** — `docs.python.org/3/library/csv.html`. The standard library CSV writer handles encoding, quoting, and newlines correctly — don't write CSV manually with string concatenation.

[← Back to home](../index.html)
