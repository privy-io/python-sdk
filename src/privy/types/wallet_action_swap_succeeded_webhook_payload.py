# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.wallet_action_step import WalletActionStep
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionSwapSucceededWebhookPayload"]


class WalletActionSwapSucceededWebhookPayload(BaseModel):
    """Payload for the wallet_action.swap.succeeded webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    caip2: str
    """Chain identifier."""

    completed_at: str
    """ISO 8601 timestamp of when the wallet action completed successfully."""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    input_amount: Optional[str] = None
    """Amount of input token in base units. Populated after onchain confirmation."""

    input_token: str
    """Token address being sold."""

    output_amount: Optional[str] = None
    """Amount of output token received, in base units.

    Populated after onchain confirmation.
    """

    output_token: str
    """Token address being bought."""

    status: Literal["succeeded"]
    """The status of the wallet action."""

    steps: List[WalletActionStep]
    """The steps of the wallet action, including transaction hashes."""

    type: Literal["wallet_action.swap.succeeded"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""
