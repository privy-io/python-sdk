# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .hex import Hex
from .quantity_param import QuantityParam

__all__ = ["EthereumSign7702AuthorizationParam"]


class EthereumSign7702AuthorizationParam(TypedDict, total=False):
    """
    A signed EIP-7702 authorization that delegates code execution to a contract address.
    """

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

    y_parity: Required[float]
