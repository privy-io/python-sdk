# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["YieldWithdrawConfirmedWebhookPayload"]


class YieldWithdrawConfirmedWebhookPayload(BaseModel):
    """Payload for the yield.withdraw.confirmed webhook event."""

    assets: str

    caip2: str

    owner: str

    receiver: str

    sender: str

    shares: str

    type: Literal["yield.withdraw.confirmed"]
    """The type of webhook event."""

    vault_address: str
