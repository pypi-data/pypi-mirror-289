# Copyright ZettaBlock Labs 2024
import typer
from zetta._utils.async_utils import synchronizer

blockchain_cli = typer.Typer(
    name="blockchain", help="blockchain interactions.", no_args_is_help=True
)


@blockchain_cli.command(
    name="get-balance", help="List all jobs that are currently running."
)
@synchronizer.create_blocking
async def get_balance(json: bool = False):
    pass


@blockchain_cli.command(name="submit", help="submit a fine tuning job.")
@synchronizer.create_blocking
async def submit(json: bool = False):
    pass


@blockchain_cli.command(name="get-lineage", help="get a job lineage.")
@synchronizer.create_blocking
async def get_lineage(json: bool = False):
    pass
