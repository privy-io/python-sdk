# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["TransactionChainNameInputParam"]

TransactionChainNameInputParam: TypeAlias = Union[
    Literal[
        "ethereum",
        "arbitrum",
        "avalanche",
        "base",
        "base_sepolia",
        "bsc",
        "tempo",
        "linea",
        "optimism",
        "polygon",
        "solana",
        "sepolia",
    ],
    str,
]
