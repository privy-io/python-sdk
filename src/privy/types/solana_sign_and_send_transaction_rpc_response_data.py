# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .caip_2 import Caip2
from .._models import BaseModel

__all__ = ["SolanaSignAndSendTransactionRpcResponseData"]


class SolanaSignAndSendTransactionRpcResponseData(BaseModel):
    """Data returned by the SVM `signAndSendTransaction` RPC."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    hash: str

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    signed_transaction: Optional[str] = None

    transaction_id: Optional[str] = None
