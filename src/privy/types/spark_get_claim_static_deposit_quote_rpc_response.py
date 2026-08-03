# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_get_claim_static_deposit_quote_rpc_response_data import SparkGetClaimStaticDepositQuoteRpcResponseData

__all__ = ["SparkGetClaimStaticDepositQuoteRpcResponse"]


class SparkGetClaimStaticDepositQuoteRpcResponse(BaseModel):
    """Response to the Spark `getClaimStaticDepositQuote` RPC."""

    method: Literal["getClaimStaticDepositQuote"]

    data: Optional[SparkGetClaimStaticDepositQuoteRpcResponseData] = None
    """Data returned by the Spark `getClaimStaticDepositQuote` RPC."""
