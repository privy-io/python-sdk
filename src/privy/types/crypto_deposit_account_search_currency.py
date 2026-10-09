# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .crypto_deposit_account_source_chain import CryptoDepositAccountSourceChain

__all__ = ["CryptoDepositAccountSearchCurrency"]


class CryptoDepositAccountSearchCurrency(BaseModel):
    """A source token matched by crypto deposit-account search."""

    chains: List[CryptoDepositAccountSourceChain]

    name: str

    symbol: str

    verified: bool
    """
    Whether this token is verified as the canonical token for its symbol, since
    unverified tokens may be lookalikes.
    """

    logo_uri: Optional[str] = None
    """URL of the token logo, omitted when none is known."""
