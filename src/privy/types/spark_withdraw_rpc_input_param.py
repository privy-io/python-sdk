# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_withdraw_rpc_input_params_param import SparkWithdrawRpcInputParamsParam

__all__ = ["SparkWithdrawRpcInputParam"]


class SparkWithdrawRpcInputParam(TypedDict, total=False):
    """Withdraws from Spark to a Bitcoin L1 address (cooperative exit)."""

    method: Required[Literal["withdraw"]]

    params: Required[SparkWithdrawRpcInputParamsParam]
    """Parameters for the Spark `withdraw` RPC."""

    network: SparkNetwork
    """The Spark network."""
