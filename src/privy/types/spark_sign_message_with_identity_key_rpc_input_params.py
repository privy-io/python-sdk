# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SparkSignMessageWithIdentityKeyRpcInputParams"]


class SparkSignMessageWithIdentityKeyRpcInputParams(BaseModel):
    """Parameters for the Spark `signMessageWithIdentityKey` RPC."""

    message: str

    compact: Optional[bool] = None
