# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["EnrollmentInitParams"]


class EnrollmentInitParams(TypedDict, total=False):
    phone_number: Required[str]

    privy_user_token: Required[Annotated[str, PropertyInfo(alias="privy-user-token")]]
    """Access token or custom authentication JWT for the user the request acts on."""

    privy_mfa_token: Annotated[str, PropertyInfo(alias="privy-mfa-token")]
    """
    MFA token from a completed MFA verification, required on MFA-protected requests
    for users with MFA enrolled.
    """
