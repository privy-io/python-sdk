# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .hex import Hex

__all__ = ["TempoFeePayerSignatureParam"]


class TempoFeePayerSignatureParam(TypedDict, total=False):
    """A fee payer signature for sponsored Tempo transactions (secp256k1 only)."""

    r: Required[Hex]
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    s: Required[Hex]
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    y_parity: Required[Literal[0, 1]]
