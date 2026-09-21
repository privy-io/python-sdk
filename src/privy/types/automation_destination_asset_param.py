# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutomationDestinationAssetParam"]


class AutomationDestinationAssetParam(TypedDict, total=False):
    """Destination asset identified by contract address on a specific chain (CAIP-2)."""

    asset_address: Required[str]

    caip2: Required[str]
