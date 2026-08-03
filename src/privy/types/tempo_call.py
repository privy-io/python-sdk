# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .hex import Hex
from .._models import BaseModel
from .quantity import Quantity

__all__ = ["TempoCall"]


class TempoCall(BaseModel):
    """A single call within a Tempo batched transaction."""

    to: str

    data: Optional[Hex] = None
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    value: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
