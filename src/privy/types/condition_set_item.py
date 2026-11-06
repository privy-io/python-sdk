# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConditionSetItem"]


class ConditionSetItem(BaseModel):
    """A single item in a condition set."""

    id: str
    """Unique ID of the created condition set item."""

    condition_set_id: str
    """Unique ID of the condition set this item belongs to."""

    created_at: float
    """Unix timestamp of when the condition set item was created in milliseconds."""

    value: str
    """The value stored in this condition set item."""

    name: Optional[str] = None
    """Label for the item, or null if it has none."""
