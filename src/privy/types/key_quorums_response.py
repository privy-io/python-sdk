# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .key_quorum import KeyQuorum

__all__ = ["KeyQuorumsResponse"]


class KeyQuorumsResponse(BaseModel):
    """Paginated list of key quorums in an app."""

    data: List[KeyQuorum]
    """Key quorums in this page."""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null when there are no further pages."""
