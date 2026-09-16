# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .crypto_deposit_account_caip_2 import CryptoDepositAccountCaip2

__all__ = ["CryptoDepositAccountChain"]


class CryptoDepositAccountChain(BaseModel):
    """Chain metadata for rendering the crypto deposit-account source picker."""

    caip2: CryptoDepositAccountCaip2
    """EVM CAIP-2 chain identifier (e.g.

    "eip155:4217" for Tempo, "eip155:1" for Ethereum).
    """

    chain_id: int
    """Numeric chain id used by some clients as an alias."""

    display_name: str

    icon_url: str
    """URL of the chain icon."""

    vm_type: str
    """Execution VM, e.g. evm or svm."""
