# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import app_get_gas_spend_params
from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .allowlist import (
    AllowlistResource,
    AsyncAllowlistResource,
    AllowlistResourceWithRawResponse,
    AsyncAllowlistResourceWithRawResponse,
    AllowlistResourceWithStreamingResponse,
    AsyncAllowlistResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.app_response import AppResponse
from ...types.test_accounts_response import TestAccountsResponse
from ...types.gas_spend_response_body import GasSpendResponseBody

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    """Operations related to app settings and allowlist management"""

    @cached_property
    def allowlist(self) -> AllowlistResource:
        """Operations related to app settings and allowlist management"""
        return AllowlistResource(self._client)

    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def get(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """
        Get the settings and configuration for an app.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template("/v1/apps/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    def get_gas_spend(
        self,
        *,
        end_timestamp: float,
        start_timestamp: float,
        wallet_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GasSpendResponseBody:
        """
        Get aggregated Privy gas credits charged for a set of wallets over a time range.
        Maximum 100 wallet IDs and 30-day range per request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/apps/gas_spend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_timestamp": end_timestamp,
                        "start_timestamp": start_timestamp,
                        "wallet_ids": wallet_ids,
                    },
                    app_get_gas_spend_params.AppGetGasSpendParams,
                ),
            ),
            cast_to=GasSpendResponseBody,
        )

    def get_test_credentials(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAccountsResponse:
        """
        Get the test accounts and credentials for an app.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template("/v1/apps/{app_id}/test_credentials", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAccountsResponse,
        )


class AsyncAppsResource(AsyncAPIResource):
    """Operations related to app settings and allowlist management"""

    @cached_property
    def allowlist(self) -> AsyncAllowlistResource:
        """Operations related to app settings and allowlist management"""
        return AsyncAllowlistResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def get(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """
        Get the settings and configuration for an app.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template("/v1/apps/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    async def get_gas_spend(
        self,
        *,
        end_timestamp: float,
        start_timestamp: float,
        wallet_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GasSpendResponseBody:
        """
        Get aggregated Privy gas credits charged for a set of wallets over a time range.
        Maximum 100 wallet IDs and 30-day range per request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/apps/gas_spend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_timestamp": end_timestamp,
                        "start_timestamp": start_timestamp,
                        "wallet_ids": wallet_ids,
                    },
                    app_get_gas_spend_params.AppGetGasSpendParams,
                ),
            ),
            cast_to=GasSpendResponseBody,
        )

    async def get_test_credentials(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAccountsResponse:
        """
        Get the test accounts and credentials for an app.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template("/v1/apps/{app_id}/test_credentials", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAccountsResponse,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.get = to_raw_response_wrapper(
            apps.get,
        )
        self.get_gas_spend = to_raw_response_wrapper(
            apps.get_gas_spend,
        )
        self.get_test_credentials = to_raw_response_wrapper(
            apps.get_test_credentials,
        )

    @cached_property
    def allowlist(self) -> AllowlistResourceWithRawResponse:
        """Operations related to app settings and allowlist management"""
        return AllowlistResourceWithRawResponse(self._apps.allowlist)


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.get = async_to_raw_response_wrapper(
            apps.get,
        )
        self.get_gas_spend = async_to_raw_response_wrapper(
            apps.get_gas_spend,
        )
        self.get_test_credentials = async_to_raw_response_wrapper(
            apps.get_test_credentials,
        )

    @cached_property
    def allowlist(self) -> AsyncAllowlistResourceWithRawResponse:
        """Operations related to app settings and allowlist management"""
        return AsyncAllowlistResourceWithRawResponse(self._apps.allowlist)


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.get = to_streamed_response_wrapper(
            apps.get,
        )
        self.get_gas_spend = to_streamed_response_wrapper(
            apps.get_gas_spend,
        )
        self.get_test_credentials = to_streamed_response_wrapper(
            apps.get_test_credentials,
        )

    @cached_property
    def allowlist(self) -> AllowlistResourceWithStreamingResponse:
        """Operations related to app settings and allowlist management"""
        return AllowlistResourceWithStreamingResponse(self._apps.allowlist)


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )
        self.get_gas_spend = async_to_streamed_response_wrapper(
            apps.get_gas_spend,
        )
        self.get_test_credentials = async_to_streamed_response_wrapper(
            apps.get_test_credentials,
        )

    @cached_property
    def allowlist(self) -> AsyncAllowlistResourceWithStreamingResponse:
        """Operations related to app settings and allowlist management"""
        return AsyncAllowlistResourceWithStreamingResponse(self._apps.allowlist)
