# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .quantity import Quantity

__all__ = ["EthereumSign7702AuthorizationRpcInputParams"]


class EthereumSign7702AuthorizationRpcInputParams(BaseModel):
    """Parameters for the EVM `eth_sign7702Authorization` RPC."""

    chain_id: Quantity
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    contract: str

    executor: Optional[Literal["self"]] = None

    nonce: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
