# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .export_type import ExportType

__all__ = ["SeedPhraseExportWebhookPayload"]


class SeedPhraseExportWebhookPayload(BaseModel):
    """Payload for the wallet.seed_phrase_export webhook event."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    type: Literal["wallet.seed_phrase_export"]
    """The type of webhook event."""

    user_id: str
    """The ID of the user who exported the seed phrase."""

    wallet_address: str
    """The address of the wallet."""

    wallet_id: str
    """The ID of the wallet."""

    export_source: Optional[ExportType] = None
    """The export type.

    'display' is for showing the key to the user in the UI, 'client' is for
    exporting to the client application.
    """
