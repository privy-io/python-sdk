# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .kyx_verification_status import KyxVerificationStatus

__all__ = ["OrganizationKYBUpdatedKYBData"]


class OrganizationKYBUpdatedKYBData(BaseModel):
    """KYB verification status in a KYB update event."""

    status: KyxVerificationStatus
    """Status of KYC/KYB verification. Passthrough from the provider."""
