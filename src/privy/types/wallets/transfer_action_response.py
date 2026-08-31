# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..gas import Gas
from ..._models import BaseModel
from ..amount_type import AmountType
from ..fee_line_item import FeeLineItem
from .failure_reason import FailureReason
from .wallet_action_step import WalletActionStep
from .wallet_action_status import WalletActionStatus

__all__ = ["TransferActionResponse"]


class TransferActionResponse(BaseModel):
    """Response for a transfer action."""

    id: str
    """The ID of the wallet action."""

    created_at: datetime
    """ISO 8601 timestamp of when the wallet action was created."""

    destination_address: str
    """Recipient address."""

    destination_amount: Optional[str] = None
    """Amount received on the destination chain.

    For exact_output cross-chain transfers, set at creation (the guaranteed exact
    amount). For exact_input cross-chain transfers, null until fill confirmation.
    """

    source_chain: str
    """Chain name (e.g. "tempo", "base")."""

    status: WalletActionStatus
    """Status of a wallet action."""

    type: Literal["transfer"]

    wallet_id: str
    """The ID of the wallet involved in the action."""

    amount_type: Optional[AmountType] = None
    """Whether the amount refers to the input token or output token."""

    destination_asset: Optional[str] = None
    """Destination asset for cross-asset transfers. Omitted for same-asset transfers."""

    destination_chain: Optional[str] = None
    """Destination chain for cross-chain transfers. Omitted for same-chain transfers."""

    estimated_fees: Optional[List[FeeLineItem]] = None
    """Estimated fee breakdown from the provider quote.

    Only present for cross-chain or cross-asset transfers. Populated after on-chain
    confirmation.
    """

    estimated_gas: Optional[Gas] = None
    """Gas cost for a blockchain action.

    Includes both raw base-unit amount and a human-readable decimal string, plus the
    gas token symbol.
    """

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    fees: Optional[List[FeeLineItem]] = None
    """Actual fees paid for the transfer.

    Populated after on-chain confirmation. Only present for cross-chain transfers.
    """

    gas: Optional[Gas] = None
    """Gas cost for a blockchain action.

    Includes both raw base-unit amount and a human-readable decimal string, plus the
    gas token symbol.
    """

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    source_amount: Optional[str] = None
    """Decimal amount sent on the source chain (e.g.

    "1.5"). For exact_output cross-chain transfers, null until fill confirmation.
    """

    source_asset: Optional[str] = None
    """Asset identifier (e.g.

    "usdc", "eth"). Present when the transfer was initiated with a named asset;
    omitted for custom-token transfers.
    """

    source_asset_address: Optional[str] = None
    """Token contract address (EVM) or mint address (Solana).

    Present when the transfer was initiated with `asset_address`.
    """

    source_asset_decimals: Optional[int] = None
    """Number of decimals for the transferred token.

    Present when the transfer was initiated with `asset_address` and the decimals
    were resolved on-chain.
    """

    steps: Optional[List[WalletActionStep]] = None
    """The steps of the wallet action. Only returned if `?include=steps` is provided."""
