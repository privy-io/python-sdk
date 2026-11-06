# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tmmf_chain import TmmfChain
from .tmmf_provider import TmmfProvider
from .tmmf_provider_wallet_status import TmmfProviderWalletStatus

__all__ = ["TmmfUserWalletResponse"]


class TmmfUserWalletResponse(BaseModel):
    """A wallet registered for a user with a provider on one chain."""

    address: str
    """Blockchain address of the registered wallet."""

    chain: TmmfChain
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    provider: TmmfProvider
    """The fund provider."""

    status: Optional[TmmfProviderWalletStatus] = None
    """
    A registered wallet's status with its tMMF provider, read live from the
    provider.
    """

    wallet_id: str
    """ID of the registered Privy wallet."""
