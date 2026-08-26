# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["WalletAssetChainNameInputParam"]

WalletAssetChainNameInputParam: TypeAlias = Union[
    Literal[
        "ethereum",
        "arbitrum",
        "avalanche",
        "base",
        "tempo",
        "linea",
        "optimism",
        "polygon",
        "bsc",
        "solana",
        "tron",
        "zksync_era",
        "robinhood",
        "hoodi",
        "sepolia",
        "arbitrum_sepolia",
        "avalanche_fuji",
        "base_sepolia",
        "linea_testnet",
        "optimism_sepolia",
        "polygon_amoy",
        "solana_devnet",
        "solana_testnet",
        "tron_nile",
        "robinhood_testnet",
    ],
    str,
]
