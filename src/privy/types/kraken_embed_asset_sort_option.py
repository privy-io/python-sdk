# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["KrakenEmbedAssetSortOption"]

KrakenEmbedAssetSortOption: TypeAlias = Literal[
    "trending",
    "market_cap_rank",
    "-market_cap_rank",
    "symbol",
    "-symbol",
    "name",
    "-name",
    "change_percent_1h",
    "-change_percent_1h",
    "change_percent_24h",
    "-change_percent_24h",
    "change_percent_7d",
    "-change_percent_7d",
    "change_percent_30d",
    "-change_percent_30d",
    "change_percent_1y",
    "-change_percent_1y",
    "listing_date",
    "-listing_date",
]
