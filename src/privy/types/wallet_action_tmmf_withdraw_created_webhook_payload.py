# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionTmmfWithdrawCreatedWebhookPayload"]


class WalletActionTmmfWithdrawCreatedWebhookPayload(BaseModel):
    """Payload for the wallet_action.tmmf_withdraw.created webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    status: Literal["pending"]
    """The status of the wallet action."""

    type: Literal["wallet_action.tmmf_withdraw.created"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""
