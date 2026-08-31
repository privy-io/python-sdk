# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..gas import Gas
from ..._models import BaseModel
from ..fee_line_item import FeeLineItem
from .failure_reason import FailureReason
from .wallet_action_step import WalletActionStep
from .wallet_action_status import WalletActionStatus

__all__ = ["SwapActionResponse"]


class SwapActionResponse(BaseModel):
    """Response for a swap action."""

    id: str
    """The ID of the wallet action."""

    caip2: str
    """CAIP-2 chain identifier for the swap."""

    created_at: datetime
    """ISO 8601 timestamp of when the wallet action was created."""

    input_amount: Optional[str] = None
    """Exact base-unit amount of input token. Populated after on-chain confirmation."""

    input_token: str
    """Token address or "native" for the token being sold."""

    output_amount: Optional[str] = None
    """Exact base-unit amount of output token. Populated after on-chain confirmation."""

    output_token: str
    """Token address or "native" for the token being bought."""

    status: WalletActionStatus
    """Status of a wallet action."""

    type: Literal["swap"]

    wallet_id: str
    """The ID of the wallet involved in the action."""

    destination_address: Optional[str] = None
    """Recipient address on the destination chain.

    Present for cross-chain swaps. May differ from the source wallet address when
    swapping between chain types (e.g. EVM to Solana).
    """

    destination_caip2: Optional[str] = None
    """Destination chain CAIP-2 identifier. Present for cross-chain swaps."""

    estimated_fees: Optional[List[FeeLineItem]] = None
    """Estimated fee breakdown from the provider quote.

    Only present for cross-chain swaps. Populated after on-chain confirmation.
    """

    estimated_gas: Optional[Gas] = None
    """Gas cost for a blockchain action.

    Includes both raw base-unit amount and a human-readable decimal string, plus the
    gas token symbol.
    """

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    fees: Optional[List[FeeLineItem]] = None
    """Actual fees paid for the swap.

    Populated after on-chain confirmation. Only present for cross-chain swaps.
    """

    gas: Optional[Gas] = None
    """Gas cost for a blockchain action.

    Includes both raw base-unit amount and a human-readable decimal string, plus the
    gas token symbol.
    """

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    steps: Optional[List[WalletActionStep]] = None
    """The steps of the wallet action. Only returned if `?include=steps` is provided."""
