# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .smart_wallet_type import SmartWalletType
from .smart_wallet_network_configuration import SmartWalletNetworkConfiguration

__all__ = ["SmartWalletConfigurationEnabled"]


class SmartWalletConfigurationEnabled(BaseModel):
    """An enabled smart wallet configuration."""

    configured_networks: List[SmartWalletNetworkConfiguration]

    enabled: Literal[True]

    smart_wallet_type: SmartWalletType
    """The supported smart wallet providers."""

    smart_wallet_version: Optional[str] = None
