# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.wallet_action_step import WalletActionStep
from .wallets.wallet_action_type import WalletActionType

__all__ = ["WalletActionEarnWithdrawSucceededWebhookPayload"]


class WalletActionEarnWithdrawSucceededWebhookPayload(BaseModel):
    """Payload for the wallet_action.earn_withdraw.succeeded webhook event."""

    action_type: WalletActionType
    """Type of wallet action"""

    asset_address: str
    """Underlying asset token address."""

    caip2: str
    """CAIP-2 chain identifier."""

    completed_at: str
    """ISO 8601 timestamp of when the wallet action completed successfully."""

    created_at: str
    """ISO 8601 timestamp of when the wallet action was created."""

    raw_amount: str
    """Base-unit amount of asset withdrawn (e.g. "1500000")."""

    share_amount: str
    """Vault shares burned in base units."""

    status: Literal["succeeded"]
    """The status of the wallet action."""

    steps: List[WalletActionStep]
    """The steps of the wallet action, including transaction hashes."""

    type: Literal["wallet_action.earn_withdraw.succeeded"]
    """The type of webhook event."""

    vault_address: str
    """ERC-4626 vault contract address."""

    vault_id: str
    """The vault ID."""

    wallet_action_id: str
    """The ID of the wallet action."""

    wallet_id: str
    """The ID of the wallet involved in the action."""

    amount: Optional[str] = None
    """Human-readable decimal amount of asset withdrawn (e.g.

    "1.5"). Only present when the token is known in the asset registry.
    """

    asset: Optional[str] = None
    """Asset identifier (e.g.

    "usdc", "eth"). Only present when the token is known in the asset registry.
    """

    decimals: Optional[int] = None
    """Number of decimals for the underlying asset (e.g.

    6 for USDC, 18 for ETH). Only present when the token is known in the asset
    registry.
    """

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""
