# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from ..._models import BaseModel
from ..wallet_asset_chain_name_input import WalletAssetChainNameInput

__all__ = ["BalanceGetResponse", "Balance"]


class Balance(BaseModel):
    asset: Union[
        Literal["usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "ousd", "pathusd", "sol", "trx"],
        str,
    ]

    chain: WalletAssetChainNameInput
    """Supported blockchain network names for wallet balance and transaction queries."""

    display_values: Dict[str, str]

    raw_value: str

    raw_value_decimals: float


class BalanceGetResponse(BaseModel):
    balances: List[Balance]
