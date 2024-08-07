import typer
from zetta._utils.async_utils import synchronizer

job_cli = typer.Typer(name="job", help="Manage your jobs in Zetta Workspace.", no_args_is_help=True)


@job_cli.command(name="list", help="List all jobs that are currently running.")
@synchronizer.create_blocking
async def list(json: bool = False):
    pass


@job_cli.command(name="get", help="get a job status.")
@synchronizer.create_blocking
async def get(json: bool = False):
    pass


@job_cli.command(name="update", help="update a job .")
@synchronizer.create_blocking
async def update(json: bool = False):
    pass



