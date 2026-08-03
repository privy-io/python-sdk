# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import KeyQuorumID, key_quorum_create_params, key_quorum_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.key_quorum_id import KeyQuorumID
from ..types.success_response import SuccessResponse

__all__ = ["KeyQuorumsResource", "AsyncKeyQuorumsResource"]


class KeyQuorumsResource(SyncAPIResource):
    """Operations related to key quorums"""

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
        authorization_threshold: float | Omit = omit,
        display_name: str | Omit = omit,
        key_quorum_ids: SequenceNotStr[str] | Omit = omit,
        public_keys: SequenceNotStr[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorum:
        """
        Create a new key quorum.

        Args:
          authorization_threshold: The number of keys that must sign for an action to be valid. Must be less than
              or equal to total number of key quorum members.

          key_quorum_ids: List of key quorum IDs that should be members of this key quorum. Key quorums
              can only be nested 1 level deep. At least one of `user_ids`, `public_keys`, or
              `key_quorum_ids` is required.

          public_keys: List of P-256 public keys of the keys that should be authorized to sign on the
              key quorum, in base64-encoded DER format. At least one of `user_ids`,
              `public_keys`, or `key_quorum_ids` is required.

          user_ids: List of user IDs of the users that should be authorized to sign on the key
              quorum. At least one of `user_ids`, `public_keys`, or `key_quorum_ids` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/key_quorums",
            body=maybe_transform(
                {
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                    "key_quorum_ids": key_quorum_ids,
                    "public_keys": public_keys,
                    "user_ids": user_ids,
                },
                key_quorum_create_params.KeyQuorumCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    def _delete(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Delete a key quorum by key quorum ID.

        Args:
          key_quorum_id: A unique identifier for a key quorum.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/v1/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def _update(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        authorization_threshold: float | Omit = omit,
        display_name: str | Omit = omit,
        key_quorum_ids: SequenceNotStr[str] | Omit = omit,
        public_keys: SequenceNotStr[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorum:
        """
        Update a key quorum by key quorum ID.

        Args:
          key_quorum_id: A unique identifier for a key quorum.

          authorization_threshold: The number of keys that must sign for an action to be valid. Must be less than
              or equal to total number of key quorum members.

          key_quorum_ids: List of key quorum IDs that should be members of this key quorum. Key quorums
              can only be nested 1 level deep.

          public_keys: List of P-256 public keys of the keys that should be authorized to sign on the
              key quorum, in base64-encoded DER format.

          user_ids: List of user IDs of the users that should be authorized to sign on the key
              quorum.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v1/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            body=maybe_transform(
                {
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                    "key_quorum_ids": key_quorum_ids,
                    "public_keys": public_keys,
                    "user_ids": user_ids,
                },
                key_quorum_update_params.KeyQuorumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    def get(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorum:
        """
        Get a key quorum by ID.

        Args:
          key_quorum_id: A unique identifier for a key quorum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        return self._get(
            path_template("/v1/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )


class AsyncKeyQuorumsResource(AsyncAPIResource):
    """Operations related to key quorums"""

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
        authorization_threshold: float | Omit = omit,
        display_name: str | Omit = omit,
        key_quorum_ids: SequenceNotStr[str] | Omit = omit,
        public_keys: SequenceNotStr[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorum:
        """
        Create a new key quorum.

        Args:
          authorization_threshold: The number of keys that must sign for an action to be valid. Must be less than
              or equal to total number of key quorum members.

          key_quorum_ids: List of key quorum IDs that should be members of this key quorum. Key quorums
              can only be nested 1 level deep. At least one of `user_ids`, `public_keys`, or
              `key_quorum_ids` is required.

          public_keys: List of P-256 public keys of the keys that should be authorized to sign on the
              key quorum, in base64-encoded DER format. At least one of `user_ids`,
              `public_keys`, or `key_quorum_ids` is required.

          user_ids: List of user IDs of the users that should be authorized to sign on the key
              quorum. At least one of `user_ids`, `public_keys`, or `key_quorum_ids` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/key_quorums",
            body=await async_maybe_transform(
                {
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                    "key_quorum_ids": key_quorum_ids,
                    "public_keys": public_keys,
                    "user_ids": user_ids,
                },
                key_quorum_create_params.KeyQuorumCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    async def _delete(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Delete a key quorum by key quorum ID.

        Args:
          key_quorum_id: A unique identifier for a key quorum.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/v1/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def _update(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        authorization_threshold: float | Omit = omit,
        display_name: str | Omit = omit,
        key_quorum_ids: SequenceNotStr[str] | Omit = omit,
        public_keys: SequenceNotStr[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorum:
        """
        Update a key quorum by key quorum ID.

        Args:
          key_quorum_id: A unique identifier for a key quorum.

          authorization_threshold: The number of keys that must sign for an action to be valid. Must be less than
              or equal to total number of key quorum members.

          key_quorum_ids: List of key quorum IDs that should be members of this key quorum. Key quorums
              can only be nested 1 level deep.

          public_keys: List of P-256 public keys of the keys that should be authorized to sign on the
              key quorum, in base64-encoded DER format.

          user_ids: List of user IDs of the users that should be authorized to sign on the key
              quorum.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v1/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            body=await async_maybe_transform(
                {
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                    "key_quorum_ids": key_quorum_ids,
                    "public_keys": public_keys,
                    "user_ids": user_ids,
                },
                key_quorum_update_params.KeyQuorumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorum,
        )

    async def get(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorum:
        """
        Get a key quorum by ID.

        Args:
          key_quorum_id: A unique identifier for a key quorum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        return await self._get(
            path_template("/v1/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
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
        self._delete = to_raw_response_wrapper(
            key_quorums._delete,
        )
        self._update = to_raw_response_wrapper(
            key_quorums._update,
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
        self._delete = async_to_raw_response_wrapper(
            key_quorums._delete,
        )
        self._update = async_to_raw_response_wrapper(
            key_quorums._update,
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
        self._delete = to_streamed_response_wrapper(
            key_quorums._delete,
        )
        self._update = to_streamed_response_wrapper(
            key_quorums._update,
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
        self._delete = async_to_streamed_response_wrapper(
            key_quorums._delete,
        )
        self._update = async_to_streamed_response_wrapper(
            key_quorums._update,
        )
        self.get = async_to_streamed_response_wrapper(
            key_quorums.get,
        )
