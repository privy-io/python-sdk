# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_claim_static_deposit_rpc_response_data import SparkClaimStaticDepositRpcResponseData

__all__ = ["SparkClaimStaticDepositRpcResponse"]


class SparkClaimStaticDepositRpcResponse(BaseModel):
    """Response to the Spark `claimStaticDeposit` RPC."""

    method: Literal["claimStaticDeposit"]

    data: Optional[SparkClaimStaticDepositRpcResponseData] = None
    """Data returned by the Spark `claimStaticDeposit` RPC."""
