# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .earn_asset import EarnAsset

__all__ = ["EthereumEarnPositionResponse"]


class EthereumEarnPositionResponse(BaseModel):
    """A wallet's position in an earn vault."""

    asset: EarnAsset
    """Asset metadata for an earn vault position."""

    assets_in_vault: str
    """Current asset value in the vault (realtime from ERC-4626), in smallest unit."""

    shares_in_vault: str
    """Current vault shares held (realtime from ERC-4626)."""

    total_deposited: str
    """Total amount deposited into the vault, in smallest unit."""

    total_withdrawn: str
    """Total amount withdrawn from the vault, in smallest unit."""
