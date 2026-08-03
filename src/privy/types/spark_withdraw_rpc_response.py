# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_coop_exit_request import SparkCoopExitRequest

__all__ = ["SparkWithdrawRpcResponse"]


class SparkWithdrawRpcResponse(BaseModel):
    """Response to the Spark `withdraw` RPC."""

    method: Literal["withdraw"]

    data: Optional[SparkCoopExitRequest] = None
    """A cooperative exit request from Spark to Bitcoin L1."""
