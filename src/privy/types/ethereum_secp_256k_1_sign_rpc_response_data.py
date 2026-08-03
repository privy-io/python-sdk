# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .hex import Hex
from .._models import BaseModel

__all__ = ["EthereumSecp256k1SignRpcResponseData"]


class EthereumSecp256k1SignRpcResponseData(BaseModel):
    """Data returned by the EVM `secp256k1_sign` RPC."""

    encoding: Literal["hex"]

    signature: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """
