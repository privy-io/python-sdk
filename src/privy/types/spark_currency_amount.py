# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkCurrencyAmount"]


class SparkCurrencyAmount(BaseModel):
    """A currency amount with its original value and unit."""

    original_unit: str

    original_value: float
