# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountFarcasterInputParam"]


class LinkedAccountFarcasterInputParam(TypedDict, total=False):
    """The payload for importing a Farcaster account."""

    fid: Required[int]

    owner_address: Required[str]

    type: Required[Literal["farcaster"]]

    bio: str

    display_name: str

    homepage_url: str

    profile_picture_url: str

    username: str
