# Copyright ZettaBlock Labs 2024
from typing import Optional

from zetta._utils.async_utils import synchronizer


@synchronizer.create_blocking
async def setup(profile: Optional[str] = None):
    """Onboard setup"""
    print("TODO: implement setup")
    pass
