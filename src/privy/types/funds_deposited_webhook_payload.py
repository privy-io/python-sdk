# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .block_info import BlockInfo
from .bridge_metadata import BridgeMetadata
from .wallet_funds_asset import WalletFundsAsset

__all__ = ["FundsDepositedWebhookPayload"]


class FundsDepositedWebhookPayload(BaseModel):
    """Payload for the wallet.funds_deposited webhook event."""

    amount: str
    """The amount transferred, as a stringified bigint."""

    asset: WalletFundsAsset
    """An asset involved in a wallet transfer."""

    block: BlockInfo
    """Block metadata for a wallet transfer event."""

    caip2: str
    """The CAIP-2 chain identifier."""

    idempotency_key: str
    """A unique key for this event."""

    recipient: str
    """The recipient address."""

    sender: str
    """The sender address."""

    transaction_hash: str
    """The blockchain transaction hash."""

    type: Literal["wallet.funds_deposited"]
    """The type of webhook event."""

    wallet_id: str
    """The ID of the wallet."""

    bridge_metadata: Optional[BridgeMetadata] = None
    """Metadata about a Bridge transaction associated with a wallet event."""

    transaction_fee: Optional[str] = None
    """The transaction fee paid, as a stringified bigint in the chain's native token."""
