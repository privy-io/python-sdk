# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .fiat_deposit_account import FiatDepositAccount

__all__ = ["FiatDepositAccountResponse"]


class FiatDepositAccountResponse(BaseModel):
    """Response containing a single fiat deposit account."""

    fiat_deposit_account: FiatDepositAccount
    """A Bridge fiat deposit account linked to a wallet."""
