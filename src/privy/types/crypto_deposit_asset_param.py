# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CryptoDepositAssetParam"]


class CryptoDepositAssetParam(TypedDict, total=False):
    """An asset on a chain.

    Uses a human-readable alias (usdc, base) when one is on file, otherwise the raw asset address and CAIP-2.
    """

    asset: Required[str]
    """Known alias (usdc) or raw asset address."""

    chain: str
    """Known alias (base) or CAIP-2.

    Omit on a source value to match every supported chain for that asset.
    """
