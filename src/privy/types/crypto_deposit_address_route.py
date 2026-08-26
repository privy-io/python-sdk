# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .crypto_deposit_asset import CryptoDepositAsset
from .crypto_deposit_asset_filter import CryptoDepositAssetFilter

__all__ = ["CryptoDepositAddressRoute"]


class CryptoDepositAddressRoute(BaseModel):
    """One deposit address and the source/destination route it accepts."""

    deposit_address: str

    destination: CryptoDepositAsset
    """An asset on a chain.

    Uses a human-readable alias (usdc, base) when one is on file, otherwise the raw
    asset address and CAIP-2.
    """

    source: CryptoDepositAssetFilter
    """Which assets a deposit address accepts.

    Asset and chain use human-readable aliases when known.
    """

    wallet_id: str
