# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OfframpCreateResponse", "DepositInstructions"]


class DepositInstructions(BaseModel):
    amount: str

    chain: Literal["ethereum", "base", "arbitrum", "polygon", "optimism"]

    currency: Literal["usdc"]

    from_address: str

    to_address: str


class OfframpCreateResponse(BaseModel):
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
