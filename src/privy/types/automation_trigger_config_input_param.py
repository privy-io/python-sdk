# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .automation_asset_filter_input_param import AutomationAssetFilterInputParam

__all__ = ["AutomationTriggerConfigInputParam"]


class AutomationTriggerConfigInputParam(TypedDict, total=False):
    """Trigger configuration for deposit events (input form with alias support)."""

    assets: Required[AutomationAssetFilterInputParam]
    """
    Which assets to include/exclude for an automation trigger (input form with alias
    support).
    """

    type: Required[Literal["deposit"]]
