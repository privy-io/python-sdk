# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["IntentType"]

IntentType: TypeAlias = Union[
    Literal["CONDITION_SET_ITEM", "KEY_QUORUM", "POLICY", "RAW_SIGN", "RULE", "RPC", "TRANSFER", "WALLET"], str
]
