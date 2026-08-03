# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_get_claim_static_deposit_quote_rpc_input_params import SparkGetClaimStaticDepositQuoteRpcInputParams

__all__ = ["SparkGetClaimStaticDepositQuoteRpcInput"]


class SparkGetClaimStaticDepositQuoteRpcInput(BaseModel):
    """Gets a quote for claiming a static deposit."""

    method: Literal["getClaimStaticDepositQuote"]

    params: SparkGetClaimStaticDepositQuoteRpcInputParams
    """Parameters for the Spark `getClaimStaticDepositQuote` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
