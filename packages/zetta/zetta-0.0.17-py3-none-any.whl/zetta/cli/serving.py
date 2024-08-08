# Copyright ZettaBlock Labs 2024
import typer
from zetta._utils.async_utils import synchronizer

serving_cli = typer.Typer(
    name="serving",
    help="Manage your inference serving in Zetta Workspace.",
    no_args_is_help=True,
)


@serving_cli.command(
    name="list", help="List all inference instance that are currently running."
)
@synchronizer.create_blocking
async def list(model: str = ""):
    pass


@serving_cli.command(name="deploy", help="deploy a model for serving.")
@synchronizer.create_blocking
async def deploy(model: str = "", replica: int = 1):
    pass


@serving_cli.command(name="update", help="update a serving config")
@synchronizer.create_blocking
async def update(replica: int = 1):
    pass


@serving_cli.command(name="shell", help="open a shell to chat with model")
@synchronizer.create_blocking
async def shell(model: str = ""):
    pass
