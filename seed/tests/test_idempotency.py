"""test_idempotency.py — Verify that ingesting the same folder twice adds zero rows.

This test does NOT call Claude. It stubs extract.parse_interaction to return
a minimal fixture response, then exercises ledger.py directly.

Run with: pytest tests/test_idempotency.py
"""

import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from account import ledger


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

FIXTURE_INTERACTION = {
    "date": "2025-01-15",
    "type": "email",
    "summary": "Initial outreach from Sarah Chen to James Park.",
}


@pytest.fixture
def tmp_db(tmp_path: Path) -> sqlite3.Connection:
    """Return an in-memory (temp file) DB connection with schema applied."""
    db_path = tmp_path / "test.db"
    conn = ledger.get_connection(db_path)
    ledger.ensure_schema(conn)
    return conn


@pytest.fixture
def sample_inbox(tmp_path: Path) -> Path:
    """Create a small inbox folder with two .txt files."""
    inbox = tmp_path / "inbox" / "acme"
    inbox.mkdir(parents=True)

    (inbox / "email-2025-01-15.txt").write_text(
        "From: Sarah Chen\nTo: James Park\nDate: January 15, 2025\n\nHello.",
        encoding="utf-8",
    )
    (inbox / "call-2025-02-03.txt").write_text(
        "Call transcript\nDate: February 3, 2025\n\nDiscovery call notes.",
        encoding="utf-8",
    )
    return inbox


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_add_twice_produces_same_row_count(
    tmp_db: sqlite3.Connection,
    sample_inbox: Path,
) -> None:
    """Ingesting the same folder twice must not add any new rows."""

    # TODO: replace this stub once ledger.insert_interaction is implemented.
    # The test structure below shows the intended call pattern.

    def _ingest_folder(conn: sqlite3.Connection, account: str, folder: Path) -> int:
        """Ingest all .txt files in folder. Returns number of new rows written."""
        # TODO: this helper should be replaced by the real `account add` logic
        # once cli.py and ledger.py are implemented. For now it's inlined here
        # to make the test runnable against the stub.
        written = 0
        for txt_file in sorted(folder.glob("*.txt")):
            sha = ledger.sha256_of_file(txt_file)
            if ledger.file_already_processed(conn, sha):
                continue
            ledger.insert_interaction(
                conn=conn,
                account=account,
                date=FIXTURE_INTERACTION["date"],
                interaction_type=FIXTURE_INTERACTION["type"],
                source_file=txt_file.name,
                sha256=sha,
                raw_text=txt_file.read_text(encoding="utf-8"),
            )
            written += 1
        return written

    account_name = "acme"

    # First pass — should write 2 rows
    first_pass_count = _ingest_folder(tmp_db, account_name, sample_inbox)
    assert first_pass_count == 2, f"Expected 2 rows on first pass, got {first_pass_count}"

    # Capture total rows after first pass
    cursor = tmp_db.execute("SELECT COUNT(*) FROM interactions WHERE account = ?", (account_name,))
    rows_after_first = cursor.fetchone()[0]
    assert rows_after_first == 2

    # Second pass — should write 0 rows
    second_pass_count = _ingest_folder(tmp_db, account_name, sample_inbox)
    assert second_pass_count == 0, f"Expected 0 new rows on second pass, got {second_pass_count}"

    # Confirm total row count is unchanged
    cursor = tmp_db.execute("SELECT COUNT(*) FROM interactions WHERE account = ?", (account_name,))
    rows_after_second = cursor.fetchone()[0]
    assert rows_after_second == rows_after_first, (
        f"Row count changed after second ingestion: {rows_after_first} -> {rows_after_second}"
    )
