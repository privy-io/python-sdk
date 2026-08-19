# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .wallet_entity import WalletEntity

__all__ = ["WalletEntityAssignmentResponse"]


class WalletEntityAssignmentResponse(BaseModel):
    """The entity assignment for a wallet."""

    id: str
    """Unique wallet entity assignment identifier."""

    created_at: float
    """Unix timestamp when the assignment was created."""

    entity: WalletEntity
    """The entity a wallet is attributed to."""

    updated_at: float
    """Unix timestamp when the assignment was last updated."""

    wallet_id: str
    """ID of the assigned wallet."""
