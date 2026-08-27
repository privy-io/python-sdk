# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .crypto_deposit_asset_param import CryptoDepositAssetParam

__all__ = ["CryptoDepositAssetFilterExcludeParam"]


class CryptoDepositAssetFilterExcludeParam(TypedDict, total=False):
    """
    Match all assets except the specified ones, using human-readable aliases when known.
    """

    mode: Required[Literal["exclude"]]

    values: Required[Iterable[CryptoDepositAssetParam]]
