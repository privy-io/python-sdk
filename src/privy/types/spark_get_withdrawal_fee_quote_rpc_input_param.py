# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_get_withdrawal_fee_quote_rpc_input_params_param import SparkGetWithdrawalFeeQuoteRpcInputParamsParam

__all__ = ["SparkGetWithdrawalFeeQuoteRpcInputParam"]


class SparkGetWithdrawalFeeQuoteRpcInputParam(TypedDict, total=False):
    """Gets a fee quote for withdrawing from Spark to a Bitcoin L1 address."""

    method: Required[Literal["getWithdrawalFeeQuote"]]

    params: Required[SparkGetWithdrawalFeeQuoteRpcInputParamsParam]
    """Parameters for the Spark `getWithdrawalFeeQuote` RPC."""

    network: SparkNetwork
    """The Spark network."""
