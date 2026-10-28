# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MfaPasskeyAssertionResponseParam"]


class MfaPasskeyAssertionResponseParam(TypedDict, total=False):
    """The authenticator assertion response from a WebAuthn authentication ceremony."""

    authenticator_data: Required[str]

    client_data_json: Required[str]

    signature: Required[str]

    user_handle: str
