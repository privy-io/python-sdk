"""Hand-written public API layered on top of the generated client."""

from .client import PrivyClient
from .wallets import WalletsService
from .authorization import (
    PreparedRequest,
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    prepare_request,
    format_request_for_authorization_signature,
)
from .request_options import PrivyRequestOptions

__all__ = [
    "AuthorizationContext",
    "PreparedRequest",
    "PrivyClient",
    "PrivyRequestOptions",
    "WalletAPIRequestSignatureInput",
    "WalletsService",
    "format_request_for_authorization_signature",
    "prepare_request",
]
