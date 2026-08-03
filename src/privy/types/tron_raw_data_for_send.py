# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .tron_contract import TronContract

__all__ = ["TronRawDataForSend"]


class TronRawDataForSend(BaseModel):
    """Tron raw_data for tron_sendTransaction.

    Block reference fields are optional; Privy fetches fresh values if omitted.
    """

    contract: List[TronContract]

    data: Optional[str] = None

    expiration: Optional[int] = None

    fee_limit: Optional[int] = None

    ref_block_bytes: Optional[str] = None

    ref_block_hash: Optional[str] = None

    timestamp: Optional[int] = None
