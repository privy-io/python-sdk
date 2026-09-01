# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fiat_deposit_currency import FiatDepositCurrency

__all__ = ["DepositStartedSource"]


class DepositStartedSource(BaseModel):
    """The fiat deposit that was received, including amount, currency, and originator."""

    amount: str
    """The fiat amount deposited."""

    currency: FiatDepositCurrency
    """Fiat currencies a deposit account can receive deposits in."""

    payment_rail: Optional[str] = None
    """The payment rail the deposit arrived on.

    Known values include "sepa", "ach_push", "wire", "fednow", "faster_payments",
    "pix", "spei", but the provider may return others.
    """

    sender_name: Optional[str] = None
