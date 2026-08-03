# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_user_operation_rpc_response_data import EthereumSignUserOperationRpcResponseData

__all__ = ["EthereumSignUserOperationRpcResponse"]


class EthereumSignUserOperationRpcResponse(BaseModel):
    """Response to the EVM `eth_signUserOperation` RPC."""

    data: EthereumSignUserOperationRpcResponseData
    """Data returned by the EVM `eth_signUserOperation` RPC."""

    method: Literal["eth_signUserOperation"]
