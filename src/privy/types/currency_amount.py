# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CurrencyAmount"]


class CurrencyAmount(BaseModel):
    """A monetary value with its currency denomination."""

    currency: Literal["usd"]
    """Currency code"""

    value: str
    """The monetary value as a string."""
