# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.wallet_action_step import WalletActionStep
from .wallets.wallet_action_type import WalletActionType
from .wallets.earn_incetive_claim_reward_entry import EarnIncetiveClaimRewardEntry

__all__ = ["WalletActionEarnIncentiveClaimSucceededWebhookPayload"]


class WalletActionEarnIncentiveClaimSucceededWebhookPayload(BaseModel):
    """Payload for the wallet_action.earn_incentive_claim.succeeded webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    chain: str
    """EVM chain name (e.g. "tempo", "base")."""

    completed_at: str
    """ISO 8601 timestamp of when the wallet action completed successfully."""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    rewards: Optional[List[EarnIncetiveClaimRewardEntry]] = None
    """Claimed reward tokens. Populated after the preparation step fetches from Merkl."""

    status: Literal["succeeded"]
    """The status of the wallet action."""

    steps: List[WalletActionStep]
    """The steps of the wallet action, including transaction hashes."""

    type: Literal["wallet_action.earn_incentive_claim.succeeded"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""
