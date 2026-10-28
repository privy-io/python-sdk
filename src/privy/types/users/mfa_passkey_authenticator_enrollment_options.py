# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .mfa_passkey_user import MfaPasskeyUser
from .mfa_passkey_relying_party import MfaPasskeyRelyingParty
from .mfa_passkey_pub_key_cred_param import MfaPasskeyPubKeyCredParam
from .mfa_passkey_credential_descriptor import MfaPasskeyCredentialDescriptor
from .mfa_passkey_enrollment_extensions import MfaPasskeyEnrollmentExtensions
from .mfa_passkey_authenticator_selection import MfaPasskeyAuthenticatorSelection

__all__ = ["MfaPasskeyAuthenticatorEnrollmentOptions"]


class MfaPasskeyAuthenticatorEnrollmentOptions(BaseModel):
    """
    WebAuthn registration options as defined by the Web Authentication specification.
    """

    challenge: str

    pub_key_cred_params: List[MfaPasskeyPubKeyCredParam]

    rp: MfaPasskeyRelyingParty
    """Relying party information for a WebAuthn ceremony."""

    user: MfaPasskeyUser
    """User entity for a WebAuthn registration ceremony."""

    attestation: Optional[str] = None

    authenticator_selection: Optional[MfaPasskeyAuthenticatorSelection] = None
    """Authenticator selection criteria for a WebAuthn registration ceremony."""

    exclude_credentials: Optional[List[MfaPasskeyCredentialDescriptor]] = None

    extensions: Optional[MfaPasskeyEnrollmentExtensions] = None
    """Extensions for a WebAuthn registration ceremony."""

    timeout: Optional[float] = None
