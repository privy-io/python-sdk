# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_balance import SparkBalance

__all__ = ["SparkGetBalanceRpcResponse"]


class SparkGetBalanceRpcResponse(BaseModel):
    """Response to the Spark `getBalance` RPC."""

    method: Literal["getBalance"]

    data: Optional[SparkBalance] = None
    """The balance of a Spark wallet."""
