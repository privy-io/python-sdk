# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tron_hex_address import TronHexAddress

__all__ = ["TronTransferContractParam"]


class TronTransferContractParam(TypedDict, total=False):
    """Tron native TRX transfer contract."""

    amount: Required[int]

    owner_address: Required[TronHexAddress]
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    to_address: Required[TronHexAddress]
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    type: Required[Literal["TransferContract"]]
