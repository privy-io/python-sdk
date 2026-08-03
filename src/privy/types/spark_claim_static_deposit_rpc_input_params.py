# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SparkClaimStaticDepositRpcInputParams"]


class SparkClaimStaticDepositRpcInputParams(BaseModel):
    """Parameters for the Spark `claimStaticDeposit` RPC."""

    credit_amount_sats: float

    signature: str

    transaction_id: str

    output_index: Optional[float] = None
