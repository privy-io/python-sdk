# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .caip_2 import Caip2
from .._models import BaseModel

__all__ = ["EthereumSendCallsRpcResponseData"]


class EthereumSendCallsRpcResponseData(BaseModel):
    """Data returned by the `wallet_sendCalls` RPC."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    transaction_id: str
