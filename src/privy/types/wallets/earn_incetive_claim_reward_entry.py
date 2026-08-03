# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EarnIncetiveClaimRewardEntry"]


class EarnIncetiveClaimRewardEntry(BaseModel):
    """A specific reward token and amount associated with an earn incentive claim."""

    amount: str
    """Claimable amount in base units."""

    token_address: str
    """Address of the reward token."""

    token_symbol: str
    """Symbol of the reward token (e.g. "MORPHO")."""

    token_decimals: Optional[int] = None
    """Number of decimal places for the reward token."""
