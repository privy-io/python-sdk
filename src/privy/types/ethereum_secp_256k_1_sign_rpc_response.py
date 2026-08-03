# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_secp_256k_1_sign_rpc_response_data import EthereumSecp256k1SignRpcResponseData

__all__ = ["EthereumSecp256k1SignRpcResponse"]


class EthereumSecp256k1SignRpcResponse(BaseModel):
    """Response to the EVM `secp256k1_sign` RPC."""

    data: EthereumSecp256k1SignRpcResponseData
    """Data returned by the EVM `secp256k1_sign` RPC."""

    method: Literal["secp256k1_sign"]
