# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DepositStartedDestination"]


class DepositStartedDestination(BaseModel):
    """The crypto asset and chain the fiat deposit is being converted into."""

    asset: str
    """The crypto asset the deposit is converted into (e.g. "usdc")."""

    chain: str
    """The chain the converted crypto is delivered on (e.g. "base")."""
