# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .wisdom_tree_settlement_fund_amount import WisdomTreeSettlementFundAmount
from .wisdom_tree_settlement_withdraw_asset_amount import WisdomTreeSettlementWithdrawAssetAmount

__all__ = ["WisdomTreeSettlementReceivedAmount"]

WisdomTreeSettlementReceivedAmount: TypeAlias = Union[
    WisdomTreeSettlementFundAmount, WisdomTreeSettlementWithdrawAssetAmount
]
