# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .hex import Hex
from .._models import BaseModel

__all__ = ["AccessListEntry"]


class AccessListEntry(BaseModel):
    """
    An entry in an EIP-2930 access list, specifying an address and its storage keys.
    """

    address: str

    storage_keys: List[Hex]
