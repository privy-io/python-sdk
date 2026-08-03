# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountLineInputParam"]


class LinkedAccountLineInputParam(TypedDict, total=False):
    """The payload for importing a LINE account."""

    subject: Required[str]

    type: Required[Literal["line_oauth"]]

    email: str

    name: str

    profile_picture_url: str
