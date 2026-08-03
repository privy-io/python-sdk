# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .spark_exit_speed import SparkExitSpeed

__all__ = ["SparkWithdrawRpcInputParams"]


class SparkWithdrawRpcInputParams(BaseModel):
    """Parameters for the Spark `withdraw` RPC."""

    exit_speed: SparkExitSpeed
    """The exit speed for a cooperative withdrawal from Spark to L1."""

    onchain_address: str

    amount_sats: Optional[float] = None

    deduct_fee_from_withdrawal_amount: Optional[bool] = None

    fee_amount_sats: Optional[float] = None

    fee_quote_id: Optional[str] = None
