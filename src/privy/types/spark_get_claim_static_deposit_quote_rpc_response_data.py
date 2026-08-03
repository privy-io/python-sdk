# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkGetClaimStaticDepositQuoteRpcResponseData"]


class SparkGetClaimStaticDepositQuoteRpcResponseData(BaseModel):
    """Data returned by the Spark `getClaimStaticDepositQuote` RPC."""

    credit_amount_sats: float

    network: str

    output_index: float

    signature: str

    transaction_id: str
