"""Verification helpers for Privy-issued access and identity tokens."""

from __future__ import annotations

import json
import time
import base64
import threading
from typing import Union, Mapping, Sequence, cast
from dataclasses import dataclass
from typing_extensions import TypeAlias

import httpx
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature

from .._models import validate_type
from ..types.user import User
from .._exceptions import PrivyAPIError

__all__ = [
    "InvalidAuthTokenError",
    "InvalidIdentityTokenError",
    "PrivyAppJWKS",
    "PrivyAuthService",
    "VerifyAccessTokenResponse",
    "create_privy_app_jwks",
    "verify_access_token",
    "verify_identity_token",
]

JWT_ALGORITHM = "ES256"
JWT_ISSUER = "privy.io"
JWKS_CACHE_MAX_AGE_SECONDS = 60 * 60
JWKS_COOLDOWN_SECONDS = 10 * 60


class InvalidAuthTokenError(PrivyAPIError):
    """Raised when a Privy-issued token cannot be verified."""


class InvalidIdentityTokenError(PrivyAPIError):
    """Raised when a verified identity token has an invalid payload."""


@dataclass(frozen=True)
class VerifyAccessTokenResponse:
    """Claims extracted from a verified Privy access token."""

    app_id: str
    issuer: str
    issued_at: int
    expiration: int
    session_id: str
    user_id: str


class PrivyAppJWKS:
    """Discover and cache the public keys used to verify an app's Privy tokens."""

    def __init__(
        self,
        *,
        app_id: str,
        api_url: str,
        headers: Mapping[str, str] | None = None,
        verification_key_override: str | None = None,
        cache_max_age_seconds: float = JWKS_CACHE_MAX_AGE_SECONDS,
        cooldown_seconds: float = JWKS_COOLDOWN_SECONDS,
    ) -> None:
        self._url = f"{api_url.rstrip('/')}/v1/apps/{app_id}/jwks.json"
        self._headers = dict(headers or {})
        self._verification_key_override = verification_key_override
        self._cache_max_age_seconds = cache_max_age_seconds
        self._cooldown_seconds = cooldown_seconds
        self._keys: tuple[tuple[str | None, ec.EllipticCurvePublicKey], ...] = ()
        self._refreshed_at = 0.0
        self._override_key: ec.EllipticCurvePublicKey | None = None
        self._lock = threading.Lock()

    def get_key(self, key_id: str | None) -> ec.EllipticCurvePublicKey:
        """Return the matching key, refreshing remote JWKS data when necessary."""

        with self._lock:
            if self._verification_key_override is not None:
                if self._override_key is None:
                    try:
                        self._override_key = _load_verification_key(self._verification_key_override)
                    except InvalidAuthTokenError as exc:
                        raise InvalidAuthTokenError("Failed to import the provided verification key override") from exc
                return self._override_key

            now = time.monotonic()
            if not self._keys or now - self._refreshed_at >= self._cache_max_age_seconds:
                self._refresh(now)

            key = self._find_key(key_id)
            if key is not None:
                return key

            if now - self._refreshed_at >= self._cooldown_seconds:
                self._refresh(now)
                key = self._find_key(key_id)
                if key is not None:
                    return key

        raise InvalidAuthTokenError("Failed to verify authentication token")

    def _find_key(self, key_id: str | None) -> ec.EllipticCurvePublicKey | None:
        if key_id is not None:
            return next((key for candidate_id, key in self._keys if candidate_id == key_id), None)
        if len(self._keys) == 1:
            return self._keys[0][1]
        return None

    def _refresh(self, now: float) -> None:
        try:
            response = httpx.get(self._url, headers=self._headers)
            response.raise_for_status()
            raw_document: object = response.json()
            if not isinstance(raw_document, dict):
                raise ValueError("Invalid JWKS document")
            document = cast("dict[str, object]", raw_document)
            raw_keys = document.get("keys")
            if not isinstance(raw_keys, list):
                raise ValueError("Invalid JWKS document")
            keys = tuple(
                _load_jwk(jwk)
                for item in cast("list[object]", raw_keys)
                if isinstance(item, dict)
                for jwk in [cast("dict[str, object]", item)]
                if _is_compatible_jwk(jwk)
            )
            if not keys:
                raise ValueError("JWKS contains no compatible keys")
        except (httpx.HTTPError, json.JSONDecodeError, TypeError, ValueError) as exc:
            raise InvalidAuthTokenError("Failed to verify authentication token") from exc
        self._keys = keys
        self._refreshed_at = now


VerificationKey: TypeAlias = Union[str, ec.EllipticCurvePublicKey, PrivyAppJWKS]


def create_privy_app_jwks(
    *,
    app_id: str,
    api_url: str,
    headers: Mapping[str, str] | None = None,
    verification_key_override: str | None = None,
) -> PrivyAppJWKS:
    """Create a cached app JWKS resolver or a resolver backed by a fixed key override."""

    return PrivyAppJWKS(
        app_id=app_id,
        api_url=api_url,
        headers=headers,
        verification_key_override=verification_key_override,
    )


def verify_access_token(
    *, access_token: str, app_id: str, verification_key: VerificationKey
) -> VerifyAccessTokenResponse:
    """Verify a Privy access token and return its authentication claims."""

    payload = _verify_privy_issued_jwt(access_token, app_id, verification_key)
    return VerifyAccessTokenResponse(
        app_id=_required_string(payload.get("aud")),
        issuer=_required_string(payload.get("iss")),
        issued_at=_required_integer(payload.get("iat")),
        expiration=_required_integer(payload.get("exp")),
        session_id=_required_string(payload.get("sid")),
        user_id=_required_string(payload.get("sub")),
    )


def verify_identity_token(*, identity_token: str, app_id: str, verification_key: VerificationKey) -> User:
    """Verify a Privy identity token and parse its payload into a user."""

    payload = _verify_privy_issued_jwt(identity_token, app_id, verification_key)
    return _parse_user_from_identity_token_payload(payload)


class PrivyAuthService:
    """Client-bound Privy token verification helpers."""

    def __init__(self, app_id: str, app_jwks: PrivyAppJWKS) -> None:
        self._app_id = app_id
        self._app_jwks = app_jwks

    def verify_access_token(self, access_token: str) -> VerifyAccessTokenResponse:
        return verify_access_token(
            access_token=access_token,
            app_id=self._app_id,
            verification_key=self._app_jwks,
        )

    def verify_identity_token(self, identity_token: str) -> User:
        return verify_identity_token(
            identity_token=identity_token,
            app_id=self._app_id,
            verification_key=self._app_jwks,
        )


def _verify_privy_issued_jwt(jwt: str, app_id: str, verification_key: VerificationKey) -> dict[str, object]:
    try:
        parts = jwt.split(".")
        if len(parts) != 3:
            raise ValueError("JWT must have three segments")
        encoded_header, encoded_payload, encoded_signature = parts
        header = _decode_json_segment(encoded_header)
        payload = _decode_json_segment(encoded_payload)
        if header.get("typ") != "JWT" or header.get("alg") != JWT_ALGORITHM:
            raise ValueError("Unsupported JWT header")

        key = (
            verification_key.get_key(cast("str | None", header.get("kid")))
            if isinstance(verification_key, PrivyAppJWKS)
            else _load_verification_key(verification_key)
        )
        raw_signature = _base64url_decode(encoded_signature)
        if len(raw_signature) != 64:
            raise ValueError("Invalid ES256 signature")
        signature = encode_dss_signature(
            int.from_bytes(raw_signature[:32], "big"),
            int.from_bytes(raw_signature[32:], "big"),
        )
        key.verify(signature, f"{encoded_header}.{encoded_payload}".encode("ascii"), ec.ECDSA(hashes.SHA256()))

        now = time.time()
        if payload.get("iss") != JWT_ISSUER or not _audience_matches(payload.get("aud"), app_id):
            raise ValueError("Invalid JWT claims")
        expiration = payload.get("exp")
        if not isinstance(expiration, (int, float)) or isinstance(expiration, bool) or expiration <= now:
            raise _ExpiredTokenError
        not_before = payload.get("nbf")
        if not_before is not None and (
            not isinstance(not_before, (int, float)) or isinstance(not_before, bool) or not_before > now
        ):
            raise ValueError("Token is not active")
        return payload
    except _ExpiredTokenError as exc:
        raise InvalidAuthTokenError("Authentication token expired") from exc
    except InvalidAuthTokenError:
        raise
    except (InvalidSignature, UnicodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise InvalidAuthTokenError("Authentication token is invalid") from exc
    except Exception as exc:
        raise InvalidAuthTokenError("Failed to verify authentication token") from exc


def _load_verification_key(key: str | ec.EllipticCurvePublicKey) -> ec.EllipticCurvePublicKey:
    if isinstance(key, ec.EllipticCurvePublicKey):
        public_key = key
    else:
        try:
            loaded = serialization.load_pem_public_key(key.encode("utf-8"))
        except (TypeError, ValueError) as exc:
            raise InvalidAuthTokenError("Failed to import verification key") from exc
        if not isinstance(loaded, ec.EllipticCurvePublicKey):
            raise InvalidAuthTokenError("Verification key must be an elliptic curve public key")
        public_key = loaded
    if not isinstance(public_key.curve, ec.SECP256R1):
        raise InvalidAuthTokenError("Verification key must use the P-256 curve")
    return public_key


def _is_compatible_jwk(jwk: Mapping[str, object]) -> bool:
    return (
        jwk.get("kty") == "EC"
        and jwk.get("crv") == "P-256"
        and jwk.get("alg") in (None, JWT_ALGORITHM)
        and jwk.get("use") in (None, "sig")
    )


def _load_jwk(jwk: Mapping[str, object]) -> tuple[str | None, ec.EllipticCurvePublicKey]:
    x = _base64url_decode(_required_jwk_string(jwk.get("x")))
    y = _base64url_decode(_required_jwk_string(jwk.get("y")))
    if len(x) != 32 or len(y) != 32:
        raise ValueError("Invalid JWK coordinates")
    key_id = jwk.get("kid")
    if key_id is not None and not isinstance(key_id, str):
        raise ValueError("Invalid JWK key ID")
    key = ec.EllipticCurvePublicNumbers(int.from_bytes(x, "big"), int.from_bytes(y, "big"), ec.SECP256R1()).public_key()
    return key_id, key


def _decode_json_segment(segment: str) -> dict[str, object]:
    value: object = json.loads(_base64url_decode(segment))
    if not isinstance(value, dict):
        raise ValueError("JWT segment is not an object")
    return cast("dict[str, object]", value)


def _base64url_decode(value: str) -> bytes:
    return base64.b64decode(value + "=" * (-len(value) % 4), altchars=b"-_", validate=True)


def _audience_matches(audience: object, app_id: str) -> bool:
    if audience == app_id:
        return True
    if not isinstance(audience, list):
        return False
    audiences = cast("list[object]", audience)
    return all(isinstance(item, str) for item in audiences) and app_id in audiences


def _required_string(value: object) -> str:
    if not isinstance(value, str) or not value:
        raise InvalidAuthTokenError("Token's payload is invalid")
    return value


def _required_integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise InvalidAuthTokenError("Token's payload is invalid")
    return value


def _required_jwk_string(value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("Invalid JWK")
    return value


def _parse_user_from_identity_token_payload(payload: Mapping[str, object]) -> User:
    try:
        subject = payload.get("sub")
        if not isinstance(subject, str) or not subject:
            raise ValueError("Missing subject")
        linked_accounts_claim = payload.get("linked_accounts")
        if not isinstance(linked_accounts_claim, str):
            raise ValueError("Missing linked accounts")
        raw_accounts: object = json.loads(linked_accounts_claim)
        if not isinstance(raw_accounts, list):
            raise ValueError("Invalid linked accounts")
        parsed_accounts = cast("list[object]", raw_accounts)

        custom_metadata = _parse_custom_metadata(payload.get("custom_metadata"))
        user: dict[str, object] = {
            "id": subject,
            "created_at": _parse_created_at(payload.get("cr")),
            "is_guest": payload.get("guest") == "t",
            "linked_accounts": [
                mapped
                for account in parsed_accounts
                if isinstance(account, dict)
                for mapped in [_map_identity_linked_account(cast("dict[str, object]", account))]
                if mapped is not None
            ],
            "has_accepted_terms": False,
            "mfa_methods": [],
        }
        if custom_metadata is not None:
            user["custom_metadata"] = custom_metadata
        return validate_type(type_=User, value=user)
    except InvalidIdentityTokenError:
        raise
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        raise InvalidIdentityTokenError("Unable to parse identity token") from exc


def _parse_created_at(value: object) -> float:
    if value is None:
        return float("nan")
    if not isinstance(value, (str, int, float)) or isinstance(value, bool):
        raise ValueError("Invalid creation time")
    return float(value)


def _parse_custom_metadata(value: object) -> dict[str, str | float | bool] | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("Invalid custom metadata")
    raw_metadata: object = json.loads(value)
    if not isinstance(raw_metadata, dict):
        raise ValueError("Invalid custom metadata")
    parsed = cast("dict[object, object]", raw_metadata)
    if not all(isinstance(key, str) and isinstance(item, (str, int, float, bool)) for key, item in parsed.items()):
        raise ValueError("Invalid custom metadata")
    return cast("dict[str, str | float | bool]", parsed)


def _map_identity_linked_account(account: dict[str, object]) -> dict[str, object] | None:
    account_type = account.get("type")
    verified_at = account.get("lv")
    common = {
        "type": account_type,
        "first_verified_at": None,
        "verified_at": verified_at,
        "latest_verified_at": verified_at,
    }
    if account_type == "email":
        return {**common, "address": account.get("address")}
    if account_type == "phone":
        return {**common, "phoneNumber": account.get("phone_number")}
    if account_type == "wallet":
        chain_type = account.get("chain_type")
        if account.get("wallet_client_type") == "privy":
            return {
                **common,
                "id": account.get("id"),
                "address": account.get("address"),
                "chain_type": chain_type,
                "wallet_client_type": "privy",
                "wallet_client": "privy",
                "connector_type": "embedded",
                "chain_id": "",
                "delegated": False,
                "imported": False,
                "public_key": "",
                "wallet_index": 0,
                "recovery_method": "privy-v2" if account.get("id") else "privy",
            }
        return {
            **common,
            "address": account.get("address"),
            "chain_type": chain_type,
            "wallet_client": "unknown",
        }
    if account_type == "smart_wallet":
        return {
            **common,
            "address": account.get("address"),
            "smart_wallet_type": account.get("smart_wallet_type"),
        }
    if account_type == "farcaster":
        return {
            **common,
            "fid": account.get("fid"),
            "username": account.get("username"),
            "owner_address": account.get("oa"),
        }
    if account_type == "twitter_oauth":
        profile_picture = account.get("pfp")
        if isinstance(profile_picture, str):
            if profile_picture.startswith("default"):
                profile_picture = f"https://abs.twimg.com/sticky/default_profile_images/{profile_picture}"
            elif not profile_picture.startswith("https://"):
                profile_picture = f"https://pbs.twimg.com/profile_images/{profile_picture}"
        return {
            **common,
            "subject": account.get("subject"),
            "username": account.get("username"),
            "name": account.get("name"),
            "profile_picture_url": profile_picture,
        }
    oauth_fields: dict[str, Sequence[str]] = {
        "google_oauth": ("subject", "email", "name"),
        "discord_oauth": ("subject", "username"),
        "github_oauth": ("subject", "username"),
        "spotify_oauth": ("subject",),
        "instagram_oauth": ("subject", "username"),
        "tiktok_oauth": ("subject", "username"),
        "linkedin_oauth": ("subject", "email"),
        "apple_oauth": ("subject", "email"),
    }
    if isinstance(account_type, str) and account_type in oauth_fields:
        mapped = {**common, **{field: account.get(field) for field in oauth_fields[account_type]}}
        if account_type in {"discord_oauth", "github_oauth", "spotify_oauth"}:
            mapped["email"] = None
        if account_type in {"github_oauth", "spotify_oauth", "tiktok_oauth"}:
            mapped["name"] = None
        return mapped
    if account_type == "cross_app":
        return {
            **common,
            "subject": account.get("subject"),
            "provider_app_id": account.get("provider_app_id"),
            "embedded_wallets": account.get("embedded_wallets"),
            "smart_wallets": account.get("smart_wallets"),
        }
    if account_type == "custom_auth":
        return {**common, "custom_user_id": account.get("custom_user_id")}
    if account_type == "telegram":
        return {
            **common,
            "telegram_user_id": account.get("telegram_user_id"),
            "username": account.get("username"),
        }
    if account_type == "passkey":
        return {**common, "credential_id": account.get("credential_id"), "enrolled_in_mfa": False}
    return None


class _ExpiredTokenError(Exception):
    pass
