# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EarnAsset"]


class EarnAsset(BaseModel):
    """Asset metadata for an earn vault position."""

    address: str
    """Token contract address."""

    decimals: int
    """Number of decimals for the asset (e.g. 6 for USDC)."""

    symbol: str
    """Lowercase token symbol (e.g. "usdc")."""
