# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .raw_sign_bytes_encoding import RawSignBytesEncoding
from .raw_sign_bytes_hash_function import RawSignBytesHashFunction

__all__ = ["RawSignBytesParams"]


class RawSignBytesParams(TypedDict, total=False):
    """Parameters for hashing and signing bytes with the `raw_sign` RPC."""

    bytes: Required[str]
    """The bytes to hash and sign."""

    encoding: Required[RawSignBytesEncoding]
    """Encoding scheme for bytes in the `raw_sign` RPC."""

    hash_function: Required[RawSignBytesHashFunction]
    """Hash function for bytes in the `raw_sign` RPC."""
