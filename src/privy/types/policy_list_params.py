# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
    cursor: str
    """Cursor returned by the previous page."""

    limit: Optional[float]
