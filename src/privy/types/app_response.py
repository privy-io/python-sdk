# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .mfa_method import MfaMethod
from .captcha_provider import CaptchaProvider
from .app_allowlist_config import AppAllowlistConfig
from .app_custom_oauth_provider import AppCustomOAuthProvider
from .smart_wallet_configuration import SmartWalletConfiguration
from .telegram_auth_config_schema import TelegramAuthConfigSchema
from .embedded_wallet_config_schema import EmbeddedWalletConfigSchema
from .funding_config_response_schema import FundingConfigResponseSchema

__all__ = ["AppResponse"]


class AppResponse(BaseModel):
    """The response for getting an app."""

    id: str

    accent_color: Optional[str] = None

    allowed_domains: List[str]

    allowed_native_app_ids: List[str]

    allowed_native_app_url_schemes: List[str]

    allowlist_config: AppAllowlistConfig
    """Configuration for the allowlist error page shown to users not on the allowlist."""

    allowlist_enabled: bool

    apple_oauth: bool

    captcha_enabled: bool

    custom_api_url: Optional[str] = None

    custom_jwt_auth: bool

    custom_oauth_providers: List[AppCustomOAuthProvider]

    data_classification: Literal["public"]
    """
    Indicates that this response contains only publicly accessible data, not a
    privileged resource
    """

    disable_plus_emails: bool

    discord_oauth: bool

    email_auth: bool

    embedded_wallet_config: EmbeddedWalletConfigSchema
    """Configuration for embedded wallets including the mode."""

    enabled_captcha_provider: Optional[CaptchaProvider] = None
    """The captcha provider enabled for an app."""

    enforce_wallet_uis: bool

    external_wallets_for_signup_enabled: bool

    farcaster_auth: bool

    farcaster_link_wallets_enabled: bool

    fiat_on_ramp_enabled: bool

    github_oauth: bool

    google_oauth: bool

    guest_auth: bool

    icon_url: Optional[str] = None

    instagram_oauth: bool

    legacy_wallet_ui_config: bool

    line_oauth: bool

    linkedin_oauth: bool

    logo_url: Optional[str] = None

    max_linked_wallets_per_user: Optional[float] = None

    merge_accounts_by_email: bool

    mfa_methods: List[MfaMethod]

    name: str

    passkey_auth: bool

    passkeys_for_signup_enabled: bool

    privacy_policy_url: Optional[str] = None

    require_users_accept_terms: Optional[bool] = None

    show_wallet_login_first: bool

    smart_wallet_config: SmartWalletConfiguration
    """The configuration object for smart wallets."""

    sms_auth: bool

    solana_wallet_auth: bool

    spotify_oauth: bool

    telegram_auth: bool

    telegram_oauth: bool

    terms_and_conditions_url: Optional[str] = None

    theme: str

    tiktok_oauth: bool

    twitch_oauth: bool

    twitter_oauth: bool

    twitter_oauth_on_mobile_enabled: bool

    verification_key: str

    wallet_auth: bool

    wallet_connect_cloud_project_id: Optional[str] = None

    whatsapp_enabled: bool

    captcha_site_key: Optional[str] = None

    funding_config: Optional[FundingConfigResponseSchema] = None
    """Configuration for funding and on-ramp options."""

    telegram_auth_config: Optional[TelegramAuthConfigSchema] = None
    """Configuration for Telegram authentication."""

    telegram_seamless_auth_enabled: Optional[bool] = None
