import click
import typer

from zetta.cli.blockchain import blockchain_cli
from zetta.cli.config import config_cli
from zetta.cli.git import git_cli
from . import run
from .job import job_cli
from .example import async_cli
from .setup import setup
from .model import model_cli
from zetta_version import __version__


entrypoint_cli_typer = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="markdown",
    help="""
    Zetta stands for a better AI economics

    See the website at https://zettablock.com/ for documentation and more information
    about running code on ZettaBlock AI network.
    """,
)


def version_callback(value: bool):
    if value:
        from zetta_version import __version__

        typer.echo(f"zetta client version: {__version__}")
        raise typer.Exit()


@entrypoint_cli_typer.callback()
def zetta(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass


# Config
entrypoint_cli_typer.add_typer(config_cli, rich_help_panel="Config")

# Git
entrypoint_cli_typer.add_typer(git_cli, rich_help_panel="Git")

# Deployments
entrypoint_cli_typer.add_typer(job_cli, rich_help_panel="AI Network")

# Blockchain
entrypoint_cli_typer.add_typer(blockchain_cli, rich_help_panel="Blockchain")

# Onboarding flow
entrypoint_cli_typer.command("setup", help="Bootstrap Zetta's configuration.", rich_help_panel="Onboarding")(setup)


entrypoint_cli = typer.main.get_command(entrypoint_cli_typer)
entrypoint_cli.list_commands(None)  # type: ignore


if __name__ == "__main__":
    # this module is only called from tests, otherwise the parent package __main__.py is used as the entrypoint
    entrypoint_cli()
