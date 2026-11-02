# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["VerificationInitParams"]


class VerificationInitParams(TypedDict, total=False):
    relying_party: Required[str]
    """Origin where the authenticator runs, such as https://app.example.com."""

    user_jwt: Required[Annotated[str, PropertyInfo(alias="privy-user-token")]]
    """Access token or custom authentication JWT for the user the request acts on."""
