# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .caip_2 import Caip2
from .signature_options_param import SignatureOptionsParam
from .ethereum_sign_typed_data_rpc_input_params_param import EthereumSignTypedDataRpcInputParamsParam

__all__ = ["EthereumSignTypedDataRpcInputParam"]


class EthereumSignTypedDataRpcInputParam(TypedDict, total=False):
    """
    Executes the EVM `eth_signTypedData_v4` RPC (EIP-712) to sign a typed data object.
    """

    method: Required[Literal["eth_signTypedData_v4"]]

    params: Required[EthereumSignTypedDataRpcInputParamsParam]
    """Parameters for the EVM `eth_signTypedData_v4` RPC."""

    address: str

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    chain_type: Literal["ethereum"]

    signature_options: SignatureOptionsParam
    """
    Options controlling signature production for personal_sign and
    eth_signTypedData_v4.
    """

    wallet_id: str
