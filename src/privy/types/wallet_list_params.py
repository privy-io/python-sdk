# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WalletListParams"]


class WalletListParams(TypedDict, total=False):
    chain_type: Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"]
    """Chain type of the wallet. 'Ethereum' supports any EVM-compatible network."""

    cursor: str

    limit: Optional[float]
