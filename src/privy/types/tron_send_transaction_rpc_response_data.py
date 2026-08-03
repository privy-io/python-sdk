# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .caip_2 import Caip2
from .._models import BaseModel

__all__ = ["TronSendTransactionRpcResponseData"]


class TronSendTransactionRpcResponseData(BaseModel):
    """Data returned by the Tron `tron_sendTransaction` RPC."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    hash: str

    transaction_id: str

    reference_id: Optional[str] = None
