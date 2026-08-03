# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ethereum_send_calls_call import EthereumSendCallsCall

__all__ = ["EthereumSendCallsRpcInputParams"]


class EthereumSendCallsRpcInputParams(BaseModel):
    """Parameters for the `wallet_sendCalls` RPC."""

    calls: List[EthereumSendCallsCall]
