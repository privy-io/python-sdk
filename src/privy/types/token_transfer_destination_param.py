# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .stellar_address import StellarAddress

__all__ = ["TokenTransferDestinationParam"]


class TokenTransferDestinationParam(TypedDict, total=False):
    """The destination address for a token transfer.

    Optionally specify a different asset or chain for cross-asset or cross-chain transfers.
    """

    address: Required[StellarAddress]
    """
    Stellar account address: an ed25519 public key in StrKey encoding, starting with
    G.
    """

    asset: str
    """The destination asset.

    Required for cross-asset transfers (e.g., source 'usdt' to destination 'usdc').
    """

    chain: str
    """The destination blockchain network.

    Required for cross-chain transfers (e.g., source 'tempo' to destination 'base').
    """
