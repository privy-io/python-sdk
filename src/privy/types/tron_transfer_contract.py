# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tron_hex_address import TronHexAddress

__all__ = ["TronTransferContract"]


class TronTransferContract(BaseModel):
    """Tron native TRX transfer contract."""

    amount: int

    owner_address: TronHexAddress
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    to_address: TronHexAddress
    """
    Tron address in hex format: 41-prefixed, 42 hex characters (21 bytes), no 0x
    prefix.
    """

    type: Literal["TransferContract"]
