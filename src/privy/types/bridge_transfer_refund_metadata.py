# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeTransferRefundMetadata"]


class BridgeTransferRefundMetadata(BaseModel):
    """Bridge metadata for a transfer refund."""

    method: Literal["transfer"]

    transfer_id: str

    type: Literal["refund"]

    original_transaction_hash: Optional[str] = None
    """The original transfer transaction hash (if available)."""
