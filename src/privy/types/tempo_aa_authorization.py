# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .hex import Hex
from .._models import BaseModel
from .quantity import Quantity

__all__ = ["TempoAaAuthorization"]


class TempoAaAuthorization(BaseModel):
    """An AA authorization for Tempo transactions with P256/WebAuthn signatures."""

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

    signature: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """
