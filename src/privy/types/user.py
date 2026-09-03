# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "User",
    "LinkedAccount",
    "LinkedAccountEmail",
    "LinkedAccountPhone",
    "LinkedAccountCrossApp",
    "LinkedAccountCrossAppEmbeddedWallet",
    "LinkedAccountCrossAppSmartWallet",
    "LinkedAccountAuthorizationKey",
    "LinkedAccountCustomJwt",
    "LinkedAccountApple",
    "LinkedAccountDiscord",
    "LinkedAccountGitHub",
    "LinkedAccountGoogle",
    "LinkedAccountInstagram",
    "LinkedAccountLinkedIn",
    "LinkedAccountSpotify",
    "LinkedAccountTiktok",
    "LinkedAccountLine",
    "LinkedAccountTwitter",
    "LinkedAccountSmartWallet",
    "LinkedAccountPasskey",
    "LinkedAccountFarcaster",
    "LinkedAccountEthereum",
    "LinkedAccountEthereumEmbeddedWallet",
    "LinkedAccountSolana",
    "LinkedAccountSolanaEmbeddedWallet",
    "LinkedAccountBitcoinSegwitEmbeddedWallet",
    "LinkedAccountBitcoinTaprootEmbeddedWallet",
    "LinkedAccountTelegram",
    "MfaMethod",
    "MfaMethodPasskey",
    "MfaMethodSMS",
    "MfaMethodTotp",
]


class LinkedAccountEmail(BaseModel):
    address: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["email"]

    verified_at: Optional[float] = None


class LinkedAccountPhone(BaseModel):
    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    phone_number: str = FieldInfo(alias="phoneNumber")

    type: Literal["phone"]

    verified_at: Optional[float] = None

    number: Optional[str] = None


class LinkedAccountCrossAppEmbeddedWallet(BaseModel):
    address: str


class LinkedAccountCrossAppSmartWallet(BaseModel):
    address: str


class LinkedAccountCrossApp(BaseModel):
    embedded_wallets: List[LinkedAccountCrossAppEmbeddedWallet]

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    provider_app_id: str

    smart_wallets: List[LinkedAccountCrossAppSmartWallet]

    subject: str

    type: Literal["cross_app"]

    verified_at: Optional[float] = None


class LinkedAccountAuthorizationKey(BaseModel):
    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    public_key: str

    type: Literal["authorization_key"]

    verified_at: float


class LinkedAccountCustomJwt(BaseModel):
    custom_user_id: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["custom_auth"]

    verified_at: Optional[float] = None


class LinkedAccountApple(BaseModel):
    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: Literal["apple_oauth"]

    verified_at: Optional[float] = None


class LinkedAccountDiscord(BaseModel):
    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: Literal["discord_oauth"]

    username: Optional[str] = None

    verified_at: Optional[float] = None


class LinkedAccountGitHub(BaseModel):
    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    subject: str

    type: Literal["github_oauth"]

    username: Optional[str] = None

    verified_at: Optional[float] = None


class LinkedAccountGoogle(BaseModel):
    email: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    subject: str

    type: Literal["google_oauth"]

    verified_at: Optional[float] = None


class LinkedAccountInstagram(BaseModel):
    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: Literal["instagram_oauth"]

    username: Optional[str] = None

    verified_at: Optional[float] = None


class LinkedAccountLinkedIn(BaseModel):
    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: Literal["linkedin_oauth"]

    verified_at: Optional[float] = None

    name: Optional[str] = None

    vanity_name: Optional[str] = None


class LinkedAccountSpotify(BaseModel):
    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    subject: str

    type: Literal["spotify_oauth"]

    verified_at: Optional[float] = None


class LinkedAccountTiktok(BaseModel):
    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    subject: str

    type: Literal["tiktok_oauth"]

    username: Optional[str] = None

    verified_at: Optional[float] = None


class LinkedAccountLine(BaseModel):
    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    profile_picture_url: Optional[str] = None

    subject: str

    type: Literal["line_oauth"]

    verified_at: float


class LinkedAccountTwitter(BaseModel):
    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    profile_picture_url: Optional[str] = None

    subject: str

    type: Literal["twitter_oauth"]

    username: Optional[str] = None

    verified_at: Optional[float] = None


class LinkedAccountSmartWallet(BaseModel):
    address: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    smart_wallet_type: Literal[
        "safe",
        "kernel",
        "biconomy",
        "light_account",
        "coinbase_smart_wallet",
        "thirdweb",
    ]

    type: Literal["smart_wallet"]

    verified_at: Optional[float] = None


class LinkedAccountPasskey(BaseModel):
    credential_id: str

    enrolled_in_mfa: bool

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["passkey"]

    verified_at: Optional[float] = None

    authenticator_name: Optional[str] = None

    created_with_browser: Optional[str] = None

    created_with_device: Optional[str] = None

    created_with_os: Optional[str] = None


class LinkedAccountFarcaster(BaseModel):
    fid: float

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    owner_address: str

    type: Literal["farcaster"]

    verified_at: Optional[float] = None

    bio: Optional[str] = None

    display_name: Optional[str] = None

    homepage_url: Optional[str] = None

    profile_picture: Optional[str] = None

    profile_picture_url: Optional[str] = None

    signer_public_key: Optional[str] = None

    username: Optional[str] = None


class LinkedAccountEthereum(BaseModel):
    address: str

    chain_type: Literal["ethereum"]

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["wallet"]

    verified_at: Optional[float] = None

    wallet_client: Literal["unknown"]

    chain_id: Optional[str] = None

    connector_type: Optional[str] = None

    wallet_client_type: Optional[str] = None


class LinkedAccountEthereumEmbeddedWallet(BaseModel):
    id: Optional[str] = None

    address: str

    chain_id: str

    chain_type: Literal["ethereum"]

    connector_type: Literal["embedded"]

    delegated: bool

    first_verified_at: Optional[float] = None

    imported: bool

    latest_verified_at: Optional[float] = None

    recovery_method: Literal[
        "privy",
        "user-passcode",
        "google-drive",
        "icloud",
        "recovery-encryption-key",
        "privy-v2",
    ]

    type: Literal["wallet"]

    verified_at: Optional[float] = None

    wallet_client: Literal["privy"]

    wallet_client_type: Literal["privy"]

    wallet_index: float


class LinkedAccountSolana(BaseModel):
    address: str

    chain_type: Literal["solana"]

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["wallet"]

    verified_at: Optional[float] = None

    wallet_client: Literal["unknown"]

    connector_type: Optional[str] = None

    wallet_client_type: Optional[str] = None


class LinkedAccountSolanaEmbeddedWallet(BaseModel):
    id: Optional[str] = None

    address: str

    chain_id: str

    chain_type: Literal["solana"]

    connector_type: Literal["embedded"]

    delegated: bool

    first_verified_at: Optional[float] = None

    imported: bool

    latest_verified_at: Optional[float] = None

    public_key: str

    recovery_method: Literal[
        "privy",
        "user-passcode",
        "google-drive",
        "icloud",
        "recovery-encryption-key",
        "privy-v2",
    ]

    type: Literal["wallet"]

    verified_at: Optional[float] = None

    wallet_client: Literal["privy"]

    wallet_client_type: Literal["privy"]

    wallet_index: float


class LinkedAccountBitcoinSegwitEmbeddedWallet(BaseModel):
    id: Optional[str] = None

    address: str

    chain_id: str

    chain_type: Literal["bitcoin-segwit"]

    connector_type: Literal["embedded"]

    delegated: bool

    first_verified_at: Optional[float] = None

    imported: bool

    latest_verified_at: Optional[float] = None

    public_key: str

    recovery_method: Literal[
        "privy",
        "user-passcode",
        "google-drive",
        "icloud",
        "recovery-encryption-key",
        "privy-v2",
    ]

    type: Literal["wallet"]

    verified_at: Optional[float] = None

    wallet_client: Literal["privy"]

    wallet_client_type: Literal["privy"]

    wallet_index: float


class LinkedAccountBitcoinTaprootEmbeddedWallet(BaseModel):
    id: Optional[str] = None

    address: str

    chain_id: str

    chain_type: Literal["bitcoin-taproot"]

    connector_type: Literal["embedded"]

    delegated: bool

    first_verified_at: Optional[float] = None

    imported: bool

    latest_verified_at: Optional[float] = None

    public_key: str

    recovery_method: Literal[
        "privy",
        "user-passcode",
        "google-drive",
        "icloud",
        "recovery-encryption-key",
        "privy-v2",
    ]

    type: Literal["wallet"]

    verified_at: Optional[float] = None

    wallet_client: Literal["privy"]

    wallet_client_type: Literal["privy"]

    wallet_index: float


class LinkedAccountTelegram(BaseModel):
    telegram_user_id: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["telegram"]

    verified_at: Optional[float] = None

    username: str


LinkedAccount: TypeAlias = Union[
    LinkedAccountEmail,
    LinkedAccountPhone,
    LinkedAccountCrossApp,
    LinkedAccountAuthorizationKey,
    LinkedAccountCustomJwt,
    LinkedAccountApple,
    LinkedAccountDiscord,
    LinkedAccountGitHub,
    LinkedAccountGoogle,
    LinkedAccountInstagram,
    LinkedAccountLinkedIn,
    LinkedAccountSpotify,
    LinkedAccountTiktok,
    LinkedAccountLine,
    LinkedAccountTwitter,
    LinkedAccountSmartWallet,
    LinkedAccountPasskey,
    LinkedAccountFarcaster,
    LinkedAccountEthereum,
    LinkedAccountEthereumEmbeddedWallet,
    LinkedAccountSolana,
    LinkedAccountSolanaEmbeddedWallet,
    LinkedAccountBitcoinSegwitEmbeddedWallet,
    LinkedAccountBitcoinTaprootEmbeddedWallet,
    LinkedAccountTelegram,
]


class MfaMethodPasskey(BaseModel):
    type: Literal["passkey"]

    verified_at: float


class MfaMethodSMS(BaseModel):
    type: Literal["sms"]

    verified_at: float


class MfaMethodTotp(BaseModel):
    type: Literal["totp"]

    verified_at: float


MfaMethod: TypeAlias = Union[MfaMethodPasskey, MfaMethodSMS, MfaMethodTotp]


class User(BaseModel):
    id: str

    created_at: float
    """Unix timestamp of when the user was created in milliseconds."""

    has_accepted_terms: Optional[bool] = None
    """Indicates if the user has accepted the terms of service."""

    is_guest: bool
    """Indicates if the user is a guest account user."""

    linked_accounts: List[LinkedAccount]

    mfa_methods: Optional[List[MfaMethod]] = None

    custom_metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """Custom metadata associated with the user."""
