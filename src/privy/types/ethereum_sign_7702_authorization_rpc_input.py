# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_7702_authorization_rpc_input_params import EthereumSign7702AuthorizationRpcInputParams

__all__ = ["EthereumSign7702AuthorizationRpcInput"]


class EthereumSign7702AuthorizationRpcInput(BaseModel):
    """Signs an EIP-7702 authorization."""

    method: Literal["eth_sign7702Authorization"]

    params: EthereumSign7702AuthorizationRpcInputParams
    """Parameters for the EVM `eth_sign7702Authorization` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["ethereum"]] = None

    wallet_id: Optional[str] = None
