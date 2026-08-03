# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_send_transaction_rpc_response_data import EthereumSendTransactionRpcResponseData

__all__ = ["EthereumSendTransactionRpcResponse"]


class EthereumSendTransactionRpcResponse(BaseModel):
    """Response to the EVM `eth_sendTransaction` RPC."""

    data: EthereumSendTransactionRpcResponseData
    """Data returned by the EVM `eth_sendTransaction` RPC."""

    method: Literal["eth_sendTransaction"]
