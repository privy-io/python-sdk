# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .external_transaction_wallet_action_step_status import ExternalTransactionWalletActionStepStatus

__all__ = ["ExternalTransactionWalletActionStep"]


class ExternalTransactionWalletActionStep(BaseModel):
    """
    A wallet action step representing a cross-chain/cross-asset fill by an external provider.
    """

    status: ExternalTransactionWalletActionStepStatus
    """Status of an external transaction step in a wallet action."""

    type: Literal["external_transaction"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""
