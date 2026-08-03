# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionSwapCreatedWebhookPayload"]


class WalletActionSwapCreatedWebhookPayload(BaseModel):
    """Payload for the wallet_action.swap.created webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    caip2: str
    """Chain identifier."""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    input_amount: Optional[str] = None
    """Amount of input token in base units. Populated after onchain confirmation."""

    input_token: str
    """Token address being sold."""

    output_token: str
    """Token address being bought."""

    status: Literal["pending"]
    """The status of the wallet action."""

    type: Literal["wallet_action.swap.created"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""
