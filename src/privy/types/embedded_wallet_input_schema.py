# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_owned_recovery_option import UserOwnedRecoveryOption
from .embedded_wallet_chain_config import EmbeddedWalletChainConfig
from .embedded_wallet_create_on_login import EmbeddedWalletCreateOnLogin

__all__ = ["EmbeddedWalletInputSchema"]


class EmbeddedWalletInputSchema(BaseModel):
    """Input configuration for embedded wallets."""

    create_on_login: EmbeddedWalletCreateOnLogin
    """Whether to create embedded wallets on login."""

    ethereum: EmbeddedWalletChainConfig
    """Chain-specific configuration for embedded wallets."""

    solana: EmbeddedWalletChainConfig
    """Chain-specific configuration for embedded wallets."""

    user_owned_recovery_options: List[UserOwnedRecoveryOption]

    require_user_owned_recovery_on_create: Optional[bool] = None

    require_user_password_on_create: Optional[bool] = None
