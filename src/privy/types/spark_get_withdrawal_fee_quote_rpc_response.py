# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_coop_exit_fee_quote import SparkCoopExitFeeQuote

__all__ = ["SparkGetWithdrawalFeeQuoteRpcResponse"]


class SparkGetWithdrawalFeeQuoteRpcResponse(BaseModel):
    """Response to the Spark `getWithdrawalFeeQuote` RPC."""

    method: Literal["getWithdrawalFeeQuote"]

    data: Optional[SparkCoopExitFeeQuote] = None
    """A fee quote for a cooperative exit from Spark to Bitcoin L1."""
