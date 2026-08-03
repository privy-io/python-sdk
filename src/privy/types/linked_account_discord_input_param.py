# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountDiscordInputParam"]


class LinkedAccountDiscordInputParam(TypedDict, total=False):
    """The payload for importing a Discord account."""

    subject: Required[str]

    type: Required[Literal["discord_oauth"]]

    username: Required[str]

    email: str
