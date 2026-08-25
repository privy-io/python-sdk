# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FiatDepositInstructions"]


class FiatDepositInstructions(BaseModel):
    """Bank or payment deposit instructions for a fiat deposit account.

    Shape varies by source currency.
    """

    account_holder_name: Optional[str] = None

    account_number: Optional[str] = None

    bank_account_number: Optional[str] = None

    bank_address: Optional[str] = None

    bank_beneficiary_address: Optional[str] = None

    bank_beneficiary_name: Optional[str] = None

    bank_name: Optional[str] = None

    bank_routing_number: Optional[str] = None

    bic: Optional[str] = None

    br_code: Optional[str] = None

    bre_b_key: Optional[str] = None

    clabe: Optional[str] = None

    deposit_message: Optional[str] = None

    iban: Optional[str] = None

    payment_rails: Optional[List[str]] = None

    sort_code: Optional[str] = None
