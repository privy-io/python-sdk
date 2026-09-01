# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .near_signed_transaction_borsh_base_64 import NearSignedTransactionBorshBase64

__all__ = ["NearSignTransactionRpcResponseData"]


class NearSignTransactionRpcResponseData(BaseModel):
    """Data returned by the NEAR `near_signTransaction` RPC."""

    encoding: Literal["base64"]

    signed_transaction: NearSignedTransactionBorshBase64
    """A non-empty, base64-encoded NEAR Ed25519 SignedTransaction."""
