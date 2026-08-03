# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .hex import Hex

__all__ = ["RawSignHashParams"]


class RawSignHashParams(TypedDict, total=False):
    """Parameters for signing a pre-computed hash with the `raw_sign` RPC."""

    hash: Required[Hex]
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """
