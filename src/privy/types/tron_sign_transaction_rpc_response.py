# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tron_sign_transaction_rpc_response_data import TronSignTransactionRpcResponseData

__all__ = ["TronSignTransactionRpcResponse"]


class TronSignTransactionRpcResponse(BaseModel):
    """Response to the Tron `tron_signTransaction` RPC."""

    data: TronSignTransactionRpcResponseData
    """Data returned by the Tron `tron_signTransaction` RPC."""

    method: Literal["tron_signTransaction"]
