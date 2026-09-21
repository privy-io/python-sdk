# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .automation_destination_asset_param import AutomationDestinationAssetParam

__all__ = ["AutomationDestinationAssetInputParam"]


class AutomationDestinationAssetInputParam(AutomationDestinationAssetParam, total=False):
    """
    A destination asset spec accepting either raw identifiers (asset_address, caip2) or human-readable aliases (asset, chain). Exactly one of asset_address or asset must be provided; exactly one of caip2 or chain must be provided.
    """

    asset: str

    chain: str
