# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .hex import Hex

__all__ = ["QuantityParam"]

QuantityParam: TypeAlias = Union[Hex, int]
