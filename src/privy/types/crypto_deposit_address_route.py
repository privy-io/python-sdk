# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .automation_asset_filter import AutomationAssetFilter
from .automation_destination_asset import AutomationDestinationAsset

__all__ = ["CryptoDepositAddressRoute"]


class CryptoDepositAddressRoute(BaseModel):
    """One deposit address and the source/destination route it accepts."""

    deposit_address: str

    destination: AutomationDestinationAsset
    """Destination asset identified by contract address on a specific chain (CAIP-2)."""

    source: AutomationAssetFilter
    """Which assets to include/exclude for an automation trigger."""

    wallet_id: str
