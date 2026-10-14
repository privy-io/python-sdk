# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .denylist_entry import DenylistEntry

__all__ = ["DenylistListResponse"]


class DenylistListResponse(BaseModel):
    """A page of denylist entries for an app."""

    data: List[DenylistEntry]
    """Denylist entries in this page."""

    next_cursor: Optional[str] = None
    """
    Cursor for the next page, which is null only when this page is empty, so keep
    paging until `data` is empty.
    """
