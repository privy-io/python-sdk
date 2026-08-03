# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr
from ..wallet_asset import WalletAsset
from ..wallet_asset_chain_name_input import WalletAssetChainNameInput

__all__ = ["BalanceGetParams"]


class BalanceGetParams(TypedDict, total=False):
    token: Union[str, SequenceNotStr[str]]
    """
    The token contract address(es) to query in format "chain:address" (e.g.,
    "tempo:0x20c000000000000000000000b9537d11c60e8b50" or
    "solana:EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"). Cannot be used together
    with `asset`/`chain` or with `include_currency`.
    """

    asset: Union[
        Literal["usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "pathusd", "sol", "trx"],
        List[WalletAsset],
    ]
    """Named asset(s) to query (e.g.

    `eth`, `usdc`). Use together with `chain` to scope the query. Cannot be used
    with `token`.
    """

    chain: Union[WalletAssetChainNameInput, List[WalletAssetChainNameInput]]
    """Chain(s) to query named assets on (e.g.

    `tempo`, `base`). Use together with `asset`. Cannot be used with `token`.
    """

    include_archived: bool
    """Include archived wallets in lookup. Defaults to false."""

    include_currency: Literal["usd", "eur"]
    """If set, balances are converted to the specified fiat currency.

    Not supported when `token` is provided.
    """
