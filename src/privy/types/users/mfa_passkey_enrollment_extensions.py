# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .mfa_passkey_cred_props_result import MfaPasskeyCredPropsResult

__all__ = ["MfaPasskeyEnrollmentExtensions"]


class MfaPasskeyEnrollmentExtensions(BaseModel):
    """Extensions for a WebAuthn registration ceremony."""

    app_id: Optional[str] = None

    cred_props: Optional[MfaPasskeyCredPropsResult] = None
    """The result of the WebAuthn credProps extension."""

    hmac_create_secret: Optional[bool] = None
