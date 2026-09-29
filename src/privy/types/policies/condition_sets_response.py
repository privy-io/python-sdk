# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..condition_set import ConditionSet

__all__ = ["ConditionSetsResponse"]


class ConditionSetsResponse(BaseModel):
    """Paginated list of condition sets in an app."""

    data: List[ConditionSet]
    """Condition sets in this page."""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null when there are no further pages."""
