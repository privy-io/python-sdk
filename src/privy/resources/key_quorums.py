# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import key_quorum_create_params, key_quorum_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.key_quorum import KeyQuorum

__all__ = ["KeyQuorumsResource", "AsyncKeyQuorumsResource"]


class KeyQuorumsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeyQuorumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return KeyQuorumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeyQuorumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return KeyQuorumsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        public_keys: List[str],
        authorization_threshold: float | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Create a new key quorum.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/key_quorums",
            body=maybe_transform(
                {
                    "public_keys": public_keys,
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                },
                key_quorum_create_params.KeyQuorumCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    def update(
        self,
        key_quorum_id: str,
        *,
        public_keys: List[str],
        authorization_threshold: float | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Update a key quorum by key quorum ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return self._patch(
            f"/v1/key_quorums/{key_quorum_id}",
            body=maybe_transform(
                {
                    "public_keys": public_keys,
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                },
                key_quorum_update_params.KeyQuorumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    def delete(
        self,
        key_quorum_id: str,
        *,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Delete a key quorum by key quorum ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/v1/key_quorums/{key_quorum_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    def get(
        self,
        key_quorum_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Get a key quorum by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        return self._get(
            f"/v1/key_quorums/{key_quorum_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )


class AsyncKeyQuorumsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeyQuorumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKeyQuorumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeyQuorumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncKeyQuorumsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        public_keys: List[str],
        authorization_threshold: float | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Create a new key quorum.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/key_quorums",
            body=await async_maybe_transform(
                {
                    "public_keys": public_keys,
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                },
                key_quorum_create_params.KeyQuorumCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    async def update(
        self,
        key_quorum_id: str,
        *,
        public_keys: List[str],
        authorization_threshold: float | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Update a key quorum by key quorum ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return await self._patch(
            f"/v1/key_quorums/{key_quorum_id}",
            body=await async_maybe_transform(
                {
                    "public_keys": public_keys,
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                },
                key_quorum_update_params.KeyQuorumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    async def delete(
        self,
        key_quorum_id: str,
        *,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Delete a key quorum by key quorum ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/v1/key_quorums/{key_quorum_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    async def get(
        self,
        key_quorum_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyQuorum:
        """
        Get a key quorum by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        return await self._get(
            f"/v1/key_quorums/{key_quorum_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )


class KeyQuorumsResourceWithRawResponse:
    def __init__(self, key_quorums: KeyQuorumsResource) -> None:
        self._key_quorums = key_quorums

        self.create = to_raw_response_wrapper(
            key_quorums.create,
        )
        self.update = to_raw_response_wrapper(
            key_quorums.update,
        )
        self.delete = to_raw_response_wrapper(
            key_quorums.delete,
        )
        self.get = to_raw_response_wrapper(
            key_quorums.get,
        )


class AsyncKeyQuorumsResourceWithRawResponse:
    def __init__(self, key_quorums: AsyncKeyQuorumsResource) -> None:
        self._key_quorums = key_quorums

        self.create = async_to_raw_response_wrapper(
            key_quorums.create,
        )
        self.update = async_to_raw_response_wrapper(
            key_quorums.update,
        )
        self.delete = async_to_raw_response_wrapper(
            key_quorums.delete,
        )
        self.get = async_to_raw_response_wrapper(
            key_quorums.get,
        )


class KeyQuorumsResourceWithStreamingResponse:
    def __init__(self, key_quorums: KeyQuorumsResource) -> None:
        self._key_quorums = key_quorums

        self.create = to_streamed_response_wrapper(
            key_quorums.create,
        )
        self.update = to_streamed_response_wrapper(
            key_quorums.update,
        )
        self.delete = to_streamed_response_wrapper(
            key_quorums.delete,
        )
        self.get = to_streamed_response_wrapper(
            key_quorums.get,
        )


class AsyncKeyQuorumsResourceWithStreamingResponse:
    def __init__(self, key_quorums: AsyncKeyQuorumsResource) -> None:
        self._key_quorums = key_quorums

        self.create = async_to_streamed_response_wrapper(
            key_quorums.create,
        )
        self.update = async_to_streamed_response_wrapper(
            key_quorums.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            key_quorums.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            key_quorums.get,
        )
