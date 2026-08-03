# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WalletAuthenticateWithJwtParams"]


class WalletAuthenticateWithJwtParams(TypedDict, total=False):
    encryption_type: Required[Literal["HPKE"]]
    """The encryption type for the authentication response.

    Currently only supports HPKE.
    """

    recipient_public_key: Required[str]
    """
    The public key of your ECDH keypair, in base64-encoded, SPKI-format, whose
    private key will be able to decrypt the session key.
    """

    user_jwt: Required[str]
    """The user's JWT, to be used to authenticate the user."""
