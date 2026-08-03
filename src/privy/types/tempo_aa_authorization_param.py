# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .hex import Hex
from .quantity_param import QuantityParam

__all__ = ["TempoAaAuthorizationParam"]


class TempoAaAuthorizationParam(TypedDict, total=False):
    """An AA authorization for Tempo transactions with P256/WebAuthn signatures."""

    chain_id: Required[QuantityParam]
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    contract: Required[str]

    nonce: Required[QuantityParam]
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    signature: Required[Hex]
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """
