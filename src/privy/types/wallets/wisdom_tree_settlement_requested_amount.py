# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .wisdom_tree_settlement_fund_amount import WisdomTreeSettlementFundAmount
from .wisdom_tree_settlement_deposit_asset_amount import WisdomTreeSettlementDepositAssetAmount

__all__ = ["WisdomTreeSettlementRequestedAmount"]

WisdomTreeSettlementRequestedAmount: TypeAlias = Union[
    WisdomTreeSettlementDepositAssetAmount, WisdomTreeSettlementFundAmount
]
