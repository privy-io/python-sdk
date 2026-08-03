# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .abi_parameter_param import AbiParameterParam

__all__ = ["AbiSchemaParam", "AbiSchemaParamItem"]


class AbiSchemaParamItem(TypedDict, total=False):
    type: Required[Literal["function", "constructor", "event", "fallback", "receive"]]

    anonymous: bool

    inputs: Iterable[AbiParameterParam]

    name: str

    outputs: Iterable[AbiParameterParam]

    state_mutability: Annotated[Literal["pure", "view", "nonpayable", "payable"], PropertyInfo(alias="stateMutability")]


AbiSchemaParam: TypeAlias = List[AbiSchemaParamItem]
