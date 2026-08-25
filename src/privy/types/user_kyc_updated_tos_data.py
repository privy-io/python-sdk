# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .kyx_tos_status import KyxTosStatus

__all__ = ["UserKYCUpdatedTosData"]


class UserKYCUpdatedTosData(BaseModel):
    """Terms of service status in a KYC update event."""

    status: KyxTosStatus
    """Status of Terms of Service acceptance. Passthrough from the provider."""
