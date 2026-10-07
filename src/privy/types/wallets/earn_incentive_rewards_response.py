# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .earn_incentive_reward_entry import EarnIncentiveRewardEntry

__all__ = ["EarnIncentiveRewardsResponse"]


class EarnIncentiveRewardsResponse(BaseModel):
    """
    All incentive rewards for a wallet, with claimed and unclaimed amounts per token.
    """

    rewards: List[EarnIncentiveRewardEntry]
    """Reward tokens with their claimed and unclaimed amounts."""
