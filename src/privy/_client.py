# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .lib.users import (
    UsersResource as PrivyUsersResource,
    AsyncUsersResource as PrivyAsyncUsersResource,
)
from .resources import users, policies, key_quorums, transactions
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PrivyAPIError, APIStatusError
from .lib.wallets import (
    WalletsResource as PrivyWalletsResource,
    AsyncWalletsResource as PrivyAsyncWalletsResource,
)
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.fiat import fiat
from .lib.http_client import PrivyHTTPClient
from .resources.wallets import wallets

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
    "staging": "https://auth.staging.privy.io",
}


class PrivyAPI(SyncAPIClient):
    wallets: PrivyWalletsResource
    users: PrivyUsersResource
    policies: policies.PoliciesResource
    transactions: transactions.TransactionsResource
    key_quorums: key_quorums.KeyQuorumsResource
    fiat: fiat.FiatResource
    with_raw_response: PrivyAPIWithRawResponse
    with_streaming_response: PrivyAPIWithStreamedResponse

    # client options
    app_id: str
    app_secret: str

    _environment: Literal["production", "staging"] | NotGiven

    def __init__(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        environment: Literal["production", "staging"] | NotGiven = NOT_GIVEN,
        authorization_key: str | None = None,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
            self._base_url_overridden = True
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PRIVY_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
            self._base_url_overridden = False
        elif base_url_env is not None:
            base_url = base_url_env
            self._base_url_overridden = True
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
            self._base_url_overridden = False

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client
            or PrivyHTTPClient(
                app_id=app_id or "",
                timeout=timeout if isinstance(timeout, (int, float)) else None,
                authorization_key=authorization_key,
            ),
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.wallets = PrivyWalletsResource(self)
        self.users = PrivyUsersResource(self)
        self.policies = policies.PoliciesResource(self)
        self.transactions = transactions.TransactionsResource(self)
        self.key_quorums = key_quorums.KeyQuorumsResource(self)
        self.fiat = fiat.FiatResource(self)
        self.with_raw_response = PrivyAPIWithRawResponse(self)
        self.with_streaming_response = PrivyAPIWithStreamedResponse(self)

    def update_authorization_key(self, authorization_key: str) -> None:
        if isinstance(self._client, PrivyHTTPClient):
            self._client._authorization_key = authorization_key.replace("wallet-auth:", "")

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
        authorization_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
        client = self.__class__(
            app_id=app_id or self.app_id,
            app_secret=app_secret or self.app_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            authorization_key=authorization_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

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
    wallets: PrivyAsyncWalletsResource
    users: PrivyAsyncUsersResource
    policies: policies.AsyncPoliciesResource
    transactions: transactions.AsyncTransactionsResource
    key_quorums: key_quorums.AsyncKeyQuorumsResource
    fiat: fiat.AsyncFiatResource
    with_raw_response: AsyncPrivyAPIWithRawResponse
    with_streaming_response: AsyncPrivyAPIWithStreamedResponse

    # client options
    app_id: str
    app_secret: str

    _environment: Literal["production", "staging"] | NotGiven

    def __init__(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        environment: Literal["production", "staging"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
            self._base_url_overridden = True
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PRIVY_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
            self._base_url_overridden = False
        elif base_url_env is not None:
            base_url = base_url_env
            self._base_url_overridden = True
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
            self._base_url_overridden = False

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

        self.wallets = PrivyAsyncWalletsResource(self)
        self.users = PrivyAsyncUsersResource(self)
        self.policies = policies.AsyncPoliciesResource(self)
        self.transactions = transactions.AsyncTransactionsResource(self)
        self.key_quorums = key_quorums.AsyncKeyQuorumsResource(self)
        self.fiat = fiat.AsyncFiatResource(self)
        self.with_raw_response = AsyncPrivyAPIWithRawResponse(self)
        self.with_streaming_response = AsyncPrivyAPIWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
        client = self.__class__(
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
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

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
    def __init__(self, client: PrivyAPI) -> None:
        self.wallets = wallets.WalletsResourceWithRawResponse(client.wallets)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.policies = policies.PoliciesResourceWithRawResponse(client.policies)
        self.transactions = transactions.TransactionsResourceWithRawResponse(client.transactions)
        self.key_quorums = key_quorums.KeyQuorumsResourceWithRawResponse(client.key_quorums)
        self.fiat = fiat.FiatResourceWithRawResponse(client.fiat)


class AsyncPrivyAPIWithRawResponse:
    def __init__(self, client: AsyncPrivyAPI) -> None:
        self.wallets = wallets.AsyncWalletsResourceWithRawResponse(client.wallets)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.policies = policies.AsyncPoliciesResourceWithRawResponse(client.policies)
        self.transactions = transactions.AsyncTransactionsResourceWithRawResponse(client.transactions)
        self.key_quorums = key_quorums.AsyncKeyQuorumsResourceWithRawResponse(client.key_quorums)
        self.fiat = fiat.AsyncFiatResourceWithRawResponse(client.fiat)


class PrivyAPIWithStreamedResponse:
    def __init__(self, client: PrivyAPI) -> None:
        self.wallets = wallets.WalletsResourceWithStreamingResponse(client.wallets)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.policies = policies.PoliciesResourceWithStreamingResponse(client.policies)
        self.transactions = transactions.TransactionsResourceWithStreamingResponse(client.transactions)
        self.key_quorums = key_quorums.KeyQuorumsResourceWithStreamingResponse(client.key_quorums)
        self.fiat = fiat.FiatResourceWithStreamingResponse(client.fiat)


class AsyncPrivyAPIWithStreamedResponse:
    def __init__(self, client: AsyncPrivyAPI) -> None:
        self.wallets = wallets.AsyncWalletsResourceWithStreamingResponse(client.wallets)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.policies = policies.AsyncPoliciesResourceWithStreamingResponse(client.policies)
        self.transactions = transactions.AsyncTransactionsResourceWithStreamingResponse(client.transactions)
        self.key_quorums = key_quorums.AsyncKeyQuorumsResourceWithStreamingResponse(client.key_quorums)
        self.fiat = fiat.AsyncFiatResourceWithStreamingResponse(client.fiat)


Client = PrivyAPI

AsyncClient = AsyncPrivyAPI
