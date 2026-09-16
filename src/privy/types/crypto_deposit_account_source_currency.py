# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .crypto_deposit_account_source_chain import CryptoDepositAccountSourceChain

__all__ = ["CryptoDepositAccountSourceCurrency"]


class CryptoDepositAccountSourceCurrency(BaseModel):
    """
    A source token in the crypto deposit-account catalog, with the chains it can be sent from.
    """

    chains: List[CryptoDepositAccountSourceChain]

    logo_uri: str
    """URL of the token logo."""

    name: str

    symbol: str
