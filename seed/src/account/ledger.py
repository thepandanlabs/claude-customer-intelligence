"""ledger.py — SQLite read/write and deduplication.

Rules:
- No network calls in this module.
- No Claude API calls in this module.
- All queries must include ORDER BY (date ASC, source_file ASC) to ensure
  deterministic output.
- Deduplication key: SHA-256 hash of source file bytes.
"""

import sqlite3
from pathlib import Path

# Default DB location. Can be overridden in tests.
DEFAULT_DB_PATH = Path.home() / ".account" / "account.db"


def get_connection(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Open (or create) the SQLite database and return a connection."""
    # TODO: implement
    #   1. Create parent directory if it doesn't exist.
    #   2. Open connection with sqlite3.connect(db_path).
    #   3. Enable WAL mode for concurrency safety.
    #   4. Return connection.
    raise NotImplementedError


def ensure_schema(conn: sqlite3.Connection) -> None:
    """Apply migrations/001_init.sql if the schema does not exist yet."""
    # TODO: implement
    #   1. Check if the 'interactions' table exists.
    #   2. If not, read migrations/001_init.sql and execute it.
    raise NotImplementedError


def sha256_of_file(file_path: Path) -> str:
    """Return the SHA-256 hex digest of the file at file_path."""
    # TODO: implement
    raise NotImplementedError


def file_already_processed(conn: sqlite3.Connection, sha256: str) -> bool:
    """Return True if a row with this sha256 already exists in interactions."""
    # TODO: implement
    raise NotImplementedError


def insert_interaction(
    conn: sqlite3.Connection,
    account: str,
    date: str,
    interaction_type: str,
    source_file: str,
    sha256: str,
    raw_text: str,
) -> None:
    """Insert a single interaction row into the interactions table.

    Caller is responsible for dedup check before calling this function.
    """
    # TODO: implement
    raise NotImplementedError


def get_interactions(
    conn: sqlite3.Connection,
    account: str | None = None,
) -> list[dict]:
    """Return all interactions, optionally filtered by account.

    Always sorted by (date ASC, source_file ASC).
    Returns a list of dicts with keys matching the interactions table columns.
    """
    # TODO: implement
    raise NotImplementedError


def list_accounts(conn: sqlite3.Connection) -> list[str]:
    """Return a sorted list of all distinct account names in the ledger."""
    # TODO: implement
    raise NotImplementedError


def get_commitments(
    conn: sqlite3.Connection,
    account: str | None = None,
    open_only: bool = False,
) -> list[dict]:
    """Return commitments, optionally filtered by account and/or open status.

    Requires Stub A (commitments table). Returns empty list until implemented.
    Always sorted by (due_date ASC, account ASC).
    """
    # TODO: implement (Stub A)
    return []
