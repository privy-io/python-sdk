# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["VerificationVerifyParams"]


class VerificationVerifyParams(TypedDict, total=False):
    code: Required[str]

    privy_user_token: Required[Annotated[str, PropertyInfo(alias="privy-user-token")]]
    """Access token or custom authentication JWT for the user the request acts on."""
