# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .automation_destination_asset import AutomationDestinationAsset

__all__ = ["AutomationSwapActionConfig"]


class AutomationSwapActionConfig(BaseModel):
    """Action configuration for swap operations."""

    destination_chain_asset: AutomationDestinationAsset
    """Destination asset identified by contract address on a specific chain (CAIP-2)."""

    type: Literal["swap"]
