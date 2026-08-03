# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tron_raw_data_for_send import TronRawDataForSend

__all__ = ["TronSendTransactionRpcInputParams"]


class TronSendTransactionRpcInputParams(BaseModel):
    """Parameters for the Tron `tron_sendTransaction` RPC."""

    raw_data: TronRawDataForSend
    """Tron raw_data for tron_sendTransaction.

    Block reference fields are optional; Privy fetches fresh values if omitted.
    """

    reference_id: Optional[str] = None
