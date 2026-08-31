# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .environment import Environment
from .orchestration_provider import OrchestrationProvider
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionPayoutCreatedWebhookPayload"]


class WalletActionPayoutCreatedWebhookPayload(BaseModel):
    """Payload for the wallet_action.payout.created webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    destination_currency: str
    """The fiat currency the payout settles in (e.g. "usd")."""

    destination_fiat_account_id: str
    """The registered external fiat account the payout settles to."""

    destination_payment_rail: str
    """The fiat payment rail the payout settles over (e.g. "ach", "sepa", "wire")."""

    environment: Environment
    """The Privy API environment."""

    provider: OrchestrationProvider
    """Supported fiat orchestration providers."""

    source_amount: str
    """Decimal amount offramped, in the asset's standard units (e.g. "100.00")."""

    source_asset: str
    """Source crypto asset sent on-chain (e.g. "usdc")."""

    source_chain: str
    """Source chain the crypto was sent from (e.g. "base")."""

    status: Literal["pending"]
    """The status of the wallet action."""

    type: Literal["wallet_action.payout.created"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""
