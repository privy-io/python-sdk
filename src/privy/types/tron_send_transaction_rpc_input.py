# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .caip_2 import Caip2
from .._models import BaseModel
from .tron_send_transaction_rpc_input_params import TronSendTransactionRpcInputParams

__all__ = ["TronSendTransactionRpcInput"]


class TronSendTransactionRpcInput(BaseModel):
    """
    Executes the Tron `tron_sendTransaction` RPC to sign and broadcast a transaction.
    """

    method: Literal["tron_sendTransaction"]

    params: TronSendTransactionRpcInputParams
    """Parameters for the Tron `tron_sendTransaction` RPC."""

    caip2: Optional[Caip2] = None
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """
