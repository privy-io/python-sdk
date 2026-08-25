# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .kyx_endorsement import KyxEndorsement
from .kyx_capabilities import KyxCapabilities
from .kyx_provider_status import KyxProviderStatus
from .organization_kyb_updated_kyb_data import OrganizationKYBUpdatedKYBData
from .organization_kyb_updated_tos_data import OrganizationKYBUpdatedTosData

__all__ = ["OrganizationKYBUpdatedData"]


class OrganizationKYBUpdatedData(BaseModel):
    """Full KYB state snapshot in a KYB update event."""

    capabilities: KyxCapabilities
    """Capability statuses for the customer."""

    endorsements: List[KyxEndorsement]

    kyb: OrganizationKYBUpdatedKYBData
    """KYB verification status in a KYB update event."""

    status: KyxProviderStatus
    """KYC/KYB status for the user."""

    tos: OrganizationKYBUpdatedTosData
    """Terms of service status in a KYB update event."""
