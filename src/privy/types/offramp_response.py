# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .onramp_transfer_status import OnrampTransferStatus
from .offramp_deposit_instructions import OfframpDepositInstructions

__all__ = ["OfframpResponse"]


class OfframpResponse(BaseModel):
    """Response for an offramp transfer initiation."""

    id: str

    deposit_instructions: OfframpDepositInstructions
    """Deposit instructions for an offramp transfer."""

    status: OnrampTransferStatus
    """Status of an onramp or offramp transfer."""
