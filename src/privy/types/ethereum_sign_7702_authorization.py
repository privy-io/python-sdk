# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .hex import Hex
from .._models import BaseModel
from .quantity import Quantity

__all__ = ["EthereumSign7702Authorization"]


class EthereumSign7702Authorization(BaseModel):
    """
    A signed EIP-7702 authorization that delegates code execution to a contract address.
    """

    chain_id: Quantity
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    contract: str

    nonce: Quantity
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    r: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    s: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    y_parity: float
