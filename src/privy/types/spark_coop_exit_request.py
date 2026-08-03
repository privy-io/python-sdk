# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .spark_exit_speed import SparkExitSpeed
from .spark_currency_amount import SparkCurrencyAmount

__all__ = ["SparkCoopExitRequest"]


class SparkCoopExitRequest(BaseModel):
    """A cooperative exit request from Spark to Bitcoin L1."""

    id: str

    coop_exit_txid: str

    created_at: str

    expires_at: str

    fee: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    l1_broadcast_fee: SparkCurrencyAmount
    """A currency amount with its original value and unit."""

    network: str

    status: str

    updated_at: str

    exit_speed: Optional[SparkExitSpeed] = None
    """The exit speed for a cooperative withdrawal from Spark to L1."""

    fee_quote_id: Optional[str] = None
