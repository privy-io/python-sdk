# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_transfer_tokens_rpc_response_data import SparkTransferTokensRpcResponseData

__all__ = ["SparkTransferTokensRpcResponse"]


class SparkTransferTokensRpcResponse(BaseModel):
    """Response to the Spark `transferTokens` RPC."""

    method: Literal["transferTokens"]

    data: Optional[SparkTransferTokensRpcResponseData] = None
    """Data returned by the Spark `transferTokens` RPC."""
