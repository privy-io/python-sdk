# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .environment import Environment
from .deposit_started_data import DepositStartedData
from .orchestration_provider import OrchestrationProvider

__all__ = ["WalletDepositAccountDepositStartedWebhookEvent"]


class WalletDepositAccountDepositStartedWebhookEvent(BaseModel):
    data: DepositStartedData
    """Details of a fiat deposit that has begun processing into a deposit account."""

    deposit_account_id: str

    deposit_type: Literal["fiat"]

    environment: Environment
    """The Privy API environment."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    provider: OrchestrationProvider
    """Supported fiat orchestration providers."""

    provider_deposit_id: str
    """The deposit's ID in the provider's system (e.g. Bridge), not a Privy ID."""

    type: Literal["wallet.deposit_account.deposit_started"]
    """The type of webhook event."""

    wallet_id: str
