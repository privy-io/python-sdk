# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .solana_sign_transaction_rpc_input_params_param import SolanaSignTransactionRpcInputParamsParam

__all__ = ["SolanaSignTransactionRpcInputParam"]


class SolanaSignTransactionRpcInputParam(TypedDict, total=False):
    """Executes the SVM `signTransaction` RPC to sign a transaction."""

    method: Required[Literal["signTransaction"]]

    params: Required[SolanaSignTransactionRpcInputParamsParam]
    """Parameters for the SVM `signTransaction` RPC."""

    address: str

    chain_type: Literal["solana"]

    wallet_id: str
