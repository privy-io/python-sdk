# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.users.earn import tmmf_get_params
from ....types.wallets.tmmf_user_response import TmmfUserResponse
from ....types.wallets.tmmf_provider_param import TmmfProviderParam

__all__ = ["TmmfResource", "AsyncTmmfResource"]


class TmmfResource(SyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> TmmfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TmmfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TmmfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return TmmfResourceWithStreamingResponse(self)

    def get(
        self,
        user_id: str,
        *,
        provider: TmmfProviderParam | Omit = omit,
        wallet_id: str | Omit = omit,
        wallets_cursor: str | Omit = omit,
        wallets_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfUserResponse:
        """
        Returns a user's registration with each tMMF provider and a page of the wallets
        registered for it, with each status read live from the provider.

        Args:
          user_id: ID of the Privy user.

          provider: The fund provider.

          wallet_id: Only return the registration of this wallet.

          wallets_cursor: Cursor returned by the previous page.

          wallets_limit: Maximum number of wallet registrations to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}/earn/tmmf", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "wallet_id": wallet_id,
                        "wallets_cursor": wallets_cursor,
                        "wallets_limit": wallets_limit,
                    },
                    tmmf_get_params.TmmfGetParams,
                ),
            ),
            cast_to=TmmfUserResponse,
        )


class AsyncTmmfResource(AsyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> AsyncTmmfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTmmfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTmmfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncTmmfResourceWithStreamingResponse(self)

    async def get(
        self,
        user_id: str,
        *,
        provider: TmmfProviderParam | Omit = omit,
        wallet_id: str | Omit = omit,
        wallets_cursor: str | Omit = omit,
        wallets_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfUserResponse:
        """
        Returns a user's registration with each tMMF provider and a page of the wallets
        registered for it, with each status read live from the provider.

        Args:
          user_id: ID of the Privy user.

          provider: The fund provider.

          wallet_id: Only return the registration of this wallet.

          wallets_cursor: Cursor returned by the previous page.

          wallets_limit: Maximum number of wallet registrations to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/earn/tmmf", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "wallet_id": wallet_id,
                        "wallets_cursor": wallets_cursor,
                        "wallets_limit": wallets_limit,
                    },
                    tmmf_get_params.TmmfGetParams,
                ),
            ),
            cast_to=TmmfUserResponse,
        )


class TmmfResourceWithRawResponse:
    def __init__(self, tmmf: TmmfResource) -> None:
        self._tmmf = tmmf

        self.get = to_raw_response_wrapper(
            tmmf.get,
        )


class AsyncTmmfResourceWithRawResponse:
    def __init__(self, tmmf: AsyncTmmfResource) -> None:
        self._tmmf = tmmf

        self.get = async_to_raw_response_wrapper(
            tmmf.get,
        )


class TmmfResourceWithStreamingResponse:
    def __init__(self, tmmf: TmmfResource) -> None:
        self._tmmf = tmmf

        self.get = to_streamed_response_wrapper(
            tmmf.get,
        )


class AsyncTmmfResourceWithStreamingResponse:
    def __init__(self, tmmf: AsyncTmmfResource) -> None:
        self._tmmf = tmmf

        self.get = async_to_streamed_response_wrapper(
            tmmf.get,
        )
