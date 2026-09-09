# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .earn_position_apy_type import EarnPositionApyType

__all__ = ["EarnPositionApyAllocation"]


class EarnPositionApyAllocation(BaseModel):
    """An APY allocation within a vault position."""

    apy_bps: int
    """Net APY in basis points, rounded to the nearest integer."""

    assets_in_vault: str
    """Allocated assets in the smallest unit of the underlying asset."""

    type: EarnPositionApyType
    """Whether an APY allocation earns the base or boosted rate."""
