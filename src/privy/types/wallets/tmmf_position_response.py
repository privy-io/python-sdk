# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .tmmf_position import TmmfPosition

__all__ = ["TmmfPositionResponse"]


class TmmfPositionResponse(BaseModel):
    """
    A page of a wallet's tMMF positions for all providers: one per fund and chain the wallet is registered for.
    """

    next_cursor: Optional[str] = None
    """Cursor of the next page of positions, or null on the last page."""

    positions: List[TmmfPosition]
    """A page of the wallet's positions, one per registered fund and chain."""

    wallet_id: str
    """ID of the Privy wallet holding the positions."""
