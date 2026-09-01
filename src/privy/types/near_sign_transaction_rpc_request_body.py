# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .near_sign_transaction_rpc_request_body_params import NearSignTransactionRpcRequestBodyParams

__all__ = ["NearSignTransactionRpcRequestBody"]


class NearSignTransactionRpcRequestBody(BaseModel):
    """Executes the NEAR `near_signTransaction` RPC to sign a transaction.

    The caller is responsible for broadcasting.
    """

    method: Literal["near_signTransaction"]

    params: NearSignTransactionRpcRequestBodyParams
    """Parameters for the NEAR `near_signTransaction` RPC."""
