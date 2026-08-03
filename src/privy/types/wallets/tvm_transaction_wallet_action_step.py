# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .tvm_wallet_action_step_status import TvmWalletActionStepStatus

__all__ = ["TvmTransactionWalletActionStep"]


class TvmTransactionWalletActionStep(BaseModel):
    """A wallet action step consisting of a TVM (Tron) transaction."""

    caip2: str
    """CAIP-2 chain identifier for the Tron network."""

    status: TvmWalletActionStepStatus
    """Status of a TVM (Tron) step in a wallet action."""

    transaction_id: Optional[str] = None
    """The Tron transaction ID. Null until broadcast."""

    type: Literal["tvm_transaction"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""
