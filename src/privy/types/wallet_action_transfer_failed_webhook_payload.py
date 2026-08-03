# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.failure_reason import FailureReason
from .wallets.wallet_action_step import WalletActionStep
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionTransferFailedWebhookPayload"]


class WalletActionTransferFailedWebhookPayload(BaseModel):
    """Payload for the wallet_action.transfer.failed webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    destination_address: str
    """Recipient address."""

    failed_at: str
    """ISO 8601 timestamp of when the wallet action failed."""

    failure_reason: FailureReason
    """A description of why a wallet action (or a step within a wallet action) failed."""

    source_chain: str
    """Chain name (e.g. "tempo", "base")."""

    status: Literal["failed"]
    """The status of the wallet action."""

    steps: List[WalletActionStep]
    """The steps of the wallet action.

    Completed steps will have transaction hashes; the failing step will have a
    failure_reason.
    """

    type: Literal["wallet_action.transfer.failed"]
    """The type of webhook event."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    source_amount: Optional[str] = None
    """Decimal amount sent on the source chain (e.g.

    "1.5"). Omitted for exact_output cross-chain transfers until the source amount
    is determined.
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
    were resolved onchain.
    """
