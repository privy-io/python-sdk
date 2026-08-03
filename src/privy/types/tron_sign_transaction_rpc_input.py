# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tron_sign_transaction_rpc_input_params import TronSignTransactionRpcInputParams

__all__ = ["TronSignTransactionRpcInput"]


class TronSignTransactionRpcInput(BaseModel):
    """Executes the Tron `tron_signTransaction` RPC to sign a transaction.

    The caller is responsible for broadcasting.
    """

    method: Literal["tron_signTransaction"]

    params: TronSignTransactionRpcInputParams
    """Parameters for the Tron `tron_signTransaction` RPC."""
