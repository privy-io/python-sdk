# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tron_hex_address import TronHexAddress

__all__ = ["TronTriggerSmartContract"]


class TronTriggerSmartContract(BaseModel):
    """Tron smart contract call (TRC-20 transfers and general contract interactions)."""

    contract_address: TronHexAddress
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    owner_address: TronHexAddress
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    type: Literal["TriggerSmartContract"]

    call_token_value: Optional[int] = None

    call_value: Optional[int] = None

    data: Optional[str] = None

    token_id: Optional[int] = None
