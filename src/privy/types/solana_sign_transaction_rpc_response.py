# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .solana_sign_transaction_rpc_response_data import SolanaSignTransactionRpcResponseData

__all__ = ["SolanaSignTransactionRpcResponse"]


class SolanaSignTransactionRpcResponse(BaseModel):
    """Response to the SVM `signTransaction` RPC."""

    data: SolanaSignTransactionRpcResponseData
    """Data returned by the SVM `signTransaction` RPC."""

    method: Literal["signTransaction"]
