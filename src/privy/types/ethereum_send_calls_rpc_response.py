# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_send_calls_rpc_response_data import EthereumSendCallsRpcResponseData

__all__ = ["EthereumSendCallsRpcResponse"]


class EthereumSendCallsRpcResponse(BaseModel):
    """Response to the `wallet_sendCalls` RPC."""

    data: EthereumSendCallsRpcResponseData
    """Data returned by the `wallet_sendCalls` RPC."""

    method: Literal["wallet_sendCalls"]
