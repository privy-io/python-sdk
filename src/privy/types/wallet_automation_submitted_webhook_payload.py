# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletAutomationSubmittedWebhookPayload"]


class WalletAutomationSubmittedWebhookPayload(BaseModel):
    """Payload for the wallet_automation.submitted webhook event."""

    action_id: str
    """The ID of the wallet action created to fulfill the automation."""

    automation_id: str
    """The ID of the automation that fired."""

    created_at: str
    """ISO 8601 timestamp of when the automation was submitted."""

    trigger_asset_address: str
    """
    Contract address of the triggering deposit's asset, or 'native-token' for the
    native asset.
    """

    trigger_caip2: str
    """CAIP-2 chain identifier of the triggering deposit (e.g., 'eip155:8453')."""

    trigger_id: str
    """The ID of the automation execution that fired."""

    type: Literal["wallet_automation.submitted"]
    """The type of webhook event."""

    wallet_id: str
    """The ID of the wallet the automation fired for."""
