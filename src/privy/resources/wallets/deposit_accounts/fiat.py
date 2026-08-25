# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....types import Environment, OrchestrationProvider
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.environment import Environment
from ....types.orchestration_provider import OrchestrationProvider
from ....types.wallets.deposit_accounts import fiat_list_params, fiat_create_params
from ....types.fiat_deposit_account_response import FiatDepositAccountResponse
from ....types.list_fiat_deposit_accounts_response import ListFiatDepositAccountsResponse
from ....types.fiat_deposit_account_destination_param import FiatDepositAccountDestinationParam
from ....types.create_fiat_deposit_account_source_param import CreateFiatDepositAccountSourceParam

__all__ = ["FiatResource", "AsyncFiatResource"]


class FiatResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> FiatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FiatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return FiatResourceWithStreamingResponse(self)

    def create(
        self,
        wallet_id: str,
        *,
        destination: FiatDepositAccountDestinationParam,
        provider: Literal["bridge"],
        source: CreateFiatDepositAccountSourceParam,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatDepositAccountResponse:
        """Creates a Bridge Virtual Account linked to a wallet.

        Fiat sent to the returned
        deposit instructions will be converted to the specified crypto asset and
        delivered to the wallet.

        Args:
          wallet_id: The ID of the wallet.

          destination: The destination crypto asset and chain for a fiat deposit account.

          provider: Discriminator: the fiat deposit account is orchestrated via Bridge.

          source: The source fiat currency for a fiat deposit account.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._post(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/fiat", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "destination": destination,
                    "provider": provider,
                    "source": source,
                    "environment": environment,
                },
                fiat_create_params.FiatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatDepositAccountResponse,
        )

    def list(
        self,
        wallet_id: str,
        *,
        provider: OrchestrationProvider,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFiatDepositAccountsResponse:
        """
        Returns a list of fiat deposit accounts linked to a wallet.

        Args:
          wallet_id: The ID of the wallet.

          provider: Supported fiat orchestration providers.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/fiat", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "environment": environment,
                    },
                    fiat_list_params.FiatListParams,
                ),
            ),
            cast_to=ListFiatDepositAccountsResponse,
        )

    def get(
        self,
        deposit_account_id: str,
        *,
        wallet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatDepositAccountResponse:
        """
        Returns a single fiat deposit account linked to a wallet.

        Args:
          wallet_id: The ID of the wallet.

          deposit_account_id: The ID of the fiat deposit account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        if not deposit_account_id:
            raise ValueError(f"Expected a non-empty value for `deposit_account_id` but received {deposit_account_id!r}")
        return self._get(
            path_template(
                "/v1/wallets/{wallet_id}/deposit_accounts/fiat/{deposit_account_id}",
                wallet_id=wallet_id,
                deposit_account_id=deposit_account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatDepositAccountResponse,
        )


class AsyncFiatResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AsyncFiatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFiatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncFiatResourceWithStreamingResponse(self)

    async def create(
        self,
        wallet_id: str,
        *,
        destination: FiatDepositAccountDestinationParam,
        provider: Literal["bridge"],
        source: CreateFiatDepositAccountSourceParam,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatDepositAccountResponse:
        """Creates a Bridge Virtual Account linked to a wallet.

        Fiat sent to the returned
        deposit instructions will be converted to the specified crypto asset and
        delivered to the wallet.

        Args:
          wallet_id: The ID of the wallet.

          destination: The destination crypto asset and chain for a fiat deposit account.

          provider: Discriminator: the fiat deposit account is orchestrated via Bridge.

          source: The source fiat currency for a fiat deposit account.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/fiat", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "provider": provider,
                    "source": source,
                    "environment": environment,
                },
                fiat_create_params.FiatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatDepositAccountResponse,
        )

    async def list(
        self,
        wallet_id: str,
        *,
        provider: OrchestrationProvider,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFiatDepositAccountsResponse:
        """
        Returns a list of fiat deposit accounts linked to a wallet.

        Args:
          wallet_id: The ID of the wallet.

          provider: Supported fiat orchestration providers.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/fiat", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "environment": environment,
                    },
                    fiat_list_params.FiatListParams,
                ),
            ),
            cast_to=ListFiatDepositAccountsResponse,
        )

    async def get(
        self,
        deposit_account_id: str,
        *,
        wallet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatDepositAccountResponse:
        """
        Returns a single fiat deposit account linked to a wallet.

        Args:
          wallet_id: The ID of the wallet.

          deposit_account_id: The ID of the fiat deposit account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        if not deposit_account_id:
            raise ValueError(f"Expected a non-empty value for `deposit_account_id` but received {deposit_account_id!r}")
        return await self._get(
            path_template(
                "/v1/wallets/{wallet_id}/deposit_accounts/fiat/{deposit_account_id}",
                wallet_id=wallet_id,
                deposit_account_id=deposit_account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatDepositAccountResponse,
        )


class FiatResourceWithRawResponse:
    def __init__(self, fiat: FiatResource) -> None:
        self._fiat = fiat

        self.create = to_raw_response_wrapper(
            fiat.create,
        )
        self.list = to_raw_response_wrapper(
            fiat.list,
        )
        self.get = to_raw_response_wrapper(
            fiat.get,
        )


class AsyncFiatResourceWithRawResponse:
    def __init__(self, fiat: AsyncFiatResource) -> None:
        self._fiat = fiat

        self.create = async_to_raw_response_wrapper(
            fiat.create,
        )
        self.list = async_to_raw_response_wrapper(
            fiat.list,
        )
        self.get = async_to_raw_response_wrapper(
            fiat.get,
        )


class FiatResourceWithStreamingResponse:
    def __init__(self, fiat: FiatResource) -> None:
        self._fiat = fiat

        self.create = to_streamed_response_wrapper(
            fiat.create,
        )
        self.list = to_streamed_response_wrapper(
            fiat.list,
        )
        self.get = to_streamed_response_wrapper(
            fiat.get,
        )


class AsyncFiatResourceWithStreamingResponse:
    def __init__(self, fiat: AsyncFiatResource) -> None:
        self._fiat = fiat

        self.create = async_to_streamed_response_wrapper(
            fiat.create,
        )
        self.list = async_to_streamed_response_wrapper(
            fiat.list,
        )
        self.get = async_to_streamed_response_wrapper(
            fiat.get,
        )
