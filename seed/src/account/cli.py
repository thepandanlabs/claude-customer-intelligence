"""account CLI — entry points.

All subcommands are defined here as Click commands.
Heavy logic lives in ledger.py, extract.py, and report.py — not here.
"""

import sys
import click

from account import ledger, extract, report


@click.group()
def cli() -> None:
    """Account intelligence CLI for Meridian Systems sales team."""


@cli.command()
@click.argument("name")
@click.argument("folder")
def add(name: str, folder: str) -> None:
    """Ingest all .txt files in FOLDER into the ledger under account NAME.

    Files already processed (SHA-256 match) are skipped automatically.
    """
    # TODO: implement
    #   1. Call ledger.ensure_schema() to apply migrations if needed.
    #   2. Iterate over .txt files in folder.
    #   3. For each file, compute SHA-256. If already in ledger, skip and count.
    #   4. Call extract.parse_interaction(text) to get structured data.
    #   5. Call ledger.insert_interaction(...) to write to DB.
    #   6. Print summary to stdout; print progress to stderr.
    click.echo("TODO: account add not yet implemented", err=True)
    sys.exit(1)


@cli.command()
@click.argument("name")
def brief(name: str) -> None:
    """Generate a markdown account brief for NAME and print to stdout.

    Includes: last contact date, interaction count, open commitments, key risks.
    """
    # TODO: implement
    #   1. Call ledger.get_interactions(name) sorted by (date ASC, source_file ASC).
    #   2. Call report.render_brief(name, interactions) to produce markdown.
    #   3. Print markdown to stdout.
    click.echo("TODO: account brief not yet implemented", err=True)
    sys.exit(1)


@cli.command()
@click.option("--open", "open_only", is_flag=True, default=False,
              help="Show only unresolved commitments.")
@click.option("--account", "account_name", default=None,
              help="Filter to a single account.")
def query(open_only: bool, account_name: str | None) -> None:
    """Query commitments across all accounts (or a single account).

    Note: commitments extraction is Stub A. Until Stub A is implemented,
    this command returns an empty result set.
    """
    # TODO: implement (requires Stub A — commitments table)
    #   1. Call ledger.get_commitments(account=account_name, open_only=open_only).
    #   2. Print results to stdout, one per line, sorted by due_date ASC.
    click.echo("TODO: account query (Stub A not yet implemented)", err=True)
    sys.exit(1)


@cli.command("list")
def list_accounts() -> None:
    """List all accounts in the ledger."""
    # TODO: implement
    #   1. Call ledger.list_accounts().
    #   2. Print each account name to stdout, one per line.
    click.echo("TODO: account list not yet implemented", err=True)
    sys.exit(1)


@cli.command()
@click.option("--account", "account_name", default=None,
              help="Export a single account only. Omit to export all accounts.")
@click.option("--output", "output_path", default="data.json",
              help="Output file path (default: data.json in current directory).")
def export(account_name: str | None, output_path: str) -> None:
    """Export ledger data to JSON for dashboard.html.

    If --account is given, exports that account only.
    """
    # TODO: implement
    #   1. Call ledger.get_interactions(account=account_name).
    #   2. Call report.render_json(interactions) to produce the JSON structure.
    #   3. Write to output_path.
    #   4. Print confirmation to stderr.
    click.echo("TODO: account export not yet implemented", err=True)
    sys.exit(1)


@cli.command()
@click.option("--rfp", "rfp_path", required=True,
              help="Path to the RFP text file.")
@click.option("--account", "account_name", default=None,
              help="Account name to pull context from. Omit to generate generic proposal.")
def pitch(rfp_path: str, account_name: str | None) -> None:
    """Generate a proposal draft from an RFP file. (Stub D)

    Reads the account brief for context, matches RFP requirements to
    capabilities in the capabilities/ folder, and writes a markdown proposal.
    """
    # TODO: implement (Stub D)
    #   See PRD.md ## Stub D for full spec.
    click.echo("TODO: account pitch (Stub D not yet implemented)", err=True)
    sys.exit(1)


@cli.group()
def capability() -> None:
    """Manage the capability library. (Stub E)"""


@capability.command("add")
@click.argument("file_path")
def capability_add(file_path: str) -> None:
    """Add a capability file to the library. (Stub E)"""
    # TODO: implement (Stub E)
    click.echo("TODO: account capability add (Stub E not yet implemented)", err=True)
    sys.exit(1)


@capability.command("list")
def capability_list() -> None:
    """List all capabilities in the library. (Stub E)"""
    # TODO: implement (Stub E)
    click.echo("TODO: account capability list (Stub E not yet implemented)", err=True)
    sys.exit(1)


if __name__ == "__main__":
    cli()
