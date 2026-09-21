# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .automation_asset_spec_param import AutomationAssetSpecParam

__all__ = ["AutomationAssetSpecInputParam"]


class AutomationAssetSpecInputParam(AutomationAssetSpecParam, total=False):
    """
    An asset spec accepting either raw identifiers (asset_address, caip2) or human-readable aliases (asset, chain). Exactly one of asset_address or asset must be provided; at most one of caip2 or chain may be provided. Use "*" for asset_address or asset to match any asset on a given chain (chain is then required). Omitting chain/caip2 (or passing "*" for either) matches the specified asset on any chain.
    """

    asset: str

    chain: str
