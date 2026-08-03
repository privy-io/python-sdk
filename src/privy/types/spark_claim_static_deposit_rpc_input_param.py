# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_claim_static_deposit_rpc_input_params_param import SparkClaimStaticDepositRpcInputParamsParam

__all__ = ["SparkClaimStaticDepositRpcInputParam"]


class SparkClaimStaticDepositRpcInputParam(TypedDict, total=False):
    """Claims a static deposit into the Spark wallet."""

    method: Required[Literal["claimStaticDeposit"]]

    params: Required[SparkClaimStaticDepositRpcInputParamsParam]
    """Parameters for the Spark `claimStaticDeposit` RPC."""

    network: SparkNetwork
    """The Spark network."""
