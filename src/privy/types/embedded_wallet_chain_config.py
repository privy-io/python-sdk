# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .embedded_wallet_create_on_login import EmbeddedWalletCreateOnLogin

__all__ = ["EmbeddedWalletChainConfig"]


class EmbeddedWalletChainConfig(BaseModel):
    """Chain-specific configuration for embedded wallets."""

    create_on_login: EmbeddedWalletCreateOnLogin
    """Whether to create embedded wallets on login."""
