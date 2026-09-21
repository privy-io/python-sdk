# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DepositAccountCryptoQuoteAssetParam"]


class DepositAccountCryptoQuoteAssetParam(TypedDict, total=False):
    """An asset and chain for an indicative crypto deposit-account quote."""

    asset: Required[str]
    """Named asset ID (e.g.

    "usdc", "eth") or chain-specific token contract or mint address
    """

    chain: Required[str]
    """Friendly chain name or CAIP-2 identifier (e.g. "base", "eip155:8453")"""
