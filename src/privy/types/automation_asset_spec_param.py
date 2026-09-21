# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutomationAssetSpecParam"]


class AutomationAssetSpecParam(TypedDict, total=False):
    """An asset identified by contract address on a specific chain (CAIP-2).

    Either field may be "*": asset_address: "*" matches any asset on the chain; caip2: "*" matches the asset on any chain (in this case asset_address holds the asset symbol id, e.g. "usdc" or "eth", not a contract address).
    """

    asset_address: Required[str]

    caip2: Required[str]
