# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .wallet_action_step import WalletActionStep
from .wallet_action_status import WalletActionStatus

__all__ = ["TmmfDepositActionResponse"]


class TmmfDepositActionResponse(BaseModel):
    """A tokenized money market fund (tMMF) deposit."""

    id: str
    """The ID of the wallet action."""

    created_at: datetime
    """ISO 8601 timestamp of when the wallet action was created."""

    status: WalletActionStatus
    """Status of a wallet action."""

    type: Literal["tmmf_deposit"]

    wallet_id: str
    """The ID of the wallet involved in the action."""

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    steps: Optional[List[WalletActionStep]] = None
    """The steps of the wallet action. Only returned if `?include=steps` is provided."""
