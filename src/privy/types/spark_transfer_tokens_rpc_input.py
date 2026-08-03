# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_transfer_tokens_rpc_input_params import SparkTransferTokensRpcInputParams

__all__ = ["SparkTransferTokensRpcInput"]


class SparkTransferTokensRpcInput(BaseModel):
    """Transfers tokens to a Spark address."""

    method: Literal["transferTokens"]

    params: SparkTransferTokensRpcInputParams
    """Parameters for the Spark `transferTokens` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
