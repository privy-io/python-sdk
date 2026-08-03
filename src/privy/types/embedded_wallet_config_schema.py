# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .embedded_wallet_mode import EmbeddedWalletMode
from .embedded_wallet_input_schema import EmbeddedWalletInputSchema

__all__ = ["EmbeddedWalletConfigSchema"]


class EmbeddedWalletConfigSchema(EmbeddedWalletInputSchema):
    """Configuration for embedded wallets including the mode."""

    mode: EmbeddedWalletMode
    """The mode for embedded wallets."""
