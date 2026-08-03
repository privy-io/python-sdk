# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Gas"]


class Gas(BaseModel):
    """Gas cost for a blockchain action.

    Includes both raw base-unit amount and a human-readable decimal string, plus the gas token symbol.
    """

    amount: str
    """Gas cost in the gas token as a human-readable decimal string (e.g. "0.0001")."""

    base_amount: str
    """Gas cost in the gas token's base units (e.g. wei)."""

    gas_asset: str
    """Gas token symbol (e.g. "ETH", "USDC")."""
