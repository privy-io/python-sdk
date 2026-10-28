# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .mfa_passkey_authenticator_verify_options import MfaPasskeyAuthenticatorVerifyOptions

__all__ = ["PasskeyMfaVerificationInitResponse"]


class PasskeyMfaVerificationInitResponse(BaseModel):
    """WebAuthn authentication options for the started passkey MFA verification."""

    options: MfaPasskeyAuthenticatorVerifyOptions
    """
    WebAuthn authentication options as defined by the Web Authentication
    specification.
    """
