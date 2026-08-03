# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .quantity_param import QuantityParam
from .user_operation_input_param import UserOperationInputParam

__all__ = ["EthereumSignUserOperationRpcInputParamsParam"]


class EthereumSignUserOperationRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the EVM `eth_signUserOperation` RPC."""

    chain_id: Required[QuantityParam]
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    contract: Required[str]

    user_operation: Required[UserOperationInputParam]
    """An ERC-4337 user operation."""
