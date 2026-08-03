# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .ethereum_secp_256k_1_sign_rpc_input_params_param import EthereumSecp256k1SignRpcInputParamsParam

__all__ = ["EthereumSecp256k1SignRpcInputParam"]


class EthereumSecp256k1SignRpcInputParam(TypedDict, total=False):
    """Signs a raw hash on the secp256k1 curve."""

    method: Required[Literal["secp256k1_sign"]]

    params: Required[EthereumSecp256k1SignRpcInputParamsParam]
    """Parameters for the EVM `secp256k1_sign` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    wallet_id: str
