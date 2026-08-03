# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountAppleInputParam"]


class LinkedAccountAppleInputParam(TypedDict, total=False):
    """The payload for importing an Apple account."""

    subject: Required[str]

    type: Required[Literal["apple_oauth"]]

    email: str
