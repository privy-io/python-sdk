# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tmmf_chain import TmmfChain
from .tmmf_provider import TmmfProvider
from .tmmf_provider_wallet_status import TmmfProviderWalletStatus

__all__ = ["TmmfWalletResponse"]


class TmmfWalletResponse(BaseModel):
    """A Privy wallet registered for a user with one tMMF provider on one chain."""

    address: str
    """Blockchain address of the registered wallet."""

    chain: TmmfChain
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    created_at: int
    """Unix timestamp in milliseconds when the wallet registration was created."""

    provider: TmmfProvider
    """The fund provider."""

    status: Optional[TmmfProviderWalletStatus] = None
    """
    A registered wallet's status with its tMMF provider, read live from the
    provider.
    """

    updated_at: int
    """Unix timestamp in milliseconds when the wallet registration was last updated."""

    user_id: str
    """ID of the Privy user the wallet is registered for."""

    wallet_id: str
    """ID of the Privy wallet registered to trade and hold fund shares."""
