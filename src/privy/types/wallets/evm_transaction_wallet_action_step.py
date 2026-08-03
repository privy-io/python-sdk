# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .evm_wallet_action_step_status import EvmWalletActionStepStatus

__all__ = ["EvmTransactionWalletActionStep"]


class EvmTransactionWalletActionStep(BaseModel):
    """A wallet action step consisting of an EVM transaction."""

    caip2: str
    """CAIP-2 chain identifier of the transaction, containing the chain ID."""

    status: EvmWalletActionStepStatus
    """Status of an EVM step in a wallet action."""

    transaction_hash: Optional[str] = None
    """The transaction hash for this step.

    May change while the step status is non-terminal.
    """

    type: Literal["evm_transaction"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    finalized: Optional[bool] = None
    """Whether this step has reached on-chain finality.

    Absent until finality is confirmed.
    """
