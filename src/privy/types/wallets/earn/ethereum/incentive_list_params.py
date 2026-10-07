# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IncentiveListParams"]


class IncentiveListParams(TypedDict, total=False):
    chain: Required[str]
    """Chain name to fetch rewards for (e.g. "tempo", "base")."""
