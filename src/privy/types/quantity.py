# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .hex import Hex

__all__ = ["Quantity"]

Quantity: TypeAlias = Union[Hex, int]
