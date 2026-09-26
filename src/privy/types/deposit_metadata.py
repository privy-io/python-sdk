# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .refund_details import RefundDetails

__all__ = ["DepositMetadata"]


class DepositMetadata(BaseModel):
    """Metadata identifying a refunded wallet deposit."""

    details: RefundDetails
    """Relay details for a refunded wallet deposit."""

    type: Literal["refund"]
