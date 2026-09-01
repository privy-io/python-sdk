# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .near_unsigned_transaction_borsh_base_64 import NearUnsignedTransactionBorshBase64

__all__ = ["NearSignTransactionRpcRequestBodyParamsParam"]


class NearSignTransactionRpcRequestBodyParamsParam(TypedDict, total=False):
    """Parameters for the NEAR `near_signTransaction` RPC."""

    transaction: Required[NearUnsignedTransactionBorshBase64]
    """A non-empty, base64-encoded Borsh NEAR Transaction."""
