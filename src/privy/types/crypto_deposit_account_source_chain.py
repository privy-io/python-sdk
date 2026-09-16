# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .crypto_deposit_account_caip_2 import CryptoDepositAccountCaip2

__all__ = ["CryptoDepositAccountSourceChain"]


class CryptoDepositAccountSourceChain(BaseModel):
    """A token contract on one source chain in the crypto deposit-account catalog."""

    address: str
    """Token contract or native asset address on this chain."""

    caip2: CryptoDepositAccountCaip2
    """EVM CAIP-2 chain identifier (e.g.

    "eip155:4217" for Tempo, "eip155:1" for Ethereum).
    """

    decimals: int
    """Token decimals on this chain."""
