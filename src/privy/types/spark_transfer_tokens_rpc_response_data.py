# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkTransferTokensRpcResponseData"]


class SparkTransferTokensRpcResponseData(BaseModel):
    """Data returned by the Spark `transferTokens` RPC."""

    id: str
