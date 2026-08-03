# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .solana_sign_message_rpc_input_params import SolanaSignMessageRpcInputParams

__all__ = ["SolanaSignMessageRpcInput"]


class SolanaSignMessageRpcInput(BaseModel):
    """Executes the SVM `signMessage` RPC to sign a message."""

    method: Literal["signMessage"]

    params: SolanaSignMessageRpcInputParams
    """Parameters for the SVM `signMessage` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["solana"]] = None

    wallet_id: Optional[str] = None
