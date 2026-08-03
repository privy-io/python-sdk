# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .ethereum_sign_user_operation_rpc_input_params_param import EthereumSignUserOperationRpcInputParamsParam

__all__ = ["EthereumSignUserOperationRpcInputParam"]


class EthereumSignUserOperationRpcInputParam(TypedDict, total=False):
    """Executes an RPC method to hash and sign a UserOperation."""

    method: Required[Literal["eth_signUserOperation"]]

    params: Required[EthereumSignUserOperationRpcInputParamsParam]
    """Parameters for the EVM `eth_signUserOperation` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    wallet_id: str
