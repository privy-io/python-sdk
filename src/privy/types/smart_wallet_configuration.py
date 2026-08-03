# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .smart_wallet_configuration_enabled import SmartWalletConfigurationEnabled
from .smart_wallet_configuration_disabled import SmartWalletConfigurationDisabled

__all__ = ["SmartWalletConfiguration"]

SmartWalletConfiguration: TypeAlias = Union[SmartWalletConfigurationDisabled, SmartWalletConfigurationEnabled]
