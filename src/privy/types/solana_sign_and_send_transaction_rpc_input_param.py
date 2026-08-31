# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .caip_2 import Caip2
from .rpc_sponsor_options_param import RpcSponsorOptionsParam
from .solana_sign_and_send_transaction_rpc_input_params_param import SolanaSignAndSendTransactionRpcInputParamsParam

__all__ = ["SolanaSignAndSendTransactionRpcInputParam"]


class SolanaSignAndSendTransactionRpcInputParam(TypedDict, total=False):
    """
    Executes the SVM `signAndSendTransaction` RPC to sign and broadcast a transaction.
    """

    caip2: Required[Caip2]
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Required[Literal["signAndSendTransaction"]]

    params: Required[SolanaSignAndSendTransactionRpcInputParamsParam]
    """Parameters for the SVM `signAndSendTransaction` RPC."""

    address: str

    chain_type: Literal["solana"]

    optimistic_broadcast: bool

    reference_id: str
    """Developer-provided identifier for this request. Must be unique per app."""

    sponsor: bool

    sponsor_options: RpcSponsorOptionsParam
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    wallet_id: str
