# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..environment import Environment
from ..payout_source import PayoutSource
from .failure_reason import FailureReason
from .wallet_action_step import WalletActionStep
from ..payout_destination import PayoutDestination
from .wallet_action_status import WalletActionStatus
from ..orchestration_provider import OrchestrationProvider

__all__ = ["PayoutResponse"]


class PayoutResponse(BaseModel):
    """A payout wallet action.

    Crypto is sent on-chain to a liquidation address that offramps to the destination bank account.
    """

    id: str
    """The ID of the wallet action."""

    created_at: datetime
    """ISO 8601 timestamp of when the wallet action was created."""

    destination: PayoutDestination
    """The destination bank account for a payout."""

    environment: Environment
    """The Privy API environment."""

    provider: OrchestrationProvider
    """Supported fiat orchestration providers."""

    source: PayoutSource
    """The source crypto asset, chain, and amount for a payout."""

    status: WalletActionStatus
    """Status of a wallet action."""

    type: Literal["payout"]

    wallet_id: str
    """The ID of the wallet involved in the action."""

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    steps: Optional[List[WalletActionStep]] = None
    """The steps of the wallet action. Only returned if `?include=steps` is provided."""
