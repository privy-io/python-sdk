# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .mfa_passkey_attestation_response_param import MfaPasskeyAttestationResponseParam
from .mfa_passkey_client_extension_results_param import MfaPasskeyClientExtensionResultsParam

__all__ = ["MfaPasskeyAuthenticatorEnrollmentResponseParam"]


class MfaPasskeyAuthenticatorEnrollmentResponseParam(TypedDict, total=False):
    """
    WebAuthn registration response as defined by the Web Authentication specification.
    """

    id: Required[str]

    client_extension_results: Required[MfaPasskeyClientExtensionResultsParam]
    """Client extension results returned by the WebAuthn authenticator."""

    raw_id: Required[str]

    response: Required[MfaPasskeyAttestationResponseParam]
    """The authenticator attestation response from a WebAuthn registration ceremony."""

    type: Required[Literal["public-key"]]

    authenticator_attachment: str
