# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .onramp_asset import OnrampAsset
from .onramp_chain import OnrampChain

__all__ = ["OfframpDepositInstructions"]


class OfframpDepositInstructions(BaseModel):
    """Deposit instructions for an offramp transfer."""

    amount: str

    chain: OnrampChain
    """Supported blockchain chains for onramp and offramp."""

    currency: OnrampAsset
    """Supported crypto assets for onramp and offramp."""

    from_address: str

    to_address: str
