# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SparkGetClaimStaticDepositQuoteRpcInputParams"]


class SparkGetClaimStaticDepositQuoteRpcInputParams(BaseModel):
    """Parameters for the Spark `getClaimStaticDepositQuote` RPC."""

    transaction_id: str

    output_index: Optional[float] = None
