# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountPhoneInputParam"]


class LinkedAccountPhoneInputParam(TypedDict, total=False):
    """The payload for importing a phone account."""

    number: Required[str]

    type: Required[Literal["phone"]]
