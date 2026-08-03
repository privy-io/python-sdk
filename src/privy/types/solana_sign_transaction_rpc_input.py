# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .solana_sign_transaction_rpc_input_params import SolanaSignTransactionRpcInputParams

__all__ = ["SolanaSignTransactionRpcInput"]


class SolanaSignTransactionRpcInput(BaseModel):
    """Executes the SVM `signTransaction` RPC to sign a transaction."""

    method: Literal["signTransaction"]

    params: SolanaSignTransactionRpcInputParams
    """Parameters for the SVM `signTransaction` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["solana"]] = None

    wallet_id: Optional[str] = None
