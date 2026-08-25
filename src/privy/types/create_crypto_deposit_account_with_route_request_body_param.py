# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .automation_asset_filter_input_param import AutomationAssetFilterInputParam
from .automation_destination_asset_input_param import AutomationDestinationAssetInputParam

__all__ = ["CreateCryptoDepositAccountWithRouteRequestBodyParam"]


class CreateCryptoDepositAccountWithRouteRequestBodyParam(TypedDict, total=False):
    """Creates a crypto deposit account from an inline source and destination."""

    destination: Required[AutomationDestinationAssetInputParam]
    """
    A destination asset spec accepting either raw identifiers (asset_address, caip2)
    or human-readable aliases (asset, chain). Exactly one of asset_address or asset
    must be provided; exactly one of caip2 or chain must be provided.
    """

    source: Required[AutomationAssetFilterInputParam]
    """
    Which assets to include/exclude for an automation trigger (input form with alias
    support).
    """
