# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tron_sign_transaction_rpc_input_params_param import TronSignTransactionRpcInputParamsParam

__all__ = ["TronSignTransactionRpcInputParam"]


class TronSignTransactionRpcInputParam(TypedDict, total=False):
    """Executes the Tron `tron_signTransaction` RPC to sign a transaction.

    The caller is responsible for broadcasting.
    """

    method: Required[Literal["tron_signTransaction"]]

    params: Required[TronSignTransactionRpcInputParamsParam]
    """Parameters for the Tron `tron_signTransaction` RPC."""
