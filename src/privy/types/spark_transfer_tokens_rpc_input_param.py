# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_transfer_tokens_rpc_input_params_param import SparkTransferTokensRpcInputParamsParam

__all__ = ["SparkTransferTokensRpcInputParam"]


class SparkTransferTokensRpcInputParam(TypedDict, total=False):
    """Transfers tokens to a Spark address."""

    method: Required[Literal["transferTokens"]]

    params: Required[SparkTransferTokensRpcInputParamsParam]
    """Parameters for the Spark `transferTokens` RPC."""

    network: SparkNetwork
    """The Spark network."""
