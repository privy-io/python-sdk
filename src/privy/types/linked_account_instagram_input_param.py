# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountInstagramInputParam"]


class LinkedAccountInstagramInputParam(TypedDict, total=False):
    """The payload for importing an Instagram account."""

    subject: Required[str]

    type: Required[Literal["instagram_oauth"]]

    username: Required[str]
