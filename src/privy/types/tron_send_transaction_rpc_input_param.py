# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .caip_2 import Caip2
from .tron_send_transaction_rpc_input_params_param import TronSendTransactionRpcInputParamsParam

__all__ = ["TronSendTransactionRpcInputParam"]


class TronSendTransactionRpcInputParam(TypedDict, total=False):
    """
    Executes the Tron `tron_sendTransaction` RPC to sign and broadcast a transaction.
    """

    method: Required[Literal["tron_sendTransaction"]]

    params: Required[TronSendTransactionRpcInputParamsParam]
    """Parameters for the Tron `tron_sendTransaction` RPC."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """
