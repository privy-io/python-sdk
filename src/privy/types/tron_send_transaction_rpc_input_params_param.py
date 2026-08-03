# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tron_raw_data_for_send_param import TronRawDataForSendParam

__all__ = ["TronSendTransactionRpcInputParamsParam"]


class TronSendTransactionRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Tron `tron_sendTransaction` RPC."""

    raw_data: Required[TronRawDataForSendParam]
    """Tron raw_data for tron_sendTransaction.

    Block reference fields are optional; Privy fetches fresh values if omitted.
    """

    reference_id: str
