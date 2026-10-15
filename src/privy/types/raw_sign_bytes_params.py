# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .raw_sign_bytes_encoding import RawSignBytesEncoding
from .raw_sign_bytes_hash_function import RawSignBytesHashFunction

__all__ = ["RawSignBytesParams"]


class RawSignBytesParams(BaseModel):
    """Parameters for hashing and signing bytes with the `raw_sign` RPC."""

    bytes: str
    """The bytes to hash and sign."""

    encoding: RawSignBytesEncoding
    """Encoding scheme for bytes in the `raw_sign` RPC."""

    hash_function: RawSignBytesHashFunction
    """Hash function for bytes in the `raw_sign` RPC."""
