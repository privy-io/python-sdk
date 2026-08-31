# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .aptos_sign_transaction_rpc_input_params import AptosSignTransactionRpcInputParams

__all__ = ["AptosSignTransactionRpcInput"]


class AptosSignTransactionRpcInput(BaseModel):
    """
    Executes the Aptos `aptos_signTransaction` RPC to sign a legacy single-signer Ed25519 RawTransaction. The caller is responsible for broadcasting.
    """

    method: Literal["aptos_signTransaction"]

    params: AptosSignTransactionRpcInputParams
    """Parameters for the Aptos `aptos_signTransaction` RPC."""
