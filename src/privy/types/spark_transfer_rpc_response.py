# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_transfer import SparkTransfer

__all__ = ["SparkTransferRpcResponse"]


class SparkTransferRpcResponse(BaseModel):
    """Response to the Spark `transfer` RPC."""

    method: Literal["transfer"]

    data: Optional[SparkTransfer] = None
    """A Spark transfer."""
