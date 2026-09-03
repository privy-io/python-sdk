# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.fiat.account_get_response import AccountGetResponse
from ...types.fiat.account_create_response import AccountCreateResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
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
        currency: Literal["usd", "eur"],
        provider: Literal["bridge", "bridge-sandbox"],
        account: account_create_params.Account | NotGiven = NOT_GIVEN,
        address: account_create_params.Address | NotGiven = NOT_GIVEN,
        bank_name: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        iban: account_create_params.Iban | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        swift: account_create_params.Swift | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateResponse:
        """
        Sets up external bank account object for the user through the configured default
        provider. Requires the user to already be KYC'ed.

        Args:
          user_id: The ID of the user to create the fiat account for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/users/{user_id}/fiat/accounts",
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
        provider: Literal["bridge", "bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountGetResponse:
        """
        Returns the IDs of all external fiat accounts (used for offramping) for the user

        Args:
          user_id: The ID of the user to get fiat accounts for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v1/users/{user_id}/fiat/accounts",
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
        currency: Literal["usd", "eur"],
        provider: Literal["bridge", "bridge-sandbox"],
        account: account_create_params.Account | NotGiven = NOT_GIVEN,
        address: account_create_params.Address | NotGiven = NOT_GIVEN,
        bank_name: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        iban: account_create_params.Iban | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        swift: account_create_params.Swift | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateResponse:
        """
        Sets up external bank account object for the user through the configured default
        provider. Requires the user to already be KYC'ed.

        Args:
          user_id: The ID of the user to create the fiat account for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/users/{user_id}/fiat/accounts",
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
        provider: Literal["bridge", "bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountGetResponse:
        """
        Returns the IDs of all external fiat accounts (used for offramping) for the user

        Args:
          user_id: The ID of the user to get fiat accounts for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v1/users/{user_id}/fiat/accounts",
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
