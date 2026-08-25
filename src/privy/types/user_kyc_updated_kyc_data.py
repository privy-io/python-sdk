# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .kyx_verification_status import KyxVerificationStatus

__all__ = ["UserKYCUpdatedKYCData"]


class UserKYCUpdatedKYCData(BaseModel):
    """KYC verification status in a KYC update event."""

    status: KyxVerificationStatus
    """Status of KYC/KYB verification. Passthrough from the provider."""
