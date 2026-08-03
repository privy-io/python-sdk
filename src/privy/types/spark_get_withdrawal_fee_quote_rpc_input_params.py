# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkGetWithdrawalFeeQuoteRpcInputParams"]


class SparkGetWithdrawalFeeQuoteRpcInputParams(BaseModel):
    """Parameters for the Spark `getWithdrawalFeeQuote` RPC."""

    amount_sats: float

    onchain_address: str
