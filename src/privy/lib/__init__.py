"""Hand-written public API layered on top of the generated client."""

from .apps import PrivyAppsService
from .auth import (
    PrivyAppJWKS,
    PrivyAuthService,
    InvalidAuthTokenError,
    InvalidIdentityTokenError,
    VerifyAccessTokenResponse,
    verify_access_token,
    create_privy_app_jwks,
    verify_identity_token,
)
from .earn import PrivyEarnService, PrivyEarnEthereumService, PrivyEarnEthereumIncentiveService
from .tron import PrivyTronService
from .swaps import PrivySwapsService
from .users import PrivyUsersService
from .client import PrivyClient
from .payout import PrivyPayoutService, PrivyPayoutFiatService
from .solana import PrivySolanaService
from .intents import PrivyIntentsService
from .wallets import (
    WalletImport,
    HDWalletImport,
    PrivyWalletsService,
    PrivateKeyWalletImport,
    ExportPrivateKeyResponse,
    ExportSeedPhraseResponse,
)
from .ethereum import PrivyEthereumService
from .policies import PrivyPoliciesService
from .webhooks import WebhookPayload, InvalidWebhookError, PrivyWebhooksService
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
from .request_expiry import DEFAULT_REQUEST_EXPIRY_MS, DEFAULT_INTENT_REQUEST_EXPIRY_MS, PrivyRequestExpiryOptions
from .request_options import PrivyRequestOptions
from .deposit_accounts import PrivyDepositAccountsService, PrivyDepositAccountsCryptoService

__all__ = [
    "DEFAULT_INTENT_REQUEST_EXPIRY_MS",
    "DEFAULT_REQUEST_EXPIRY_MS",
    "AuthorizationContext",
    "ExportPrivateKeyResponse",
    "ExportSeedPhraseResponse",
    "InvalidAuthTokenError",
    "InvalidIdentityTokenError",
    "PrivyAppJWKS",
    "PrivyAuthService",
    "PrivyAppsService",
    "PrivyKeyQuorumsService",
    "PrivyIntentsService",
    "PrivyOrganizationsService",
    "P256KeyPair",
    "PreparedRequest",
    "PrivyTransactionsService",
    "PrivyClient",
    "PrivyEthereumService",
    "PrivyEarnService",
    "PrivyEarnEthereumService",
    "PrivyEarnEthereumIncentiveService",
    "PrivyDepositAccountsService",
    "PrivyDepositAccountsCryptoService",
    "PrivyPayoutService",
    "PrivyPayoutFiatService",
    "PrivyRequestOptions",
    "PrivyRequestExpiryOptions",
    "PrivySolanaService",
    "PrivySwapsService",
    "PrivyPoliciesService",
    "PrivyTronService",
    "VerifyAccessTokenResponse",
    "WalletAPIRequestSignatureInput",
    "HDWalletImport",
    "PrivateKeyWalletImport",
    "WalletImport",
    "PrivyWalletsService",
    "InvalidWebhookError",
    "PrivyWebhooksService",
    "WebhookPayload",
    "PrivyUsersService",
    "create_privy_app_jwks",
    "format_request_for_authorization_signature",
    "generate_authorization_signature",
    "generate_authorization_signatures",
    "generate_p256_key_pair",
    "prepare_request",
    "verify_access_token",
    "verify_identity_token",
]
