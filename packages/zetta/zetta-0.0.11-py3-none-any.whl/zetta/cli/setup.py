from typing import Optional

import typer
from zetta._utils.async_utils import synchronizer


@synchronizer.create_blocking
async def setup(profile: Optional[str] = None):
    """ Onboard setup"""
    print("TODO: implement setup")
    pass
