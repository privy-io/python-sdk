# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionGetResponse"]


class TransactionGetResponse(BaseModel):
    id: str

    caip2: str

    created_at: float

    status: Literal["broadcasted", "confirmed", "execution_reverted", "failed"]

    transaction_hash: Optional[str] = None

    wallet_id: str
