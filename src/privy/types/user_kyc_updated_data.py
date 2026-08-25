# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .kyx_endorsement import KyxEndorsement
from .kyx_capabilities import KyxCapabilities
from .kyx_provider_status import KyxProviderStatus
from .user_kyc_updated_kyc_data import UserKYCUpdatedKYCData
from .user_kyc_updated_tos_data import UserKYCUpdatedTosData

__all__ = ["UserKYCUpdatedData"]


class UserKYCUpdatedData(BaseModel):
    """Full KYC state snapshot in a KYC update event."""

    capabilities: KyxCapabilities
    """Capability statuses for the customer."""

    endorsements: List[KyxEndorsement]

    kyc: UserKYCUpdatedKYCData
    """KYC verification status in a KYC update event."""

    status: KyxProviderStatus
    """KYC/KYB status for the user."""

    tos: UserKYCUpdatedTosData
    """Terms of service status in a KYC update event."""
