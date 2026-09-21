# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .automation_destination_asset_input_param import AutomationDestinationAssetInputParam

__all__ = ["AutomationSwapActionConfigInputParam"]


class AutomationSwapActionConfigInputParam(TypedDict, total=False):
    """Action configuration for swap operations (input form with alias support)."""

    destination_chain_asset: Required[AutomationDestinationAssetInputParam]
    """
    A destination asset spec accepting either raw identifiers (asset_address, caip2)
    or human-readable aliases (asset, chain). Exactly one of asset_address or asset
    must be provided; exactly one of caip2 or chain must be provided.
    """

    type: Required[Literal["swap"]]
