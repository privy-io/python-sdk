# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["KeyQuorumCreateParams"]


class KeyQuorumCreateParams(TypedDict, total=False):
    public_keys: Required[List[str]]

    authorization_threshold: float

    display_name: str
