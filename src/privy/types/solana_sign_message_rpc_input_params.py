# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SolanaSignMessageRpcInputParams"]


class SolanaSignMessageRpcInputParams(BaseModel):
    """Parameters for the SVM `signMessage` RPC."""

    encoding: Literal["base64"]

    message: str
