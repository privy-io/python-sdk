# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .linked_account_line_input_param import LinkedAccountLineInputParam
from .linked_account_apple_input_param import LinkedAccountAppleInputParam
from .linked_account_email_input_param import LinkedAccountEmailInputParam
from .linked_account_phone_input_param import LinkedAccountPhoneInputParam
from .linked_account_github_input_param import LinkedAccountGitHubInputParam
from .linked_account_google_input_param import LinkedAccountGoogleInputParam
from .linked_account_tiktok_input_param import LinkedAccountTiktokInputParam
from .linked_account_twitch_input_param import LinkedAccountTwitchInputParam
from .linked_account_wallet_input_param import LinkedAccountWalletInputParam
from .linked_account_discord_input_param import LinkedAccountDiscordInputParam
from .linked_account_passkey_input_param import LinkedAccountPasskeyInputParam
from .linked_account_spotify_input_param import LinkedAccountSpotifyInputParam
from .linked_account_twitter_input_param import LinkedAccountTwitterInputParam
from .linked_account_telegram_input_param import LinkedAccountTelegramInputParam
from .linked_account_farcaster_input_param import LinkedAccountFarcasterInputParam
from .linked_account_instagram_input_param import LinkedAccountInstagramInputParam
from .linked_account_linked_in_input_param import LinkedAccountLinkedInInputParam
from .linked_account_custom_jwt_input_param import LinkedAccountCustomJwtInputParam

__all__ = ["LinkedAccountInputParam"]

LinkedAccountInputParam: TypeAlias = Union[
    LinkedAccountWalletInputParam,
    LinkedAccountEmailInputParam,
    LinkedAccountPhoneInputParam,
    LinkedAccountGoogleInputParam,
    LinkedAccountTwitterInputParam,
    LinkedAccountDiscordInputParam,
    LinkedAccountGitHubInputParam,
    LinkedAccountSpotifyInputParam,
    LinkedAccountInstagramInputParam,
    LinkedAccountTiktokInputParam,
    LinkedAccountLineInputParam,
    LinkedAccountTwitchInputParam,
    LinkedAccountAppleInputParam,
    LinkedAccountLinkedInInputParam,
    LinkedAccountFarcasterInputParam,
    LinkedAccountTelegramInputParam,
    LinkedAccountCustomJwtInputParam,
    LinkedAccountPasskeyInputParam,
]
