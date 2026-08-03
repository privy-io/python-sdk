# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .linked_account_type_param import LinkedAccountTypeParam

__all__ = ["UserUnlinkLinkedAccountParams"]


class UserUnlinkLinkedAccountParams(TypedDict, total=False):
    handle: Required[str]

    type: Required[LinkedAccountTypeParam]
    """The possible types of linked accounts."""

    provider: str
