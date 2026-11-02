# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ...mfa_passkey_authenticator_enrollment_response_param import MfaPasskeyAuthenticatorEnrollmentResponseParam

__all__ = ["EnrollmentVerifyParams"]


class EnrollmentVerifyParams(TypedDict, total=False):
    credential: Required[MfaPasskeyAuthenticatorEnrollmentResponseParam]
    """
    WebAuthn registration response as defined by the Web Authentication
    specification.
    """

    user_jwt: Required[Annotated[str, PropertyInfo(alias="privy-user-token")]]
    """Access token or custom authentication JWT for the user the request acts on."""
