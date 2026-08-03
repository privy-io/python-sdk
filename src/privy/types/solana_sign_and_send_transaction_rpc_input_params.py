# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SolanaSignAndSendTransactionRpcInputParams"]


class SolanaSignAndSendTransactionRpcInputParams(BaseModel):
    """Parameters for the SVM `signAndSendTransaction` RPC."""

    encoding: Literal["base64"]

    transaction: str
