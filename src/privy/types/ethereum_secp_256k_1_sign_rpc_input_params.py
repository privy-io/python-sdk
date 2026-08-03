# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .hex import Hex
from .._models import BaseModel

__all__ = ["EthereumSecp256k1SignRpcInputParams"]


class EthereumSecp256k1SignRpcInputParams(BaseModel):
    """Parameters for the EVM `secp256k1_sign` RPC."""

    hash: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """
