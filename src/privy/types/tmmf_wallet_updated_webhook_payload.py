# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallets.tmmf_chain import TmmfChain
from .wallets.tmmf_provider import TmmfProvider
from .wallets.tmmf_provider_wallet_status import TmmfProviderWalletStatus

__all__ = ["TmmfWalletUpdatedWebhookPayload"]


class TmmfWalletUpdatedWebhookPayload(BaseModel):
    """
    Payload for the tmmf.wallet.updated webhook event: the status of a tMMF wallet with the provider changed.
    """

    address: str
    """Blockchain address of the registered wallet."""

    chain: TmmfChain
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    created_at: int
    """Unix timestamp in milliseconds when the wallet registration was created."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    provider: TmmfProvider
    """The fund provider."""

    status: Optional[TmmfProviderWalletStatus] = None
    """
    A registered wallet's status with its tMMF provider, read live from the
    provider.
    """

    type: Literal["tmmf.wallet.updated"]
    """The type of webhook event."""

    updated_at: int
    """Unix timestamp in milliseconds when the wallet registration was last updated."""

    user_id: str
    """ID of the Privy user the wallet is registered for."""

    wallet_id: str
    """ID of the Privy wallet registered to trade and hold fund shares."""

    emitted_at: Optional[int] = None
    """
    Unix timestamp in milliseconds when the provider emitted the event of the
    change; absent when no provider event reported it.
    """

    sequence: Optional[int] = None
    """
    The provider's sequence number of the change, higher for later changes to the
    resource; absent when no provider event reported it.
    """
