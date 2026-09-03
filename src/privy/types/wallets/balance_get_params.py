# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BalanceGetParams"]


class BalanceGetParams(TypedDict, total=False):
    asset: Required[Union[Literal["usdc", "eth", "pol", "sol"], List[Literal["usdc", "eth", "pol", "sol"]]]]

    chain: Required[
        Union[
            Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"],
            List[Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"]],
        ]
    ]

    include_currency: Literal["usd"]
