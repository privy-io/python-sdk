# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConditionSetItemValueInput"]


class ConditionSetItemValueInput(BaseModel):
    """A single value to add to a condition set."""

    value: str
