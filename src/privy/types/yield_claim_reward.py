# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["YieldClaimReward"]


class YieldClaimReward(BaseModel):
    """A single reward token claimed from a yield vault."""

    amount: str

    token_address: str

    token_symbol: str
