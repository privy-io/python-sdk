# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .spark_transfer_leaf import SparkTransferLeaf

__all__ = ["SparkTransfer"]


class SparkTransfer(BaseModel):
    """A Spark transfer."""

    id: str

    leaves: List[SparkTransferLeaf]

    receiver_identity_public_key: str

    sender_identity_public_key: str

    status: str

    total_value: float

    transfer_direction: str

    type: str

    created_time: Optional[str] = None

    expiry_time: Optional[str] = None

    updated_time: Optional[str] = None
