# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AutomationDestinationAsset"]


class AutomationDestinationAsset(BaseModel):
    """Destination asset identified by contract address on a specific chain (CAIP-2)."""

    asset_address: str

    caip2: str
