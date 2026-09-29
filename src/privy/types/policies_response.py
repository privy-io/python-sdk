# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .policy_list_item import PolicyListItem

__all__ = ["PoliciesResponse"]


class PoliciesResponse(BaseModel):
    """Paginated list of policies in an app."""

    data: List[PolicyListItem]
    """Policies in this page."""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null when there are no further pages."""
