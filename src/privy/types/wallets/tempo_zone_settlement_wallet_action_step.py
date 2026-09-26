# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..hex import Hex
from ..._models import BaseModel
from .failure_reason import FailureReason
from .external_transaction_wallet_action_step_status import ExternalTransactionWalletActionStepStatus

__all__ = ["TempoZoneSettlementWalletActionStep"]


class TempoZoneSettlementWalletActionStep(BaseModel):
    """A wallet action step representing a Tempo Zone settlement on its parent chain."""

    caip2: Optional[str] = None
    """CAIP-2 identifier of the Tempo parent chain, or null when unavailable."""

    status: ExternalTransactionWalletActionStepStatus
    """Status of an external transaction step in a wallet action."""

    transaction_hash: Optional[Hex] = None
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    type: Literal["tempo_zone_settlement"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""
