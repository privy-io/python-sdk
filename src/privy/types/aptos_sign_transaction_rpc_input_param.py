# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .aptos_sign_transaction_rpc_input_params_param import AptosSignTransactionRpcInputParamsParam

__all__ = ["AptosSignTransactionRpcInputParam"]


class AptosSignTransactionRpcInputParam(TypedDict, total=False):
    """
    Executes the Aptos `aptos_signTransaction` RPC to sign a legacy single-signer Ed25519 RawTransaction. The caller is responsible for broadcasting.
    """

    method: Required[Literal["aptos_signTransaction"]]

    params: Required[AptosSignTransactionRpcInputParamsParam]
    """Parameters for the Aptos `aptos_signTransaction` RPC."""
