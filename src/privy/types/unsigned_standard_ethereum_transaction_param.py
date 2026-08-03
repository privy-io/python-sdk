# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .hex import Hex
from .quantity_param import QuantityParam
from .ethereum_sign_7702_authorization_param import EthereumSign7702AuthorizationParam

__all__ = ["UnsignedStandardEthereumTransactionParam"]

_UnsignedStandardEthereumTransactionParamReservedKeywords = TypedDict(
    "_UnsignedStandardEthereumTransactionParamReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class UnsignedStandardEthereumTransactionParam(_UnsignedStandardEthereumTransactionParamReservedKeywords, total=False):
    """An unsigned standard Ethereum transaction object.

    Supports EVM transaction types 0, 1, 2, and 4.
    """

    authorization_list: Iterable[EthereumSign7702AuthorizationParam]

    chain_id: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    data: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    gas_limit: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    gas_price: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_fee_per_gas: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_priority_fee_per_gas: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    nonce: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    to: str

    type: Literal[0, 1, 2, 4]

    value: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
