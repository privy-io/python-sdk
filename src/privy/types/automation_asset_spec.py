# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AutomationAssetSpec"]


class AutomationAssetSpec(BaseModel):
    """An asset identified by contract address, scoped to a chain via CAIP-2."""

    asset_address: str

    caip2: str
