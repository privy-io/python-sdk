# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountTiktokInputParam"]


class LinkedAccountTiktokInputParam(TypedDict, total=False):
    """The payload for importing a Tiktok account."""

    name: Required[Optional[str]]

    subject: Required[str]

    type: Required[Literal["tiktok_oauth"]]

    username: Required[str]
