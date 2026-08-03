# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .token_output import TokenOutput

__all__ = ["OutputWithPreviousTransactionData"]


class OutputWithPreviousTransactionData(BaseModel):
    """A Spark token output with its previous transaction data."""

    previous_transaction_hash: str

    previous_transaction_vout: float

    output: Optional[TokenOutput] = None
    """A Spark token output."""
