# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel
from .crypto_deposit_account_chain import CryptoDepositAccountChain
from .crypto_deposit_account_search_currency import CryptoDepositAccountSearchCurrency

__all__ = ["CryptoDepositAccountConfigSearchResponse"]


class CryptoDepositAccountConfigSearchResponse(BaseModel):
    """Source tokens matching a crypto deposit-account search."""

    chains: Dict[str, CryptoDepositAccountChain]

    currencies: List[CryptoDepositAccountSearchCurrency]
