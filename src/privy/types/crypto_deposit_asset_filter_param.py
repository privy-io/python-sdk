# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .crypto_deposit_asset_filter_all_param import CryptoDepositAssetFilterAllParam
from .crypto_deposit_asset_filter_exclude_param import CryptoDepositAssetFilterExcludeParam
from .crypto_deposit_asset_filter_include_param import CryptoDepositAssetFilterIncludeParam

__all__ = ["CryptoDepositAssetFilterParam"]

CryptoDepositAssetFilterParam: TypeAlias = Union[
    CryptoDepositAssetFilterAllParam, CryptoDepositAssetFilterIncludeParam, CryptoDepositAssetFilterExcludeParam
]
