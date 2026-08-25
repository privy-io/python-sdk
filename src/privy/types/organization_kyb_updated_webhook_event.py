# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel
from .kyx_provider import KyxProvider
from .kyx_environment import KyxEnvironment
from .organization_kyb_updated_data import OrganizationKYBUpdatedData

__all__ = ["OrganizationKYBUpdatedWebhookEvent"]


class OrganizationKYBUpdatedWebhookEvent(BaseModel):
    changes: Dict[str, List[object]]

    data: OrganizationKYBUpdatedData
    """Full KYB state snapshot in a KYB update event."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""

    organization_id: str

    provider: KyxProvider
    """KYC/KYB provider identifier."""

    type: Literal["organization.kyb.updated"]
    """The type of webhook event."""
