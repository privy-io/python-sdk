# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .hex import Hex
from .._types import SequenceNotStr

__all__ = ["AccessListEntryParam"]


class AccessListEntryParam(TypedDict, total=False):
    """
    An entry in an EIP-2930 access list, specifying an address and its storage keys.
    """

    address: Required[str]

    storage_keys: Required[SequenceNotStr[Hex]]
