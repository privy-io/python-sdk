# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EarnIncentiveRewardEntry"]


class EarnIncentiveRewardEntry(BaseModel):
    """A reward token with claimed and unclaimed amounts."""

    amount_claimed: str
    """Total amount already claimed, in smallest unit."""

    amount_unclaimed: str
    """Amount available to claim on-chain but not yet claimed, in smallest unit."""

    token_address: str
    """Address of the reward token."""

    token_symbol: str
    """Symbol of the reward token (e.g. "MORPHO")."""

    token_decimals: Optional[int] = None
    """Number of decimals for the reward token."""
