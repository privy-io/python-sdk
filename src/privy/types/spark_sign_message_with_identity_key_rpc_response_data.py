# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkSignMessageWithIdentityKeyRpcResponseData"]


class SparkSignMessageWithIdentityKeyRpcResponseData(BaseModel):
    """Data returned by the Spark `signMessageWithIdentityKey` RPC."""

    signature: str
