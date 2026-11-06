# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ConditionSetItemsRequestBodyParam", "ConditionSetItemValueInputParam"]


class ConditionSetItemValueInputParam(TypedDict, total=False):
    """A value to add to a condition set, with an optional name."""

    value: Required[str]

    name: str
    """Optional label for the item, unique within the condition set ignoring case."""


ConditionSetItemsRequestBodyParam: TypeAlias = List[ConditionSetItemValueInputParam]
