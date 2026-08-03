# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_get_withdrawal_fee_quote_rpc_input_params import SparkGetWithdrawalFeeQuoteRpcInputParams

__all__ = ["SparkGetWithdrawalFeeQuoteRpcInput"]


class SparkGetWithdrawalFeeQuoteRpcInput(BaseModel):
    """Gets a fee quote for withdrawing from Spark to a Bitcoin L1 address."""

    method: Literal["getWithdrawalFeeQuote"]

    params: SparkGetWithdrawalFeeQuoteRpcInputParams
    """Parameters for the Spark `getWithdrawalFeeQuote` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
