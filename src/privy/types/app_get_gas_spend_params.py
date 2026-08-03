# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AppGetGasSpendParams"]


class AppGetGasSpendParams(TypedDict, total=False):
    end_timestamp: Required[float]

    start_timestamp: Required[float]

    wallet_ids: Required[SequenceNotStr[str]]
