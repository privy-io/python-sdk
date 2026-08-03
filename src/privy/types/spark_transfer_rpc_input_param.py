# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_transfer_rpc_input_params_param import SparkTransferRpcInputParamsParam

__all__ = ["SparkTransferRpcInputParam"]


class SparkTransferRpcInputParam(TypedDict, total=False):
    """Transfers satoshis to a Spark address."""

    method: Required[Literal["transfer"]]

    params: Required[SparkTransferRpcInputParamsParam]
    """Parameters for the Spark `transfer` RPC."""

    network: SparkNetwork
    """The Spark network."""
