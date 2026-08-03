# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .wallet_funds_sac_asset import WalletFundsSacAsset
from .wallet_funds_spl_asset import WalletFundsSplAsset
from .wallet_funds_erc_20_asset import WalletFundsErc20Asset
from .wallet_funds_trc_20_asset import WalletFundsTrc20Asset
from .wallet_funds_native_token_asset import WalletFundsNativeTokenAsset

__all__ = ["WalletFundsAsset"]

WalletFundsAsset: TypeAlias = Annotated[
    Union[
        WalletFundsNativeTokenAsset,
        WalletFundsErc20Asset,
        WalletFundsSplAsset,
        WalletFundsSacAsset,
        WalletFundsTrc20Asset,
    ],
    PropertyInfo(discriminator="type"),
]
