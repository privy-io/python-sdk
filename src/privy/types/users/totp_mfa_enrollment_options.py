# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TotpMfaEnrollmentOptions"]


class TotpMfaEnrollmentOptions(BaseModel):
    """Authenticator setup information for TOTP MFA enrollment."""

    secret: str
    """Base32-encoded TOTP secret."""

    uri: str
    """Authenticator setup URI using the otpauth scheme."""
