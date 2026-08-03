# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

from .custom_oauth_provider_id import CustomOAuthProviderID

__all__ = ["LinkedAccountTypeParam"]

LinkedAccountTypeParam: TypeAlias = Union[
    Literal[
        "email",
        "phone",
        "wallet",
        "smart_wallet",
        "google_oauth",
        "twitter_oauth",
        "discord_oauth",
        "github_oauth",
        "spotify_oauth",
        "instagram_oauth",
        "tiktok_oauth",
        "line_oauth",
        "twitch_oauth",
        "linkedin_oauth",
        "apple_oauth",
        "custom_auth",
        "farcaster",
        "passkey",
        "telegram",
        "cross_app",
        "authorization_key",
    ],
    CustomOAuthProviderID,
]
