# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .usage_source_type import UsageSourceType

__all__ = ["UsageGasSponsorshipRecordedWebhookPayload"]


class UsageGasSponsorshipRecordedWebhookPayload(BaseModel):
    """
    Payload for the usage.gas_sponsorship.recorded webhook event (sponsored network gas).
    """

    amount_usd: str

    event_id: str
    """An opaque, stable identifier for this charge.

    Use it to deduplicate webhook deliveries.
    """

    recorded_at: int

    source_id: str

    source_type: UsageSourceType
    """The type of operation that incurred a usage charge."""

    type: Literal["usage.gas_sponsorship.recorded"]
    """The type of webhook event."""
