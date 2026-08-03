# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .hex import Hex

__all__ = ["EthereumSecp256k1SignRpcInputParamsParam"]


class EthereumSecp256k1SignRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the EVM `secp256k1_sign` RPC."""

    hash: Required[Hex]
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """
