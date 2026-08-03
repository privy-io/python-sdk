# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_transaction_rpc_response_data import EthereumSignTransactionRpcResponseData

__all__ = ["EthereumSignTransactionRpcResponse"]


class EthereumSignTransactionRpcResponse(BaseModel):
    """Response to the EVM `eth_signTransaction` RPC."""

    data: EthereumSignTransactionRpcResponseData
    """Data returned by the EVM `eth_signTransaction` RPC."""

    method: Literal["eth_signTransaction"]
