# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BalanceGetResponse", "Balance"]


class Balance(BaseModel):
    asset: Literal["usdc", "eth", "pol", "sol"]

    chain: Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"]

    display_values: Dict[str, str]

    raw_value: str

    raw_value_decimals: float


class BalanceGetResponse(BaseModel):
    balances: List[Balance]
