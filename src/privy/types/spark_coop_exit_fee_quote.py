# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .spark_currency_amount import SparkCurrencyAmount

__all__ = ["SparkCoopExitFeeQuote"]


class SparkCoopExitFeeQuote(BaseModel):
    """A fee quote for a cooperative exit from Spark to Bitcoin L1."""

    id: str

    created_at: str

    expires_at: str

    l1_broadcast_fee_fast: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    l1_broadcast_fee_medium: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    l1_broadcast_fee_slow: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    network: str

    total_amount: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    updated_at: str

    user_fee_fast: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    user_fee_medium: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    user_fee_slow: SparkCurrencyAmount
    """A currency amount with its original value and unit."""
