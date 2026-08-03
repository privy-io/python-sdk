# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["UserSearchParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    search_term: Required[Annotated[str, PropertyInfo(alias="searchTerm")]]


class Variant1(TypedDict, total=False):
    emails: Required[SequenceNotStr[str]]

    phone_numbers: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="phoneNumbers")]]

    wallet_addresses: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="walletAddresses")]]


UserSearchParams: TypeAlias = Union[Variant0, Variant1]
