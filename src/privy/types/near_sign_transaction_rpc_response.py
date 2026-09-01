# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .near_sign_transaction_rpc_response_data import NearSignTransactionRpcResponseData

__all__ = ["NearSignTransactionRpcResponse"]


class NearSignTransactionRpcResponse(BaseModel):
    """Response to the NEAR `near_signTransaction` RPC."""

    data: NearSignTransactionRpcResponseData
    """Data returned by the NEAR `near_signTransaction` RPC."""

    method: Literal["near_signTransaction"]
