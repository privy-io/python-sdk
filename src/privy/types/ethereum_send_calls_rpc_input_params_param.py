# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .ethereum_send_calls_call_param import EthereumSendCallsCallParam

__all__ = ["EthereumSendCallsRpcInputParamsParam"]


class EthereumSendCallsRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the `wallet_sendCalls` RPC."""

    calls: Required[Iterable[EthereumSendCallsCallParam]]
