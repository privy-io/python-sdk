# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SolanaSignTransactionRpcResponseData"]


class SolanaSignTransactionRpcResponseData(BaseModel):
    """Data returned by the SVM `signTransaction` RPC."""

    encoding: Literal["base64"]

    signed_transaction: str
