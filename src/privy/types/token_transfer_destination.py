# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .stellar_address import StellarAddress

__all__ = ["TokenTransferDestination"]


class TokenTransferDestination(BaseModel):
    """The destination address for a token transfer.

    Optionally specify a different asset or chain for cross-asset or cross-chain transfers.
    """

    address: StellarAddress
    """
    Stellar account address: an ed25519 public key in StrKey encoding, starting with
    G.
    """

    asset: Optional[str] = None
    """The destination asset.

    Required for cross-asset transfers (e.g., source 'usdt' to destination 'usdc').
    """

    chain: Optional[str] = None
    """The destination blockchain network.

    Required for cross-chain transfers (e.g., source 'tempo' to destination 'base').
    """
