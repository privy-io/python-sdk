# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .onramp_transfer_status import OnrampTransferStatus
from .onramp_deposit_instructions import OnrampDepositInstructions

__all__ = ["OnrampResponse"]


class OnrampResponse(BaseModel):
    """Response for an onramp transfer initiation."""

    id: str

    deposit_instructions: OnrampDepositInstructions
    """Bank deposit instructions for an onramp transfer."""

    status: OnrampTransferStatus
    """Status of an onramp or offramp transfer."""
