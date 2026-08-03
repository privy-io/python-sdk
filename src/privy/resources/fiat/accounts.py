# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import FiatCurrency, OnrampProvider
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.fiat import account_get_params, account_create_params
from ..._base_client import make_request_options
from ...types.fiat_currency import FiatCurrency
from ...types.onramp_provider import OnrampProvider
from ...types.fiat.account_get_response import AccountGetResponse
from ...types.fiat.account_create_response import AccountCreateResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        account_owner_name: str,
        currency: FiatCurrency,
        provider: OnrampProvider,
        account: account_create_params.Account | Omit = omit,
        address: account_create_params.Address | Omit = omit,
        bank_name: str | Omit = omit,
        first_name: str | Omit = omit,
        iban: account_create_params.Iban | Omit = omit,
        last_name: str | Omit = omit,
        swift: account_create_params.Swift | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountCreateResponse:
        """
        Sets up external bank account object for the user through the configured default
        provider. Requires the user to already be KYC'ed.

        Args:
          user_id: The ID of the user to create the fiat account for

          currency: Supported fiat currencies.

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/fiat/accounts", user_id=user_id),
            body=maybe_transform(
                {
                    "account_owner_name": account_owner_name,
                    "currency": currency,
                    "provider": provider,
                    "account": account,
                    "address": address,
                    "bank_name": bank_name,
                    "first_name": first_name,
                    "iban": iban,
                    "last_name": last_name,
                    "swift": swift,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    def get(
        self,
        user_id: str,
        *,
        provider: OnrampProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetResponse:
        """
        Returns the IDs of all external fiat accounts (used for offramping) for the user

        Args:
          user_id: The ID of the user to get fiat accounts for

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}/fiat/accounts", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"provider": provider}, account_get_params.AccountGetParams),
            ),
            cast_to=AccountGetResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        account_owner_name: str,
        currency: FiatCurrency,
        provider: OnrampProvider,
        account: account_create_params.Account | Omit = omit,
        address: account_create_params.Address | Omit = omit,
        bank_name: str | Omit = omit,
        first_name: str | Omit = omit,
        iban: account_create_params.Iban | Omit = omit,
        last_name: str | Omit = omit,
        swift: account_create_params.Swift | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountCreateResponse:
        """
        Sets up external bank account object for the user through the configured default
        provider. Requires the user to already be KYC'ed.

        Args:
          user_id: The ID of the user to create the fiat account for

          currency: Supported fiat currencies.

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/fiat/accounts", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "account_owner_name": account_owner_name,
                    "currency": currency,
                    "provider": provider,
                    "account": account,
                    "address": address,
                    "bank_name": bank_name,
                    "first_name": first_name,
                    "iban": iban,
                    "last_name": last_name,
                    "swift": swift,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    async def get(
        self,
        user_id: str,
        *,
        provider: OnrampProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountGetResponse:
        """
        Returns the IDs of all external fiat accounts (used for offramping) for the user

        Args:
          user_id: The ID of the user to get fiat accounts for

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/fiat/accounts", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"provider": provider}, account_get_params.AccountGetParams),
            ),
            cast_to=AccountGetResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.get = to_raw_response_wrapper(
            accounts.get,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.get = async_to_raw_response_wrapper(
            accounts.get,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.get = to_streamed_response_wrapper(
            accounts.get,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.get = async_to_streamed_response_wrapper(
            accounts.get,
        )
