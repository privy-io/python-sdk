# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .earn_asset import EarnAsset
from .earn_position_apy_allocation import EarnPositionApyAllocation

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

    apy_allocation: Optional[List[EarnPositionApyAllocation]] = None
    """Vault APY allocations by origin, returned together with apy_bps when available."""

    apy_bps: Optional[int] = None
    """Wallet-specific net APY in basis points, rounded to the nearest integer.

    Returned together with apy_allocation when available.
    """
