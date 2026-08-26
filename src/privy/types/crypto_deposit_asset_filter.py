# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .crypto_deposit_asset_filter_all import CryptoDepositAssetFilterAll
from .crypto_deposit_asset_filter_exclude import CryptoDepositAssetFilterExclude
from .crypto_deposit_asset_filter_include import CryptoDepositAssetFilterInclude

__all__ = ["CryptoDepositAssetFilter"]

CryptoDepositAssetFilter: TypeAlias = Annotated[
    Union[CryptoDepositAssetFilterAll, CryptoDepositAssetFilterInclude, CryptoDepositAssetFilterExclude],
    PropertyInfo(discriminator="mode"),
]
