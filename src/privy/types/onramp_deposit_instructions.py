# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fiat_currency import FiatCurrency
from .fiat_payment_rail import FiatPaymentRail

__all__ = ["OnrampDepositInstructions"]


class OnrampDepositInstructions(BaseModel):
    """Bank deposit instructions for an onramp transfer."""

    amount: str

    currency: FiatCurrency
    """Supported fiat currencies."""

    payment_rail: FiatPaymentRail
    """Supported fiat payment rails."""

    account_holder_name: Optional[str] = None

    bank_account_number: Optional[str] = None

    bank_address: Optional[str] = None

    bank_beneficiary_address: Optional[str] = None

    bank_beneficiary_name: Optional[str] = None

    bank_name: Optional[str] = None

    bank_routing_number: Optional[str] = None

    bic: Optional[str] = None

    deposit_message: Optional[str] = None

    iban: Optional[str] = None
