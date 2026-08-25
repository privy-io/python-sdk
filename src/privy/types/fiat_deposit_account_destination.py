# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FiatDepositAccountDestination"]


class FiatDepositAccountDestination(BaseModel):
    """The destination crypto asset and chain for a fiat deposit account."""

    asset: str
    """Destination crypto asset (e.g. "usdc")."""

    chain: str
    """Destination chain (e.g. "base", "tempo")."""
