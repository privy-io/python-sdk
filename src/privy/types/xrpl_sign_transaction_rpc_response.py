# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .xrpl_sign_transaction_rpc_response_data import XrplSignTransactionRpcResponseData

__all__ = ["XrplSignTransactionRpcResponse"]


class XrplSignTransactionRpcResponse(BaseModel):
    """Response to the XRPL `xrpl_signTransaction` RPC."""

    data: XrplSignTransactionRpcResponseData
    """Data returned by the XRPL `xrpl_signTransaction` RPC."""

    method: Literal["xrpl_signTransaction"]
