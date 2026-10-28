# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .mfa_passkey_verify_extensions import MfaPasskeyVerifyExtensions
from .mfa_passkey_credential_descriptor import MfaPasskeyCredentialDescriptor

__all__ = ["MfaPasskeyAuthenticatorVerifyOptions"]


class MfaPasskeyAuthenticatorVerifyOptions(BaseModel):
    """
    WebAuthn authentication options as defined by the Web Authentication specification.
    """

    challenge: str

    allow_credentials: Optional[List[MfaPasskeyCredentialDescriptor]] = None

    extensions: Optional[MfaPasskeyVerifyExtensions] = None
    """Extensions for a WebAuthn authentication ceremony."""

    rp_id: Optional[str] = None

    timeout: Optional[float] = None

    user_verification: Optional[str] = None
