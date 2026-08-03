# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountCustomJwtInputParam"]


class LinkedAccountCustomJwtInputParam(TypedDict, total=False):
    """The payload for importing a Custom JWT account."""

    custom_user_id: Required[str]

    type: Required[Literal["custom_auth"]]
