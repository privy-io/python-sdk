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

    transaction_hash: Optional[str] = None
    """
    Identifier of the transaction the custodian last reported on the destination
    chain. Set on a settled transfer, and also on a failed one when the custodian
    had already broadcast a payout that was later returned. Null until the custodian
    reports one.
    """

    type: Literal["custodian_transaction"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""
