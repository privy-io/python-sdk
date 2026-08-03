# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["YieldDepositConfirmedWebhookPayload"]


class YieldDepositConfirmedWebhookPayload(BaseModel):
    """Payload for the yield.deposit.confirmed webhook event."""

    assets: str

    caip2: str

    owner: str

    sender: str

    shares: str

    type: Literal["yield.deposit.confirmed"]
    """The type of webhook event."""

    vault_address: str
