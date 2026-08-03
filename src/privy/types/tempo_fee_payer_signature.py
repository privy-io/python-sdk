# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .hex import Hex
from .._models import BaseModel

__all__ = ["TempoFeePayerSignature"]


class TempoFeePayerSignature(BaseModel):
    """A fee payer signature for sponsored Tempo transactions (secp256k1 only)."""

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

    y_parity: Literal[0, 1]
