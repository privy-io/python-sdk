# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .wallet_recovery_setup_method import WalletRecoverySetupMethod

__all__ = ["WalletRecoverySetupWebhookPayload"]


class WalletRecoverySetupWebhookPayload(BaseModel):
    """Payload for the wallet.recovery_setup webhook event."""

    method: WalletRecoverySetupMethod
    """Recovery method types for embedded wallet recovery setup webhooks."""

    type: Literal["wallet.recovery_setup"]
    """The type of webhook event."""

    user_id: str
    """The ID of the user."""

    wallet_address: str
    """The address of the wallet."""

    wallet_id: str
    """The ID of the wallet."""
