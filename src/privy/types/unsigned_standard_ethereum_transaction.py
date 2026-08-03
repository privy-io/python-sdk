# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .hex import Hex
from .._models import BaseModel
from .quantity import Quantity
from .ethereum_sign_7702_authorization import EthereumSign7702Authorization

__all__ = ["UnsignedStandardEthereumTransaction"]


class UnsignedStandardEthereumTransaction(BaseModel):
    """An unsigned standard Ethereum transaction object.

    Supports EVM transaction types 0, 1, 2, and 4.
    """

    authorization_list: Optional[List[EthereumSign7702Authorization]] = None

    chain_id: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    data: Optional[Hex] = None
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    gas_limit: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    gas_price: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_fee_per_gas: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_priority_fee_per_gas: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    nonce: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    to: Optional[str] = None

    type: Optional[Literal[0, 1, 2, 4]] = None

    value: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
