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
from ...types.fiat import onramp_create_params
from ..._base_client import make_request_options
from ...types.fiat.onramp_create_response import OnrampCreateResponse

__all__ = ["OnrampResource", "AsyncOnrampResource"]


class OnrampResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnrampResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnrampResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnrampResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return OnrampResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        amount: str,
        destination: onramp_create_params.Destination,
        provider: Literal["bridge", "bridge-sandbox"],
        source: onramp_create_params.Source,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnrampCreateResponse:
        """
        Triggers an onramp to the specified recipient blockchain address, returns the
        bank deposit instructions

        Args:
          user_id: The ID of the user initiating the onramp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/users/{user_id}/fiat/onramp",
            body=maybe_transform(
                {
                    "amount": amount,
                    "destination": destination,
                    "provider": provider,
                    "source": source,
                },
                onramp_create_params.OnrampCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnrampCreateResponse,
        )


class AsyncOnrampResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnrampResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnrampResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnrampResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncOnrampResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        amount: str,
        destination: onramp_create_params.Destination,
        provider: Literal["bridge", "bridge-sandbox"],
        source: onramp_create_params.Source,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnrampCreateResponse:
        """
        Triggers an onramp to the specified recipient blockchain address, returns the
        bank deposit instructions

        Args:
          user_id: The ID of the user initiating the onramp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/users/{user_id}/fiat/onramp",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "destination": destination,
                    "provider": provider,
                    "source": source,
                },
                onramp_create_params.OnrampCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnrampCreateResponse,
        )


class OnrampResourceWithRawResponse:
    def __init__(self, onramp: OnrampResource) -> None:
        self._onramp = onramp

        self.create = to_raw_response_wrapper(
            onramp.create,
        )


class AsyncOnrampResourceWithRawResponse:
    def __init__(self, onramp: AsyncOnrampResource) -> None:
        self._onramp = onramp

        self.create = async_to_raw_response_wrapper(
            onramp.create,
        )


class OnrampResourceWithStreamingResponse:
    def __init__(self, onramp: OnrampResource) -> None:
        self._onramp = onramp

        self.create = to_streamed_response_wrapper(
            onramp.create,
        )


class AsyncOnrampResourceWithStreamingResponse:
    def __init__(self, onramp: AsyncOnrampResource) -> None:
        self._onramp = onramp

        self.create = async_to_streamed_response_wrapper(
            onramp.create,
        )
