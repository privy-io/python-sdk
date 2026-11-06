# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .tmmf_order_type import TmmfOrderType
from .wisdom_tree_settlement_received_amount import WisdomTreeSettlementReceivedAmount
from .wisdom_tree_settlement_requested_amount import WisdomTreeSettlementRequestedAmount
from .wisdom_tree_settlement_wallet_action_step_status import WisdomTreeSettlementWalletActionStepStatus

__all__ = ["WisdomTreeSettlementWalletActionStep"]


class WisdomTreeSettlementWalletActionStep(BaseModel):
    """
    A wallet action step representing the settlement of a tokenized money market fund (tMMF) order by WisdomTree.
    """

    caip2: Optional[str] = None
    """CAIP-2 identifier of the chain the order trades on."""

    order_type: Optional[TmmfOrderType] = None
    """
    How a tMMF order fills: `secondary` from the provider pool in minutes, or
    `primary` at the next NAV strike.
    """

    received: Optional[WisdomTreeSettlementReceivedAmount] = None
    """
    What a tMMF order receives: fund shares for a deposit, the withdraw asset for a
    withdrawal.
    """

    requested: Optional[WisdomTreeSettlementRequestedAmount] = None
    """
    What a tMMF order sends: the deposit asset for a deposit, fund shares for a
    withdrawal.
    """

    settlement_transaction_hash: Optional[str] = None
    """The transaction that delivered the received asset.

    Null until Privy verifies the settlement.
    """

    status: WisdomTreeSettlementWalletActionStepStatus
    """Status of a WisdomTree settlement step in a wallet action."""

    type: Literal["wisdomtree_settlement"]

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""
