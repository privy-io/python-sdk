# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .yield_claim_reward import YieldClaimReward

__all__ = ["YieldClaimConfirmedWebhookPayload"]


class YieldClaimConfirmedWebhookPayload(BaseModel):
    """Payload for the yield.claim.confirmed webhook event."""

    caip2: str

    rewards: List[YieldClaimReward]

    transaction_id: str

    type: Literal["yield.claim.confirmed"]
    """The type of webhook event."""

    wallet_id: str
