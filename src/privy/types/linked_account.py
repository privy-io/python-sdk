# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .linked_account_email import LinkedAccountEmail
from .linked_account_phone import LinkedAccountPhone
from .linked_account_solana import LinkedAccountSolana
from .linked_account_passkey import LinkedAccountPasskey
from .linked_account_ethereum import LinkedAccountEthereum
from .linked_account_telegram import LinkedAccountTelegram
from .linked_account_cross_app import LinkedAccountCrossApp
from .linked_account_farcaster import LinkedAccountFarcaster
from .linked_account_custom_jwt import LinkedAccountCustomJwt
from .linked_account_line_oauth import LinkedAccountLineOAuth
from .linked_account_apple_oauth import LinkedAccountAppleOAuth
from .linked_account_custom_oauth import LinkedAccountCustomOAuth
from .linked_account_github_oauth import LinkedAccountGitHubOAuth
from .linked_account_google_oauth import LinkedAccountGoogleOAuth
from .linked_account_smart_wallet import LinkedAccountSmartWallet
from .linked_account_tiktok_oauth import LinkedAccountTiktokOAuth
from .linked_account_twitch_oauth import LinkedAccountTwitchOAuth
from .linked_account_discord_oauth import LinkedAccountDiscordOAuth
from .linked_account_spotify_oauth import LinkedAccountSpotifyOAuth
from .linked_account_twitter_oauth import LinkedAccountTwitterOAuth
from .linked_account_instagram_oauth import LinkedAccountInstagramOAuth
from .linked_account_linked_in_oauth import LinkedAccountLinkedInOAuth
from .linked_account_authorization_key import LinkedAccountAuthorizationKey
from .linked_account_solana_embedded_wallet import LinkedAccountSolanaEmbeddedWallet
from .linked_account_ethereum_embedded_wallet import LinkedAccountEthereumEmbeddedWallet
from .linked_account_curve_signing_embedded_wallet import LinkedAccountCurveSigningEmbeddedWallet
from .linked_account_bitcoin_segwit_embedded_wallet import LinkedAccountBitcoinSegwitEmbeddedWallet
from .linked_account_bitcoin_taproot_embedded_wallet import LinkedAccountBitcoinTaprootEmbeddedWallet

__all__ = ["LinkedAccount"]

LinkedAccount: TypeAlias = Union[
    LinkedAccountEmail,
    LinkedAccountPhone,
    LinkedAccountEthereum,
    LinkedAccountSolana,
    LinkedAccountSmartWallet,
    LinkedAccountEthereumEmbeddedWallet,
    LinkedAccountSolanaEmbeddedWallet,
    LinkedAccountBitcoinSegwitEmbeddedWallet,
    LinkedAccountBitcoinTaprootEmbeddedWallet,
    LinkedAccountCurveSigningEmbeddedWallet,
    LinkedAccountGoogleOAuth,
    LinkedAccountTwitterOAuth,
    LinkedAccountDiscordOAuth,
    LinkedAccountGitHubOAuth,
    LinkedAccountSpotifyOAuth,
    LinkedAccountInstagramOAuth,
    LinkedAccountTiktokOAuth,
    LinkedAccountLineOAuth,
    LinkedAccountTwitchOAuth,
    LinkedAccountLinkedInOAuth,
    LinkedAccountAppleOAuth,
    LinkedAccountCustomOAuth,
    LinkedAccountCustomJwt,
    LinkedAccountFarcaster,
    LinkedAccountPasskey,
    LinkedAccountTelegram,
    LinkedAccountCrossApp,
    LinkedAccountAuthorizationKey,
]
