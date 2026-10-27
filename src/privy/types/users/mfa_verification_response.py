# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..user import User
from ..._models import BaseModel

__all__ = ["MfaVerificationResponse"]


class MfaVerificationResponse(BaseModel):
    """An MFA token and the current user after completing an MFA ceremony."""

    token: str
    """JWT proving the user completed MFA."""

    expires_at: int
    """Unix timestamp in seconds when the MFA token expires."""

    user: User
    """A Privy user object."""
