# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_7702_authorization_rpc_response_data import EthereumSign7702AuthorizationRpcResponseData

__all__ = ["EthereumSign7702AuthorizationRpcResponse"]


class EthereumSign7702AuthorizationRpcResponse(BaseModel):
    """Response to the EVM `eth_sign7702Authorization` RPC."""

    data: EthereumSign7702AuthorizationRpcResponseData
    """Data returned by the EVM `eth_sign7702Authorization` RPC."""

    method: Literal["eth_sign7702Authorization"]
