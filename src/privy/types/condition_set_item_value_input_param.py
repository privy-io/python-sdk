# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConditionSetItemValueInputParam"]


class ConditionSetItemValueInputParam(TypedDict, total=False):
    """A value to add to a condition set, with an optional name."""

    value: Required[str]

    name: str
    """Optional label for the item, unique within the condition set ignoring case."""
