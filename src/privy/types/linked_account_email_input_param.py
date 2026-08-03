# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountEmailInputParam"]


class LinkedAccountEmailInputParam(TypedDict, total=False):
    """The payload for importing an email account."""

    address: Required[str]

    type: Required[Literal["email"]]
