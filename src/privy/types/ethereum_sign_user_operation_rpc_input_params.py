# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .quantity import Quantity
from .user_operation_input import UserOperationInput

__all__ = ["EthereumSignUserOperationRpcInputParams"]


class EthereumSignUserOperationRpcInputParams(BaseModel):
    """Parameters for the EVM `eth_signUserOperation` RPC."""

    chain_id: Quantity
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    contract: str

    user_operation: UserOperationInput
    """An ERC-4337 user operation."""
