# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ConditionSetItemsRequestBodyParam", "ConditionSetItemValueInputParam"]


class ConditionSetItemValueInputParam(TypedDict, total=False):
    """A single value to add to a condition set."""

    value: Required[str]


ConditionSetItemsRequestBodyParam: TypeAlias = List[ConditionSetItemValueInputParam]
