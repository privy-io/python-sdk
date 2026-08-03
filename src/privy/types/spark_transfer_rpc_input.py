# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_transfer_rpc_input_params import SparkTransferRpcInputParams

__all__ = ["SparkTransferRpcInput"]


class SparkTransferRpcInput(BaseModel):
    """Transfers satoshis to a Spark address."""

    method: Literal["transfer"]

    params: SparkTransferRpcInputParams
    """Parameters for the Spark `transfer` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
