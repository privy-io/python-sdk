# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .alchemy_paymaster_context import AlchemyPaymasterContext

__all__ = ["SmartWalletNetworkConfiguration"]


class SmartWalletNetworkConfiguration(BaseModel):
    """Network configuration for a smart wallet."""

    bundler_url: str

    chain_id: str

    chain_name: Optional[str] = None

    paymaster_context: Optional[AlchemyPaymasterContext] = None
    """The Alchemy paymaster context for a smart wallet network configuration."""

    paymaster_url: Optional[str] = None

    rpc_url: Optional[str] = None
