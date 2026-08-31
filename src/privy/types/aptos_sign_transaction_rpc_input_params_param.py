# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .aptos_bcs_hex import AptosBcsHex

__all__ = ["AptosSignTransactionRpcInputParamsParam"]


class AptosSignTransactionRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Aptos `aptos_signTransaction` RPC."""

    transaction: Required[AptosBcsHex]
    """A non-empty, 0x-prefixed, even-length BCS hex string."""
