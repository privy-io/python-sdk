# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .solana_sign_and_send_transaction_rpc_response_data import SolanaSignAndSendTransactionRpcResponseData

__all__ = ["SolanaSignAndSendTransactionRpcResponse"]


class SolanaSignAndSendTransactionRpcResponse(BaseModel):
    """Response to the SVM `signAndSendTransaction` RPC."""

    data: SolanaSignAndSendTransactionRpcResponseData
    """Data returned by the SVM `signAndSendTransaction` RPC."""

    method: Literal["signAndSendTransaction"]
