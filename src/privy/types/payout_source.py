# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PayoutSource"]


class PayoutSource(BaseModel):
    """The source crypto asset, chain, and amount for a payout."""

    amount: str
    """Amount to offramp, in the asset's standard units (e.g. "100.00")."""

    asset: str
    """Source crypto asset (e.g. "usdc")."""

    chain: str
    """Source chain (e.g. "base")."""
