# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fiat_currency import FiatCurrency
from .fiat_payment_rail import FiatPaymentRail

__all__ = ["DepositStartedSource"]


class DepositStartedSource(BaseModel):
    """The fiat deposit that was received, including amount, currency, and originator."""

    amount: str
    """The fiat amount deposited."""

    currency: FiatCurrency
    """Supported fiat currencies."""

    payment_rail: Optional[FiatPaymentRail] = None
    """Supported fiat payment rails."""

    sender_name: Optional[str] = None
