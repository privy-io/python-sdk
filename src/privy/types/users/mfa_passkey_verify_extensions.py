# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MfaPasskeyVerifyExtensions"]


class MfaPasskeyVerifyExtensions(BaseModel):
    """Extensions for a WebAuthn authentication ceremony."""

    app_id: Optional[str] = None

    cred_props: Optional[bool] = None

    hmac_create_secret: Optional[bool] = None
