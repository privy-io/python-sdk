# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AppGetGasSpendParams"]


class AppGetGasSpendParams(TypedDict, total=False):
    end_timestamp: Required[float]
    """Unix timestamp in milliseconds, exclusive.

    Must be greater than or equal to `start_timestamp`, and the range from
    `start_timestamp` to `end_timestamp` must not exceed 30 days.
    """

    start_timestamp: Required[float]
    """Unix timestamp in milliseconds, inclusive.

    Must be less than or equal to `end_timestamp`, and the range from
    `start_timestamp` to `end_timestamp` must not exceed 30 days.
    """

    wallet_ids: Required[SequenceNotStr[str]]
    """List of wallet IDs to query gas spend for. Maximum 100."""
