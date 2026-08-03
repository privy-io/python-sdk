# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SwapQuoteDestinationParam"]


class SwapQuoteDestinationParam(TypedDict, total=False):
    """The output side of a swap quote request."""

    asset_address: Required[str]
    """Token contract address to buy, or "native" for the chain's native token."""

    caip2: str
    """CAIP-2 chain identifier for the destination.

    Defaults to source chain if omitted. Will result in a cross-chain swap if source
    and destination chains differ.
    """

    destination_address: str
    """Address to receive the output tokens.

    Defaults to the swapping wallet address. Required when swapping between chains
    with different address types (e.g. EVM to Solana).
    """
