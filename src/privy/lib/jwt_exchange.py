"""User JWT to authorization-key exchange."""

from __future__ import annotations

import time
import base64
import threading
from collections import OrderedDict
from dataclasses import dataclass

from pyhpke import PyHPKEError

from ._hpke import HPKERecipient
from .._exceptions import PrivyAPIError
from ..resources.wallets.wallets import WalletsResource
from ..types.encrypted_wallet_authenticate_response import EncryptedWalletAuthenticateResponse

DEFAULT_AUTHORIZATION_KEY_CACHE_MAX_CAPACITY = 1000


@dataclass(frozen=True)
class _CacheEntry:
    authorization_key: str
    expires_at: float


class JWTExchangeService:
    """Exchanges and caches short-lived authorization keys for user JWTs."""

    def __init__(
        self,
        wallets: WalletsResource,
        *,
        cache_max_capacity: int | None = DEFAULT_AUTHORIZATION_KEY_CACHE_MAX_CAPACITY,
    ) -> None:
        if cache_max_capacity is not None and cache_max_capacity <= 0:
            raise ValueError("authorization_key_cache_max_capacity must be greater than zero")
        self._wallets = wallets
        self._recipient = HPKERecipient()
        self._cache_max_capacity = cache_max_capacity
        self._cache: OrderedDict[str, _CacheEntry] = OrderedDict()
        self._lock = threading.Lock()

    def exchange_jwt_for_authorization_key(self, jwt: str) -> str:
        cached = self._get_cached(jwt)
        if cached is not None:
            return cached

        response = self._wallets.authenticate_with_jwt(
            user_jwt=jwt,
            encryption_type="HPKE",
            recipient_public_key=base64.b64encode(self._recipient.public_key_spki).decode("ascii"),
        )
        if not isinstance(response, EncryptedWalletAuthenticateResponse):
            raise PrivyAPIError("JWT exchange failed: unsupported encryption type")

        encrypted = response.encrypted_authorization_key
        if encrypted.encryption_type != "HPKE":
            raise PrivyAPIError("JWT exchange failed: unsupported encryption type")
        try:
            plaintext = self._recipient.decrypt(
                base64.b64decode(encrypted.encapsulated_key, validate=True),
                base64.b64decode(encrypted.ciphertext, validate=True),
            )
            authorization_key = plaintext.decode("utf-8")
        except (PyHPKEError, ValueError, UnicodeDecodeError) as exc:
            raise PrivyAPIError("JWT exchange failed: invalid encrypted authorization key") from exc

        self._put_cached(jwt, authorization_key, response.expires_at)
        return authorization_key

    def _get_cached(self, jwt: str) -> str | None:
        if self._cache_max_capacity is None:
            return None

        with self._lock:
            entry = self._cache.get(jwt)
            if entry is None:
                return None
            if entry.expires_at <= time.time() * 1000:
                del self._cache[jwt]
                return None
            self._cache.move_to_end(jwt)
            return entry.authorization_key

    def _put_cached(self, jwt: str, authorization_key: str, expires_at: float) -> None:
        if self._cache_max_capacity is None:
            return

        with self._lock:
            self._cache[jwt] = _CacheEntry(authorization_key, expires_at)
            self._cache.move_to_end(jwt)
            while len(self._cache) > self._cache_max_capacity:
                self._cache.popitem(last=False)
