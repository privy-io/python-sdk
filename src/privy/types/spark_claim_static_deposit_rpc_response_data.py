# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkClaimStaticDepositRpcResponseData"]


class SparkClaimStaticDepositRpcResponseData(BaseModel):
    """Data returned by the Spark `claimStaticDeposit` RPC."""

    transfer_id: str
