# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .payout_payment_rail import PayoutPaymentRail

__all__ = ["PayoutDestination"]


class PayoutDestination(BaseModel):
    """The destination bank account for a payout."""

    fiat_account_id: str
    """The ID of a previously registered external fiat account to pay out to."""

    payment_rail: Optional[PayoutPaymentRail] = None
    """A fiat payment rail a payout can settle over.

    `ach` is a standard ACH credit to the destination account.
    """
