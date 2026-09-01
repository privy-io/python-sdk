# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .near_sign_transaction_rpc_request_body_params_param import NearSignTransactionRpcRequestBodyParamsParam

__all__ = ["NearSignTransactionRpcRequestBodyParam"]


class NearSignTransactionRpcRequestBodyParam(TypedDict, total=False):
    """Executes the NEAR `near_signTransaction` RPC to sign a transaction.

    The caller is responsible for broadcasting.
    """

    method: Required[Literal["near_signTransaction"]]

    params: Required[NearSignTransactionRpcRequestBodyParamsParam]
    """Parameters for the NEAR `near_signTransaction` RPC."""
