"""Hand-written public API layered on top of the generated client."""

from .apps import PrivyAppsService
from .tron import PrivyTronService
from .users import PrivyUsersService
from .client import PrivyClient
from .solana import PrivySolanaService
from .intents import PrivyIntentsService
from .wallets import PrivyWalletsService
from .ethereum import PrivyEthereumService
from .policies import PrivyPoliciesService
from .webhooks import PrivyWebhooksService
from .key_quorums import PrivyKeyQuorumsService
from .transactions import PrivyTransactionsService
from .authorization import (
    P256KeyPair,
    PreparedRequest,
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    prepare_request,
    generate_p256_key_pair,
    generate_authorization_signature,
    generate_authorization_signatures,
    format_request_for_authorization_signature,
)
from .organizations import PrivyOrganizationsService
from .request_expiry import PrivyRequestExpiryOptions
from .request_options import PrivyRequestOptions

__all__ = [
    "AuthorizationContext",
    "PrivyAppsService",
    "PrivyKeyQuorumsService",
    "PrivyIntentsService",
    "PrivyOrganizationsService",
    "P256KeyPair",
    "PreparedRequest",
    "PrivyTransactionsService",
    "PrivyClient",
    "PrivyEthereumService",
    "PrivyRequestOptions",
    "PrivyRequestExpiryOptions",
    "PrivySolanaService",
    "PrivyPoliciesService",
    "PrivyTronService",
    "WalletAPIRequestSignatureInput",
    "PrivyWalletsService",
    "PrivyWebhooksService",
    "PrivyUsersService",
    "format_request_for_authorization_signature",
    "generate_authorization_signature",
    "generate_authorization_signatures",
    "generate_p256_key_pair",
    "prepare_request",
]
