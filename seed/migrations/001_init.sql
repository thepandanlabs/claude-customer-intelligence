-- migrations/001_init.sql
-- Initial schema for the account CLI ledger.
-- Applied once at startup by ledger.ensure_schema().
-- Do not modify this file after deployment — create a new migration instead.


-- accounts: one row per known account name.
-- Populated automatically when the first interaction is ingested for an account.
CREATE TABLE IF NOT EXISTS accounts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,
    created_at  TEXT    NOT NULL DEFAULT (date('now'))
);


-- interactions: one row per ingested source file.
-- Deduplication key: sha256 (SHA-256 hex digest of source file bytes).
-- If sha256 already exists, the file is skipped — no duplicate rows.
CREATE TABLE IF NOT EXISTS interactions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    account         TEXT    NOT NULL REFERENCES accounts(name),
    date            TEXT    NOT NULL,   -- YYYY-MM-DD (extracted from file by Claude)
    type            TEXT    NOT NULL,   -- 'email' | 'call' | 'meeting'
    source_file     TEXT    NOT NULL,   -- original filename (basename)
    sha256          TEXT    NOT NULL UNIQUE,
    raw_text        TEXT    NOT NULL,   -- full content of the source file

    -- Stub B: sentiment (NULL until Stub B is implemented)
    sentiment       TEXT,              -- 'positive' | 'neutral' | 'negative' | 'escalated'

    -- Stub C: competitors mentioned (comma-separated, empty string if none)
    competitors_mentioned TEXT NOT NULL DEFAULT '',

    ingested_at     TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_interactions_account
    ON interactions (account, date ASC, source_file ASC);

CREATE INDEX IF NOT EXISTS idx_interactions_sha256
    ON interactions (sha256);


-- commitments: extracted from interactions by Claude. (Stub A)
-- Empty until Stub A is implemented.
-- One row per commitment found in a source file.
CREATE TABLE IF NOT EXISTS commitments (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    account     TEXT    NOT NULL REFERENCES accounts(name),
    source_file TEXT    NOT NULL,      -- matches interactions.source_file
    owner       TEXT    NOT NULL,      -- name or role of the person who committed
    commitment  TEXT    NOT NULL,      -- what was committed to
    due_date    TEXT,                  -- YYYY-MM-DD | 'TBD' | NULL
    resolved    INTEGER NOT NULL DEFAULT 0,  -- 0 = open, 1 = resolved (boolean)
    created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_commitments_account_open
    ON commitments (account, resolved, due_date ASC);


-- capabilities: managed by 'account capability add'. (Stub E)
-- Empty until Stub E is implemented. Pitch (Stub D) falls back to flat files
-- in capabilities/ folder if this table is empty.
CREATE TABLE IF NOT EXISTS capabilities (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    category    TEXT,
    description TEXT    NOT NULL,
    keywords    TEXT    NOT NULL DEFAULT '',  -- comma-separated
    source_file TEXT    NOT NULL,
    added_at    TEXT    NOT NULL DEFAULT (datetime('now'))
);
