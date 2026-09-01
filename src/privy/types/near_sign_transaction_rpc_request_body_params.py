# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .near_unsigned_transaction_borsh_base_64 import NearUnsignedTransactionBorshBase64

__all__ = ["NearSignTransactionRpcRequestBodyParams"]


class NearSignTransactionRpcRequestBodyParams(BaseModel):
    """Parameters for the NEAR `near_signTransaction` RPC."""

    transaction: NearUnsignedTransactionBorshBase64
    """A non-empty, base64-encoded Borsh NEAR Transaction."""
