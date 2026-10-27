# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .totp_mfa_enrollment_options import TotpMfaEnrollmentOptions

__all__ = ["TotpMfaEnrollmentInitResponse"]


class TotpMfaEnrollmentInitResponse(BaseModel):
    """Authenticator setup information for the started TOTP MFA enrollment."""

    options: TotpMfaEnrollmentOptions
    """Authenticator setup information for TOTP MFA enrollment."""
