# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .xrpl_sign_transaction_rpc_input_params_param import XrplSignTransactionRpcInputParamsParam

__all__ = ["XrplSignTransactionRpcInputParam"]


class XrplSignTransactionRpcInputParam(TypedDict, total=False):
    """Executes the XRPL `xrpl_signTransaction` RPC to sign a transaction.

    The caller is responsible for broadcasting.
    """

    method: Required[Literal["xrpl_signTransaction"]]

    params: Required[XrplSignTransactionRpcInputParamsParam]
    """Parameters for the XRPL `xrpl_signTransaction` RPC."""
