# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .ethereum_sign_transaction_rpc_input_params_param import EthereumSignTransactionRpcInputParamsParam

__all__ = ["EthereumSignTransactionRpcInputParam"]


class EthereumSignTransactionRpcInputParam(TypedDict, total=False):
    """Executes the EVM `eth_signTransaction` RPC to sign a transaction."""

    method: Required[Literal["eth_signTransaction"]]

    params: Required[EthereumSignTransactionRpcInputParamsParam]
    """Parameters for the EVM `eth_signTransaction` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    wallet_id: str
