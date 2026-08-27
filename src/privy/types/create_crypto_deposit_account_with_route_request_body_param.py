# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .crypto_deposit_asset_param import CryptoDepositAssetParam
from .crypto_deposit_asset_filter_param import CryptoDepositAssetFilterParam

__all__ = ["CreateCryptoDepositAccountWithRouteRequestBodyParam"]


class CreateCryptoDepositAccountWithRouteRequestBodyParam(TypedDict, total=False):
    """Creates a crypto deposit account from an inline source and destination."""

    destination: Required[CryptoDepositAssetParam]
    """An asset on a chain.

    Uses a human-readable alias (usdc, base) when one is on file, otherwise the raw
    asset address and CAIP-2.
    """

    source: Required[CryptoDepositAssetFilterParam]
    """Which assets a deposit address accepts.

    Asset and chain use human-readable aliases when known.
    """
