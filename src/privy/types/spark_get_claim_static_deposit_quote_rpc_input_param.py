# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_get_claim_static_deposit_quote_rpc_input_params_param import (
    SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
)

__all__ = ["SparkGetClaimStaticDepositQuoteRpcInputParam"]


class SparkGetClaimStaticDepositQuoteRpcInputParam(TypedDict, total=False):
    """Gets a quote for claiming a static deposit."""

    method: Required[Literal["getClaimStaticDepositQuote"]]

    params: Required[SparkGetClaimStaticDepositQuoteRpcInputParamsParam]
    """Parameters for the Spark `getClaimStaticDepositQuote` RPC."""

    network: SparkNetwork
    """The Spark network."""
