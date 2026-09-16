# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel
from .crypto_deposit_account_chain import CryptoDepositAccountChain
from .crypto_deposit_account_source_currency import CryptoDepositAccountSourceCurrency

__all__ = ["CryptoDepositAccountConfigResponse"]


class CryptoDepositAccountConfigResponse(BaseModel):
    """Source-token catalog for crypto deposit accounts.

    Only automation-sweepable, gas-sponsored mainnets.
    """

    chains: Dict[str, CryptoDepositAccountChain]

    currencies: List[CryptoDepositAccountSourceCurrency]
