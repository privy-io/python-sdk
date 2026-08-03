# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_withdraw_rpc_input_params import SparkWithdrawRpcInputParams

__all__ = ["SparkWithdrawRpcInput"]


class SparkWithdrawRpcInput(BaseModel):
    """Withdraws from Spark to a Bitcoin L1 address (cooperative exit)."""

    method: Literal["withdraw"]

    params: SparkWithdrawRpcInputParams
    """Parameters for the Spark `withdraw` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
