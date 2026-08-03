# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountTwitchInputParam"]


class LinkedAccountTwitchInputParam(TypedDict, total=False):
    """The payload for importing a Twitch account."""

    subject: Required[str]

    type: Required[Literal["twitch_oauth"]]

    username: str
