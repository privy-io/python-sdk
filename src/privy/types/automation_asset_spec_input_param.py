# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .automation_asset_spec_param import AutomationAssetSpecParam

__all__ = ["AutomationAssetSpecInputParam"]


class AutomationAssetSpecInputParam(AutomationAssetSpecParam, total=False):
    """
    An asset spec accepting either raw identifiers (asset_address, caip2) or human-readable aliases (asset, chain). Exactly one of asset_address or asset must be provided; at most one of caip2 or chain may be provided.
    """

    asset: str

    chain: str
