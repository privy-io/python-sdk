# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .linked_account_passkey_credential_device_type import LinkedAccountPasskeyCredentialDeviceType

__all__ = ["LinkedAccountPasskeyInputParam"]


class LinkedAccountPasskeyInputParam(TypedDict, total=False):
    """The payload for importing a passkey account."""

    credential_device_type: Required[LinkedAccountPasskeyCredentialDeviceType]
    """
    WebAuthn credential device type indicating platform or cross-platform
    authenticator residency.
    """

    credential_id: Required[str]

    credential_public_key: Required[str]

    credential_username: Required[str]

    type: Required[Literal["passkey"]]
