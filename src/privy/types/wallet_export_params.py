# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .hpke_encryption import HpkeEncryption

__all__ = ["WalletExportParams"]


class WalletExportParams(TypedDict, total=False):
    encryption_type: Required[HpkeEncryption]
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""

    recipient_public_key: Required[str]
    """
    The base64-encoded encryption public key to encrypt the wallet private key with.
    """

    export_seed_phrase: bool

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
