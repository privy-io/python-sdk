# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .solana_sign_message_rpc_input_params_param import SolanaSignMessageRpcInputParamsParam

__all__ = ["SolanaSignMessageRpcInputParam"]


class SolanaSignMessageRpcInputParam(TypedDict, total=False):
    """Executes the SVM `signMessage` RPC to sign a message."""

    method: Required[Literal["signMessage"]]

    params: Required[SolanaSignMessageRpcInputParamsParam]
    """Parameters for the SVM `signMessage` RPC."""

    address: str

    chain_type: Literal["solana"]

    wallet_id: str
