# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .environment import Environment
from .deposit_failed_data import DepositFailedData
from .orchestration_provider import OrchestrationProvider

__all__ = ["WalletDepositAccountDepositFailedWebhookEvent"]


class WalletDepositAccountDepositFailedWebhookEvent(BaseModel):
    data: DepositFailedData
    """
    Details of a fiat deposit that failed to convert and was refunded to the sender.
    """

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

    type: Literal["wallet.deposit_account.deposit_failed"]
    """The type of webhook event."""

    wallet_id: str

    provider_deposit_id: Optional[str] = None
    """The deposit's ID in the provider's system (e.g.

    Bridge), when the provider assigned one.
    """
