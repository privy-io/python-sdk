# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_sign_message_with_identity_key_rpc_response_data import SparkSignMessageWithIdentityKeyRpcResponseData

__all__ = ["SparkSignMessageWithIdentityKeyRpcResponse"]


class SparkSignMessageWithIdentityKeyRpcResponse(BaseModel):
    """Response to the Spark `signMessageWithIdentityKey` RPC."""

    method: Literal["signMessageWithIdentityKey"]

    data: Optional[SparkSignMessageWithIdentityKeyRpcResponseData] = None
    """Data returned by the Spark `signMessageWithIdentityKey` RPC."""
