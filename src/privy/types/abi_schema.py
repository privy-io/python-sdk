# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .abi_parameter import AbiParameter

__all__ = ["AbiSchema", "AbiSchemaItem"]


class AbiSchemaItem(BaseModel):
    type: Literal["function", "constructor", "event", "fallback", "receive"]

    anonymous: Optional[bool] = None

    inputs: Optional[List[AbiParameter]] = None

    name: Optional[str] = None

    outputs: Optional[List[AbiParameter]] = None

    state_mutability: Optional[Literal["pure", "view", "nonpayable", "payable"]] = FieldInfo(
        alias="stateMutability", default=None
    )


AbiSchema: TypeAlias = List[AbiSchemaItem]
