# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountTwitterInputParam"]


class LinkedAccountTwitterInputParam(TypedDict, total=False):
    """The payload for importing a Twitter account."""

    name: Required[str]

    subject: Required[str]

    type: Required[Literal["twitter_oauth"]]

    username: Required[str]

    profile_picture_url: str
