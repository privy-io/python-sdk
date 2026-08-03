# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SwapDestinationParam"]


class SwapDestinationParam(TypedDict, total=False):
    """The output side of a swap execution request."""

    asset_address: Required[str]
    """Token contract address to buy, or "native" for the chain's native token."""

    caip2: str
    """CAIP-2 chain identifier for the destination.

    Defaults to source chain if omitted. Specify a different chain for cross-chain
    swaps.
    """

    destination_address: str
    """Address to receive the output tokens.

    Defaults to the swapping wallet address. Required when swapping between
    different chain types (e.g. EVM to Solana).
    """
