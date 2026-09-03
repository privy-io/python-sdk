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
from ...types.fiat import offramp_create_params
from ..._base_client import make_request_options
from ...types.fiat.offramp_create_response import OfframpCreateResponse

__all__ = ["OfframpResource", "AsyncOfframpResource"]


class OfframpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OfframpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return OfframpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OfframpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return OfframpResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        amount: str,
        destination: offramp_create_params.Destination,
        provider: Literal["bridge", "bridge-sandbox"],
        source: offramp_create_params.Source,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OfframpCreateResponse:
        """
        Triggers the offramp flow and gets the on-chain address to send funds to

        Args:
          user_id: The ID of the user initiating the offramp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/users/{user_id}/fiat/offramp",
            body=maybe_transform(
                {
                    "amount": amount,
                    "destination": destination,
                    "provider": provider,
                    "source": source,
                },
                offramp_create_params.OfframpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfframpCreateResponse,
        )


class AsyncOfframpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOfframpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOfframpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOfframpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncOfframpResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        amount: str,
        destination: offramp_create_params.Destination,
        provider: Literal["bridge", "bridge-sandbox"],
        source: offramp_create_params.Source,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OfframpCreateResponse:
        """
        Triggers the offramp flow and gets the on-chain address to send funds to

        Args:
          user_id: The ID of the user initiating the offramp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/users/{user_id}/fiat/offramp",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "destination": destination,
                    "provider": provider,
                    "source": source,
                },
                offramp_create_params.OfframpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfframpCreateResponse,
        )


class OfframpResourceWithRawResponse:
    def __init__(self, offramp: OfframpResource) -> None:
        self._offramp = offramp

        self.create = to_raw_response_wrapper(
            offramp.create,
        )


class AsyncOfframpResourceWithRawResponse:
    def __init__(self, offramp: AsyncOfframpResource) -> None:
        self._offramp = offramp

        self.create = async_to_raw_response_wrapper(
            offramp.create,
        )


class OfframpResourceWithStreamingResponse:
    def __init__(self, offramp: OfframpResource) -> None:
        self._offramp = offramp

        self.create = to_streamed_response_wrapper(
            offramp.create,
        )


class AsyncOfframpResourceWithStreamingResponse:
    def __init__(self, offramp: AsyncOfframpResource) -> None:
        self._offramp = offramp

        self.create = async_to_streamed_response_wrapper(
            offramp.create,
        )
