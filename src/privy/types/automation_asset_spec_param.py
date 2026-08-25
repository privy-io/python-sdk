# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutomationAssetSpecParam"]


class AutomationAssetSpecParam(TypedDict, total=False):
    """An asset identified by contract address, scoped to a chain via CAIP-2."""

    asset_address: Required[str]

    caip2: Required[str]
