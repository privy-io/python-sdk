# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .svm_wallet_action_step_status import SvmWalletActionStepStatus

__all__ = ["SvmTransactionWalletActionStep"]


class SvmTransactionWalletActionStep(BaseModel):
    """A wallet action step consisting of an SVM (Solana) transaction."""

    caip2: str
    """CAIP-2 chain identifier for the Solana network."""

    status: SvmWalletActionStepStatus
    """Status of an SVM step in a wallet action."""

    transaction_signature: Optional[str] = None
    """The Solana transaction signature (base58-encoded). Null until broadcast."""

    type: Literal["svm_transaction"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    finalized: Optional[bool] = None
    """Whether this step has reached on-chain finality.

    Absent until finality is confirmed.
    """

    gas_credits_charged_usd: Optional[str] = None
    """Amount charged in USD for gas sponsorship on this step."""
