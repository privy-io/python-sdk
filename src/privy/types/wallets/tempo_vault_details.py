# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .earn_asset import EarnAsset

__all__ = ["TempoVaultDetails"]


class TempoVaultDetails(BaseModel):
    """Vault details for a Tempo earn vault."""

    id: str
    """Vault identifier."""

    admin_wallet_address: str
    """EVM address of the vault admin wallet."""

    admin_wallet_id: Optional[str] = None
    """
    Privy wallet ID of the vault admin, or null when the Tempo vault admin is not
    Privy-managed.
    """

    app_apy: Optional[float] = None
    """
    Annual percentage yield earned by the app from fee wrapper fees, in basis
    points.
    """

    asset: EarnAsset
    """Asset metadata for an earn vault position."""

    available_liquidity_usd: Optional[float] = None
    """Available liquidity in USD."""

    caip2: str
    """CAIP-2 chain identifier (e.g. "eip155:4217" for Tempo, "eip155:8453" for Base)."""

    name: str
    """Human-readable vault name from the yield provider."""

    provider: Literal["tempo"]

    tvl_usd: Optional[float] = None
    """Total value locked in USD."""

    user_apy: Optional[float] = None
    """
    Annual percentage yield available to the user, after fees and excluding rewards,
    in basis points (e.g. 500 for 5%). 1 basis point = 0.01%.
    """

    vault_address: str
    """Onchain vault contract address."""
