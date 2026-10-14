# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DenylistEmailInputParam"]


class DenylistEmailInputParam(TypedDict, total=False):
    """
    Denylist input for an email address, which also blocks its `+` and `.` variants.
    """

    type: Required[Literal["email"]]

    value: Required[str]
