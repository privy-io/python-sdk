# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MfaPasskeyAuthenticatorSelection"]


class MfaPasskeyAuthenticatorSelection(BaseModel):
    """Authenticator selection criteria for a WebAuthn registration ceremony."""

    authenticator_attachment: Optional[str] = None

    require_resident_key: Optional[bool] = None

    resident_key: Optional[str] = None

    user_verification: Optional[str] = None
