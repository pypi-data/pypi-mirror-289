# Copyright ZettaBlock Labs 2024
import typer
from zetta._utils.async_utils import synchronizer

config_cli = typer.Typer(
    name="config", help="Manage your config in Zetta AI Network.", no_args_is_help=True
)


@config_cli.command(name="add-key", help="add API keys for AI network.")
@synchronizer.create_blocking
async def add_key(json: bool = False):
    pass


@config_cli.command(name="add-secret", help="add secret for AI network.")
@synchronizer.create_blocking
async def add_secret(json: bool = False):
    pass


@config_cli.command(name="add-wallet", help="add wallet for AI network.")
@synchronizer.create_blocking
async def add_wallet(json: bool = False):
    pass
