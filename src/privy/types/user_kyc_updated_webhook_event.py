# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel
from .kyx_provider import KyxProvider
from .kyx_environment import KyxEnvironment
from .user_kyc_updated_data import UserKYCUpdatedData

__all__ = ["UserKYCUpdatedWebhookEvent"]


class UserKYCUpdatedWebhookEvent(BaseModel):
    changes: Dict[str, List[object]]

    data: UserKYCUpdatedData
    """Full KYC state snapshot in a KYC update event."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    provider: KyxProvider
    """KYC/KYB provider identifier."""

    type: Literal["user.kyc.updated"]
    """The type of webhook event."""

    user_id: str
