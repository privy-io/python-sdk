# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SwapSourceParam"]


class SwapSourceParam(TypedDict, total=False):
    """The input side of a swap request, including token and chain."""

    asset_address: Required[str]
    """Token contract address to sell, or "native" for the chain's native token."""

    caip2: Required[str]
    """
    CAIP-2 chain identifier (e.g., "eip155:4217" for Tempo, "eip155:1" for
    Ethereum).
    """
