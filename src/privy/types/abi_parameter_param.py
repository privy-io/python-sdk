# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AbiParameterParam"]


class AbiParameterParam(TypedDict, total=False):
    """A parameter in a Solidity ABI function or event definition."""

    type: Required[str]

    components: Iterable[Dict[str, object]]

    indexed: bool

    internal_type: Annotated[str, PropertyInfo(alias="internalType")]

    name: str
