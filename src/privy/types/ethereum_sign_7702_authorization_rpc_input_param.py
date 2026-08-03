# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .ethereum_sign_7702_authorization_rpc_input_params_param import EthereumSign7702AuthorizationRpcInputParamsParam

__all__ = ["EthereumSign7702AuthorizationRpcInputParam"]


class EthereumSign7702AuthorizationRpcInputParam(TypedDict, total=False):
    """Signs an EIP-7702 authorization."""

    method: Required[Literal["eth_sign7702Authorization"]]

    params: Required[EthereumSign7702AuthorizationRpcInputParamsParam]
    """Parameters for the EVM `eth_sign7702Authorization` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    wallet_id: str
