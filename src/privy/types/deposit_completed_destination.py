# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DepositCompletedDestination"]


class DepositCompletedDestination(BaseModel):
    """
    The crypto asset, chain, delivered amount, and settlement transaction for a completed deposit.
    """

    amount: str
    """The crypto amount delivered to the wallet, after conversion and fees."""

    asset: str
    """The crypto asset the deposit was converted into (e.g. "usdc")."""

    chain: str
    """The chain the converted crypto was delivered on (e.g. "base")."""

    transaction_hash: str
    """The on-chain settlement transaction for the delivered crypto."""
