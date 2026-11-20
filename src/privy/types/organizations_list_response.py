# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .organization import Organization

__all__ = ["OrganizationsListResponse"]


class OrganizationsListResponse(BaseModel):
    """Response returned when listing organizations for an app."""

    data: List[Organization]
    """Items in this page."""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null when there are no further pages."""
