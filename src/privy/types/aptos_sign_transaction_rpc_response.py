# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .aptos_sign_transaction_rpc_response_data import AptosSignTransactionRpcResponseData

__all__ = ["AptosSignTransactionRpcResponse"]


class AptosSignTransactionRpcResponse(BaseModel):
    """Response to the Aptos `aptos_signTransaction` RPC."""

    data: AptosSignTransactionRpcResponseData
    """Data returned by the Aptos `aptos_signTransaction` RPC."""

    method: Literal["aptos_signTransaction"]
