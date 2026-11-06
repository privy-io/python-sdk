# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .stellar_address import StellarAddress

__all__ = ["CustomTokenTransferSourceParam"]


class CustomTokenTransferSourceParam(TypedDict, total=False):
    """
    Source for a transfer identified by a token contract address (EVM) or mint address (Solana). Use this variant for tokens that are not first-class assets.
    """

    asset_address: Required[StellarAddress]
    """
    Stellar account address: an ed25519 public key in StrKey encoding, starting with
    G.
    """

    chain: Required[str]
    """The blockchain network on which to perform the transfer.

    Supported chains include: 'tempo', 'ethereum', 'base', 'arbitrum', 'polygon',
    'solana', and their respective testnets.
    """

    amount: str
    """Amount as a decimal string in the token's standard unit (e.g.

    "1.5" for 1.5 USDC, "0.01" for 0.01 ETH). For exact_input, specifies the amount
    to send. Not in the smallest on-chain unit (wei, lamports, etc.). Maximum 100
    characters. Deprecated: use the top-level `amount` field instead.
    """
