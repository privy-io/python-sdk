# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.failure_reason import FailureReason
from .wallets.wallet_action_step import WalletActionStep
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionSwapFailedWebhookPayload"]


class WalletActionSwapFailedWebhookPayload(BaseModel):
    """Payload for the wallet_action.swap.failed webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    caip2: str
    """Chain identifier."""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    failed_at: str
    """ISO 8601 timestamp of when the wallet action failed."""

    failure_reason: FailureReason
    """A description of why a wallet action (or a step within a wallet action) failed."""

    input_amount: Optional[str] = None
    """Amount of input token in base units. Populated after onchain confirmation."""

    input_token: str
    """Token address being sold."""

    output_token: str
    """Token address being bought."""

    status: Literal["failed"]
    """The status of the wallet action."""

    steps: List[WalletActionStep]
    """The steps of the wallet action.

    Completed steps will have transaction hashes; the failing step will have a
    failure_reason.
    """

    type: Literal["wallet_action.swap.failed"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""
