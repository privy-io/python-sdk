# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserOperationCompletedWebhookPayload"]


class UserOperationCompletedWebhookPayload(BaseModel):
    """Payload for the user_operation.completed webhook event."""

    actual_gas_cost: str

    actual_gas_used: str

    block_number: float

    caip2: str

    log_index: float

    nonce: str

    paymaster: Optional[str] = None

    sender: str

    success: bool

    transaction_hash: str

    type: Literal["user_operation.completed"]
    """The type of webhook event."""

    user_op_hash: str
