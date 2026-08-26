"""Hand-written public API layered on top of the generated client."""

from .client import PrivyClient
from .wallets import WalletsService
from .authorization import (
    P256KeyPair,
    PreparedRequest,
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    prepare_request,
    generate_p256_key_pair,
    generate_authorization_signature,
    format_request_for_authorization_signature,
)
from .request_options import PrivyRequestOptions

__all__ = [
    "AuthorizationContext",
    "P256KeyPair",
    "PreparedRequest",
    "PrivyClient",
    "PrivyRequestOptions",
    "WalletAPIRequestSignatureInput",
    "WalletsService",
    "format_request_for_authorization_signature",
    "generate_authorization_signature",
    "generate_p256_key_pair",
    "prepare_request",
]
