# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SolanaSignMessageRpcResponseData"]


class SolanaSignMessageRpcResponseData(BaseModel):
    """Data returned by the SVM `signMessage` RPC."""

    encoding: Literal["base64"]

    signature: str
