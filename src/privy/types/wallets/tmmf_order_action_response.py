# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .tmmf_deposit_action_response import TmmfDepositActionResponse
from .tmmf_withdraw_action_response import TmmfWithdrawActionResponse

__all__ = ["TmmfOrderActionResponse"]

TmmfOrderActionResponse: TypeAlias = Annotated[
    Union[TmmfDepositActionResponse, TmmfWithdrawActionResponse], PropertyInfo(discriminator="type")
]
