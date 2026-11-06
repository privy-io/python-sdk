# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConditionSetItemValueInput"]


class ConditionSetItemValueInput(BaseModel):
    """A value to add to a condition set, with an optional name."""

    value: str

    name: Optional[str] = None
    """Optional label for the item, unique within the condition set ignoring case."""
