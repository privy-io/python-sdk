# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .usage_source_type import UsageSourceType

__all__ = ["UsageAtaDepositRecordedWebhookPayload"]


class UsageAtaDepositRecordedWebhookPayload(BaseModel):
    """
    Payload for the usage.ata_deposit.recorded webhook event (sponsored Solana associated token account creation rent).
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

    type: Literal["usage.ata_deposit.recorded"]
    """The type of webhook event."""
