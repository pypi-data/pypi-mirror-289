"""Module defining the CLI for Artix."""

from __future__ import annotations

import importlib.metadata
from pathlib import Path

import loguru
import rich_click as click

import artix.config

PACKAGE = Path(__file__).parent.name
VERSION = importlib.metadata.version(PACKAGE)


@click.group()
def cli() -> None:
    """Run the CLI application."""


@cli.command()
def version() -> None:  # pragma: no cover
    """Display Artix version information."""
    click.echo(message=VERSION)


@cli.command()
@click.option(
    "--chdir",
    help="Act on this directory, defaults to the current working directory.",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        writable=True,
        resolve_path=True,
    ),
    default=Path(),
    required=False,
)
@click.pass_context
def sync(ctx: click.Context, chdir: str | Path) -> None:
    """Sync the local filesystem with the Artix artifacts."""
    # Force it into a path type.
    chdir = Path(chdir)

    # Normalize the given path.
    loguru.logger.info("syncing local repository with artifacts")
    loguru.logger.info("using directory: {}", chdir)

    # Load the configuration for the project.
    project = artix.config.Project.from_path(path=chdir)

    # Sync the project.
    success = project.sync()
    ctx.exit(code=int(not success))


if __name__ == "__main__":  # pragma: no cover
    cli()
