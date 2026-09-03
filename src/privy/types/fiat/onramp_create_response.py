# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnrampCreateResponse", "DepositInstructions"]


class DepositInstructions(BaseModel):
    amount: str

    currency: Literal["usd", "eur"]

    payment_rail: Literal["sepa", "ach_push", "wire"]

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


class OnrampCreateResponse(BaseModel):
    id: str

    deposit_instructions: DepositInstructions

    status: Literal[
        "awaiting_funds",
        "in_review",
        "funds_received",
        "payment_submitted",
        "payment_processed",
        "canceled",
        "error",
        "undeliverable",
        "returned",
        "refunded",
    ]
