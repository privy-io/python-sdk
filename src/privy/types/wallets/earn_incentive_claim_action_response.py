# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .wallet_action_step import WalletActionStep
from .wallet_action_status import WalletActionStatus
from .earn_incetive_claim_reward_entry import EarnIncetiveClaimRewardEntry

__all__ = ["EarnIncentiveClaimActionResponse"]


class EarnIncentiveClaimActionResponse(BaseModel):
    """Response for an earn incentive claim action."""

    id: str
    """The ID of the wallet action."""

    chain: str
    """EVM chain name (e.g. "tempo", "base")."""

    created_at: datetime
    """ISO 8601 timestamp of when the wallet action was created."""

    rewards: Optional[List[EarnIncetiveClaimRewardEntry]] = None
    """Claimed reward tokens. Populated after the preparation step fetches from Merkl."""

    status: WalletActionStatus
    """Status of a wallet action."""

    type: Literal["earn_incentive_claim"]

    wallet_id: str
    """The ID of the wallet involved in the action."""

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    steps: Optional[List[WalletActionStep]] = None
    """The steps of the wallet action. Only returned if `?include=steps` is provided."""
