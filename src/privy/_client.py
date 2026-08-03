# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PrivyAPIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import apps, fiat, users, intents, wallets, policies, key_quorums, transactions
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.intents import IntentsResource, AsyncIntentsResource
    from .resources.policies import PoliciesResource, AsyncPoliciesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.apps.apps import AppsResource, AsyncAppsResource
    from .resources.fiat.fiat import FiatResource, AsyncFiatResource
    from .resources.key_quorums import KeyQuorumsResource, AsyncKeyQuorumsResource
    from .resources.transactions import TransactionsResource, AsyncTransactionsResource
    from .resources.wallets.wallets import WalletsResource, AsyncWalletsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "PrivyAPI",
    "AsyncPrivyAPI",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.privy.io",
    "staging": "https://api.staging.privy.io",
}


class PrivyAPI(SyncAPIClient):
    # client options
    app_id: str
    app_secret: str

    _environment: Literal["production", "staging"] | NotGiven

    def __init__(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        environment: Literal["production", "staging"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous PrivyAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `app_id` from `PRIVY_APP_ID`
        - `app_secret` from `PRIVY_APP_SECRET`
        """
        if app_id is None:
            app_id = os.environ.get("PRIVY_APP_ID")
        if app_id is None:
            raise PrivyAPIError(
                "The app_id client option must be set either by passing app_id to the client or by setting the PRIVY_APP_ID environment variable"
            )
        self.app_id = app_id

        if app_secret is None:
            app_secret = os.environ.get("PRIVY_APP_SECRET")
        if app_secret is None:
            raise PrivyAPIError(
                "The app_secret client option must be set either by passing app_secret to the client or by setting the PRIVY_APP_SECRET environment variable"
            )
        self.app_secret = app_secret

        self._environment = environment

        base_url_env = os.environ.get("PRIVY_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PRIVY_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("PRIVY_API_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def wallets(self) -> WalletsResource:
        from .resources.wallets import WalletsResource

        return WalletsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """Operations related to users"""
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def policies(self) -> PoliciesResource:
        """Operations related to policies"""
        from .resources.policies import PoliciesResource

        return PoliciesResource(self)

    @cached_property
    def transactions(self) -> TransactionsResource:
        """Operations related to transactions"""
        from .resources.transactions import TransactionsResource

        return TransactionsResource(self)

    @cached_property
    def key_quorums(self) -> KeyQuorumsResource:
        """Operations related to key quorums"""
        from .resources.key_quorums import KeyQuorumsResource

        return KeyQuorumsResource(self)

    @cached_property
    def intents(self) -> IntentsResource:
        """Operations related to authorization intents for wallet actions"""
        from .resources.intents import IntentsResource

        return IntentsResource(self)

    @cached_property
    def apps(self) -> AppsResource:
        """Operations related to app settings and allowlist management"""
        from .resources.apps import AppsResource

        return AppsResource(self)

    @cached_property
    def fiat(self) -> FiatResource:
        """Operations related to fiat onramping and offramping"""
        from .resources.fiat import FiatResource

        return FiatResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> PrivyAPIWithRawResponse:
        return PrivyAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivyAPIWithStreamedResponse:
        return PrivyAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.app_id}:{self.app_secret}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "privy-app-id": self.app_id,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        environment: Literal["production", "staging"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            app_id=app_id or self.app_id,
            app_secret=app_secret or self.app_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPrivyAPI(AsyncAPIClient):
    # client options
    app_id: str
    app_secret: str

    _environment: Literal["production", "staging"] | NotGiven

    def __init__(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        environment: Literal["production", "staging"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPrivyAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `app_id` from `PRIVY_APP_ID`
        - `app_secret` from `PRIVY_APP_SECRET`
        """
        if app_id is None:
            app_id = os.environ.get("PRIVY_APP_ID")
        if app_id is None:
            raise PrivyAPIError(
                "The app_id client option must be set either by passing app_id to the client or by setting the PRIVY_APP_ID environment variable"
            )
        self.app_id = app_id

        if app_secret is None:
            app_secret = os.environ.get("PRIVY_APP_SECRET")
        if app_secret is None:
            raise PrivyAPIError(
                "The app_secret client option must be set either by passing app_secret to the client or by setting the PRIVY_APP_SECRET environment variable"
            )
        self.app_secret = app_secret

        self._environment = environment

        base_url_env = os.environ.get("PRIVY_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PRIVY_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("PRIVY_API_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def wallets(self) -> AsyncWalletsResource:
        from .resources.wallets import AsyncWalletsResource

        return AsyncWalletsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Operations related to users"""
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        """Operations related to policies"""
        from .resources.policies import AsyncPoliciesResource

        return AsyncPoliciesResource(self)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        """Operations related to transactions"""
        from .resources.transactions import AsyncTransactionsResource

        return AsyncTransactionsResource(self)

    @cached_property
    def key_quorums(self) -> AsyncKeyQuorumsResource:
        """Operations related to key quorums"""
        from .resources.key_quorums import AsyncKeyQuorumsResource

        return AsyncKeyQuorumsResource(self)

    @cached_property
    def intents(self) -> AsyncIntentsResource:
        """Operations related to authorization intents for wallet actions"""
        from .resources.intents import AsyncIntentsResource

        return AsyncIntentsResource(self)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        """Operations related to app settings and allowlist management"""
        from .resources.apps import AsyncAppsResource

        return AsyncAppsResource(self)

    @cached_property
    def fiat(self) -> AsyncFiatResource:
        """Operations related to fiat onramping and offramping"""
        from .resources.fiat import AsyncFiatResource

        return AsyncFiatResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPrivyAPIWithRawResponse:
        return AsyncPrivyAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivyAPIWithStreamedResponse:
        return AsyncPrivyAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.app_id}:{self.app_secret}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "privy-app-id": self.app_id,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        environment: Literal["production", "staging"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            app_id=app_id or self.app_id,
            app_secret=app_secret or self.app_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PrivyAPIWithRawResponse:
    _client: PrivyAPI

    def __init__(self, client: PrivyAPI) -> None:
        self._client = client

    @cached_property
    def wallets(self) -> wallets.WalletsResourceWithRawResponse:
        from .resources.wallets import WalletsResourceWithRawResponse

        return WalletsResourceWithRawResponse(self._client.wallets)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """Operations related to users"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def policies(self) -> policies.PoliciesResourceWithRawResponse:
        """Operations related to policies"""
        from .resources.policies import PoliciesResourceWithRawResponse

        return PoliciesResourceWithRawResponse(self._client.policies)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithRawResponse:
        """Operations related to transactions"""
        from .resources.transactions import TransactionsResourceWithRawResponse

        return TransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def key_quorums(self) -> key_quorums.KeyQuorumsResourceWithRawResponse:
        """Operations related to key quorums"""
        from .resources.key_quorums import KeyQuorumsResourceWithRawResponse

        return KeyQuorumsResourceWithRawResponse(self._client.key_quorums)

    @cached_property
    def intents(self) -> intents.IntentsResourceWithRawResponse:
        """Operations related to authorization intents for wallet actions"""
        from .resources.intents import IntentsResourceWithRawResponse

        return IntentsResourceWithRawResponse(self._client.intents)

    @cached_property
    def apps(self) -> apps.AppsResourceWithRawResponse:
        """Operations related to app settings and allowlist management"""
        from .resources.apps import AppsResourceWithRawResponse

        return AppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def fiat(self) -> fiat.FiatResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        from .resources.fiat import FiatResourceWithRawResponse

        return FiatResourceWithRawResponse(self._client.fiat)


class AsyncPrivyAPIWithRawResponse:
    _client: AsyncPrivyAPI

    def __init__(self, client: AsyncPrivyAPI) -> None:
        self._client = client

    @cached_property
    def wallets(self) -> wallets.AsyncWalletsResourceWithRawResponse:
        from .resources.wallets import AsyncWalletsResourceWithRawResponse

        return AsyncWalletsResourceWithRawResponse(self._client.wallets)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """Operations related to users"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def policies(self) -> policies.AsyncPoliciesResourceWithRawResponse:
        """Operations related to policies"""
        from .resources.policies import AsyncPoliciesResourceWithRawResponse

        return AsyncPoliciesResourceWithRawResponse(self._client.policies)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithRawResponse:
        """Operations related to transactions"""
        from .resources.transactions import AsyncTransactionsResourceWithRawResponse

        return AsyncTransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def key_quorums(self) -> key_quorums.AsyncKeyQuorumsResourceWithRawResponse:
        """Operations related to key quorums"""
        from .resources.key_quorums import AsyncKeyQuorumsResourceWithRawResponse

        return AsyncKeyQuorumsResourceWithRawResponse(self._client.key_quorums)

    @cached_property
    def intents(self) -> intents.AsyncIntentsResourceWithRawResponse:
        """Operations related to authorization intents for wallet actions"""
        from .resources.intents import AsyncIntentsResourceWithRawResponse

        return AsyncIntentsResourceWithRawResponse(self._client.intents)

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithRawResponse:
        """Operations related to app settings and allowlist management"""
        from .resources.apps import AsyncAppsResourceWithRawResponse

        return AsyncAppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def fiat(self) -> fiat.AsyncFiatResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        from .resources.fiat import AsyncFiatResourceWithRawResponse

        return AsyncFiatResourceWithRawResponse(self._client.fiat)


class PrivyAPIWithStreamedResponse:
    _client: PrivyAPI

    def __init__(self, client: PrivyAPI) -> None:
        self._client = client

    @cached_property
    def wallets(self) -> wallets.WalletsResourceWithStreamingResponse:
        from .resources.wallets import WalletsResourceWithStreamingResponse

        return WalletsResourceWithStreamingResponse(self._client.wallets)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """Operations related to users"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def policies(self) -> policies.PoliciesResourceWithStreamingResponse:
        """Operations related to policies"""
        from .resources.policies import PoliciesResourceWithStreamingResponse

        return PoliciesResourceWithStreamingResponse(self._client.policies)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithStreamingResponse:
        """Operations related to transactions"""
        from .resources.transactions import TransactionsResourceWithStreamingResponse

        return TransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def key_quorums(self) -> key_quorums.KeyQuorumsResourceWithStreamingResponse:
        """Operations related to key quorums"""
        from .resources.key_quorums import KeyQuorumsResourceWithStreamingResponse

        return KeyQuorumsResourceWithStreamingResponse(self._client.key_quorums)

    @cached_property
    def intents(self) -> intents.IntentsResourceWithStreamingResponse:
        """Operations related to authorization intents for wallet actions"""
        from .resources.intents import IntentsResourceWithStreamingResponse

        return IntentsResourceWithStreamingResponse(self._client.intents)

    @cached_property
    def apps(self) -> apps.AppsResourceWithStreamingResponse:
        """Operations related to app settings and allowlist management"""
        from .resources.apps import AppsResourceWithStreamingResponse

        return AppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def fiat(self) -> fiat.FiatResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        from .resources.fiat import FiatResourceWithStreamingResponse

        return FiatResourceWithStreamingResponse(self._client.fiat)


class AsyncPrivyAPIWithStreamedResponse:
    _client: AsyncPrivyAPI

    def __init__(self, client: AsyncPrivyAPI) -> None:
        self._client = client

    @cached_property
    def wallets(self) -> wallets.AsyncWalletsResourceWithStreamingResponse:
        from .resources.wallets import AsyncWalletsResourceWithStreamingResponse

        return AsyncWalletsResourceWithStreamingResponse(self._client.wallets)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """Operations related to users"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def policies(self) -> policies.AsyncPoliciesResourceWithStreamingResponse:
        """Operations related to policies"""
        from .resources.policies import AsyncPoliciesResourceWithStreamingResponse

        return AsyncPoliciesResourceWithStreamingResponse(self._client.policies)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithStreamingResponse:
        """Operations related to transactions"""
        from .resources.transactions import AsyncTransactionsResourceWithStreamingResponse

        return AsyncTransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def key_quorums(self) -> key_quorums.AsyncKeyQuorumsResourceWithStreamingResponse:
        """Operations related to key quorums"""
        from .resources.key_quorums import AsyncKeyQuorumsResourceWithStreamingResponse

        return AsyncKeyQuorumsResourceWithStreamingResponse(self._client.key_quorums)

    @cached_property
    def intents(self) -> intents.AsyncIntentsResourceWithStreamingResponse:
        """Operations related to authorization intents for wallet actions"""
        from .resources.intents import AsyncIntentsResourceWithStreamingResponse

        return AsyncIntentsResourceWithStreamingResponse(self._client.intents)

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithStreamingResponse:
        """Operations related to app settings and allowlist management"""
        from .resources.apps import AsyncAppsResourceWithStreamingResponse

        return AsyncAppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def fiat(self) -> fiat.AsyncFiatResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        from .resources.fiat import AsyncFiatResourceWithStreamingResponse

        return AsyncFiatResourceWithStreamingResponse(self._client.fiat)


Client = PrivyAPI

AsyncClient = AsyncPrivyAPI
