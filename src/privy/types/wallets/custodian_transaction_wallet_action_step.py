# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .custodian_transaction_wallet_action_step_status import CustodianTransactionWalletActionStepStatus

__all__ = ["CustodianTransactionWalletActionStep"]


class CustodianTransactionWalletActionStep(BaseModel):
    """A wallet action step representing a transaction executed by a custodian (e.g.

    Bridge).
    """

    custodian: str
    """Identifier of the custodian executing this transaction (e.g. "bridge")."""

    status: CustodianTransactionWalletActionStepStatus
    """Status of a custodian transaction step in a wallet action."""

    type: Literal["custodian_transaction"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""
