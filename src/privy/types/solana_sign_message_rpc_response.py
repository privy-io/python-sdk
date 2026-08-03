# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .solana_sign_message_rpc_response_data import SolanaSignMessageRpcResponseData

__all__ = ["SolanaSignMessageRpcResponse"]


class SolanaSignMessageRpcResponse(BaseModel):
    """Response to the SVM `signMessage` RPC."""

    data: SolanaSignMessageRpcResponseData
    """Data returned by the SVM `signMessage` RPC."""

    method: Literal["signMessage"]
