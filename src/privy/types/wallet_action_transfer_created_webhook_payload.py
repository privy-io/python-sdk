# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionTransferCreatedWebhookPayload"]


class WalletActionTransferCreatedWebhookPayload(BaseModel):
    """Payload for the wallet_action.transfer.created webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    destination_address: str
    """Recipient address."""

    source_chain: str
    """Chain name (e.g. "tempo", "base")."""

    status: Literal["pending"]
    """The status of the wallet action."""

    type: Literal["wallet_action.transfer.created"]
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
