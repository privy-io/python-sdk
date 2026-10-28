# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .mfa_passkey_cred_props_result_param import MfaPasskeyCredPropsResultParam

__all__ = ["MfaPasskeyClientExtensionResultsParam"]


class MfaPasskeyClientExtensionResultsParam(TypedDict, total=False):
    """Client extension results returned by the WebAuthn authenticator."""

    app_id: bool

    cred_props: MfaPasskeyCredPropsResultParam
    """The result of the WebAuthn credProps extension."""

    hmac_create_secret: bool
