# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tron_send_transaction_rpc_response_data import TronSendTransactionRpcResponseData

__all__ = ["TronSendTransactionRpcResponse"]


class TronSendTransactionRpcResponse(BaseModel):
    """Response to the Tron `tron_sendTransaction` RPC."""

    data: TronSendTransactionRpcResponseData
    """Data returned by the Tron `tron_sendTransaction` RPC."""

    method: Literal["tron_sendTransaction"]
