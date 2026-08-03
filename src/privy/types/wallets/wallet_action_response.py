# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .swap_action_response import SwapActionResponse
from .transfer_action_response import TransferActionResponse
from .earn_deposit_action_response import EarnDepositActionResponse
from .earn_withdraw_action_response import EarnWithdrawActionResponse
from .earn_fee_collect_action_response import EarnFeeCollectActionResponse
from .earn_incentive_claim_action_response import EarnIncentiveClaimActionResponse

__all__ = ["WalletActionResponse"]

WalletActionResponse: TypeAlias = Annotated[
    Union[
        SwapActionResponse,
        TransferActionResponse,
        EarnDepositActionResponse,
        EarnWithdrawActionResponse,
        EarnIncentiveClaimActionResponse,
        EarnFeeCollectActionResponse,
    ],
    PropertyInfo(discriminator="type"),
]
