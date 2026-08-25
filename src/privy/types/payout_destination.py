# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PayoutDestination"]


class PayoutDestination(BaseModel):
    """The destination bank account for a payout."""

    fiat_account_id: str
    """The ID of a previously registered external fiat account to pay out to."""
