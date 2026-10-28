# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .mfa_passkey_authenticator_enrollment_options import MfaPasskeyAuthenticatorEnrollmentOptions

__all__ = ["PasskeyMfaEnrollmentInitResponse"]


class PasskeyMfaEnrollmentInitResponse(BaseModel):
    """WebAuthn registration options for the started passkey MFA enrollment."""

    options: MfaPasskeyAuthenticatorEnrollmentOptions
    """
    WebAuthn registration options as defined by the Web Authentication
    specification.
    """
