# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tron_hex_address import TronHexAddress

__all__ = ["TronTriggerSmartContractParam"]


class TronTriggerSmartContractParam(TypedDict, total=False):
    """Tron smart contract call (TRC-20 transfers and general contract interactions)."""

    contract_address: Required[TronHexAddress]
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    owner_address: Required[TronHexAddress]
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    type: Required[Literal["TriggerSmartContract"]]

    call_token_value: int

    call_value: int

    data: str

    token_id: int
