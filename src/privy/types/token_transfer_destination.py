# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenTransferDestination"]


class TokenTransferDestination(BaseModel):
    """The destination address for a token transfer.

    Optionally specify a different asset or chain for cross-asset or cross-chain transfers.
    """

    address: str
    """Recipient address (hex for EVM, base58 for Solana, base58check for Tron)"""

    asset: Optional[str] = None
    """The destination asset.

    Required for cross-asset transfers (e.g., source 'usdt' to destination 'usdc').
    """

    chain: Optional[str] = None
    """The destination blockchain network.

    Required for cross-chain transfers (e.g., source 'tempo' to destination 'base').
    """
