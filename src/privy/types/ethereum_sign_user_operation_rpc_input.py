# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_user_operation_rpc_input_params import EthereumSignUserOperationRpcInputParams

__all__ = ["EthereumSignUserOperationRpcInput"]


class EthereumSignUserOperationRpcInput(BaseModel):
    """Executes an RPC method to hash and sign a UserOperation."""

    method: Literal["eth_signUserOperation"]

    params: EthereumSignUserOperationRpcInputParams
    """Parameters for the EVM `eth_signUserOperation` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["ethereum"]] = None

    wallet_id: Optional[str] = None
