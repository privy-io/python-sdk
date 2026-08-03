# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .wallet_batch_create_result import WalletBatchCreateResult

__all__ = ["WalletBatchCreateResponse"]


class WalletBatchCreateResponse(BaseModel):
    """Response for a batch wallet creation request."""

    results: List[WalletBatchCreateResult]
    """Array of results for each wallet creation request, in the same order as input."""
