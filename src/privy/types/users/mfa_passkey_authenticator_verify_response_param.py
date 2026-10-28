# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .mfa_passkey_assertion_response_param import MfaPasskeyAssertionResponseParam
from .mfa_passkey_client_extension_results_param import MfaPasskeyClientExtensionResultsParam

__all__ = ["MfaPasskeyAuthenticatorVerifyResponseParam"]


class MfaPasskeyAuthenticatorVerifyResponseParam(TypedDict, total=False):
    """
    WebAuthn authentication response as defined by the Web Authentication specification.
    """

    id: Required[str]

    client_extension_results: Required[MfaPasskeyClientExtensionResultsParam]
    """Client extension results returned by the WebAuthn authenticator."""

    raw_id: Required[str]

    response: Required[MfaPasskeyAssertionResponseParam]
    """The authenticator assertion response from a WebAuthn authentication ceremony."""

    type: Required[Literal["public-key"]]

    authenticator_attachment: str
