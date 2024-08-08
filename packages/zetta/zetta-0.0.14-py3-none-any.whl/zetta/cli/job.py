# Copyright ZettaBlock Labs 2024
import typer
from zetta._utils.async_utils import synchronizer
from zetta._utils.connections import check_api_status

job_cli = typer.Typer(
    name="job", help="Manage your jobs in Zetta Workspace.", no_args_is_help=True
)

@job_cli.command(name="list", help="List all jobs that are currently running.")
@synchronizer.create_blocking
async def list(json: bool = False):
    pass


@job_cli.command(name="get", help="get a job status.")
@synchronizer.create_blocking
async def get(json: bool = False):
    pass


@job_cli.command(name="update", help="update a job.")
@synchronizer.create_blocking
async def update(json: bool = False):
    pass

@job_cli.command(name="cancel", help="cancel a running job for current user.")
@synchronizer.create_blocking
async def cancel(json: bool = False):
    pass

@job_cli.command(name="status", help="check the status of the Zetta API.")
@synchronizer.create_blocking
async def status():
    return check_api_status()
