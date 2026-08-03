# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .tron_contract import TronContract

__all__ = ["TronRawDataForSign"]


class TronRawDataForSign(BaseModel):
    """Tron raw_data for tron_signTransaction.

    Block reference fields are required; caller is responsible for fetching them.
    """

    contract: List[TronContract]

    expiration: int

    ref_block_bytes: str

    ref_block_hash: str

    data: Optional[str] = None

    fee_limit: Optional[int] = None

    timestamp: Optional[int] = None
