# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_secp_256k_1_sign_rpc_input_params import EthereumSecp256k1SignRpcInputParams

__all__ = ["EthereumSecp256k1SignRpcInput"]


class EthereumSecp256k1SignRpcInput(BaseModel):
    """Signs a raw hash on the secp256k1 curve."""

    method: Literal["secp256k1_sign"]

    params: EthereumSecp256k1SignRpcInputParams
    """Parameters for the EVM `secp256k1_sign` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["ethereum"]] = None

    wallet_id: Optional[str] = None
