"""Public Privy client."""

from __future__ import annotations

import time
from types import TracebackType

from .users import UsersService
from .intents import IntentsService
from .wallets import WalletsService
from .._client import PrivyAPI
from .policies import PoliciesService
from .._version import __version__
from .key_quorums import KeyQuorumsService
from .jwt_exchange import DEFAULT_AUTHORIZATION_KEY_CACHE_MAX_CAPACITY, JWTExchangeService
from .transactions import TransactionsService
from .request_expiry import (
    DEFAULT_REQUEST_EXPIRY_MS,
    DEFAULT_INTENT_REQUEST_EXPIRY_MS,
    PrivyRequestExpiryOptions,
)

__all__ = ["PrivyClient", "PrivyRequestExpiryOptions"]


class PrivyClient:
    """Synchronous entrypoint for the Privy API."""

    def __init__(
        self,
        *,
        app_id: str,
        app_secret: str,
        base_url: str,
        authorization_key_cache_max_capacity: int = DEFAULT_AUTHORIZATION_KEY_CACHE_MAX_CAPACITY,
        request_expiry: PrivyRequestExpiryOptions | None = None,
    ) -> None:
        request_expiry_options = request_expiry or PrivyRequestExpiryOptions()
        self._request_expiry_disabled = request_expiry_options.disabled
        self._default_request_expiry_ms = (
            DEFAULT_REQUEST_EXPIRY_MS
            if request_expiry_options.default_ms is None
            else request_expiry_options.default_ms
        )
        self._default_intent_request_expiry_ms = (
            DEFAULT_INTENT_REQUEST_EXPIRY_MS
            if request_expiry_options.default_intent_ms is None
            else request_expiry_options.default_intent_ms
        )
        self._client = PrivyAPI(
            app_id=app_id,
            app_secret=app_secret,
            base_url=base_url,
            default_headers={"privy-client": f"python:{__version__}"},
        )
        self.policies = PoliciesService(self._client, self.get_request_expiry)
        self.key_quorums = KeyQuorumsService(self._client, self.get_request_expiry)
        self.intents = IntentsService(self._client, self._get_intent_request_expiry)
        self.users = UsersService(self._client)
        self.transactions = TransactionsService(self._client)
        self._jwt_exchange = JWTExchangeService(
            self._client.wallets,
            cache_max_capacity=authorization_key_cache_max_capacity,
        )
        self.wallets = WalletsService(self._client, self._jwt_exchange, self.get_request_expiry)

    def get_request_expiry(self, expiry_ms_from_now: int | None = None) -> int | None:
        """Return an absolute request-expiry timestamp in Unix milliseconds."""

        if self._request_expiry_disabled:
            return None
        duration = self._default_request_expiry_ms if expiry_ms_from_now is None else expiry_ms_from_now
        return time.time_ns() // 1_000_000 + duration

    def _get_intent_request_expiry(self, expiry_ms_from_now: int | None = None) -> int | None:
        """Return an absolute request-expiry timestamp for an intent request."""

        if self._request_expiry_disabled:
            return None
        duration = self._default_intent_request_expiry_ms if expiry_ms_from_now is None else expiry_ms_from_now
        return time.time_ns() // 1_000_000 + duration

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> PrivyClient:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
