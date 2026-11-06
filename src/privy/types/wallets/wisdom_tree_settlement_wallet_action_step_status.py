# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["WisdomTreeSettlementWalletActionStepStatus"]

WisdomTreeSettlementWalletActionStepStatus: TypeAlias = Union[
    Literal["preparing", "queued", "pending", "confirmed", "rejected", "failed"], str
]
