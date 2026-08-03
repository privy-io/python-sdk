# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhoneInviteInputParam"]


class PhoneInviteInputParam(TypedDict, total=False):
    """Allowlist invite input for a phone number."""

    type: Required[Literal["phone"]]

    value: Required[str]
