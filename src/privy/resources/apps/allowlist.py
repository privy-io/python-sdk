# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...types import EmailDomain
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.apps import allowlist_create_params, allowlist_delete_params
from ..._base_client import make_request_options
from ...types.email_domain import EmailDomain
from ...types.allowlist_entry import AllowlistEntry
from ...types.allowlist_deletion_response import AllowlistDeletionResponse
from ...types.apps.allowlist_list_response import AllowlistListResponse

__all__ = ["AllowlistResource", "AsyncAllowlistResource"]


class AllowlistResource(SyncAPIResource):
    """Operations related to app settings and allowlist management"""

    @cached_property
    def with_raw_response(self) -> AllowlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AllowlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllowlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AllowlistResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        app_id: str,
        *,
        type: Literal["email"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        app_id: str,
        *,
        type: Literal["emailDomain"],
        value: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          value: An email domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        app_id: str,
        *,
        type: Literal["wallet"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        app_id: str,
        *,
        type: Literal["phone"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type", "value"])
    def create(
        self,
        app_id: str,
        *,
        type: Literal["email"] | Literal["emailDomain"] | Literal["wallet"] | Literal["phone"],
        value: str | EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            path_template("/v1/apps/{app_id}/allowlist", app_id=app_id),
            body=maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                allowlist_create_params.AllowlistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistEntry,
        )

    def list(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistListResponse:
        """Get all allowlist entries for an app.

        Returns the list of users allowed to
        access the app when the allowlist is enabled.

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
            path_template("/v1/apps/{app_id}/allowlist", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistListResponse,
        )

    @overload
    def delete(
        self,
        app_id: str,
        *,
        type: Literal["email"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete(
        self,
        app_id: str,
        *,
        type: Literal["emailDomain"],
        value: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          value: An email domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete(
        self,
        app_id: str,
        *,
        type: Literal["wallet"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete(
        self,
        app_id: str,
        *,
        type: Literal["phone"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type", "value"])
    def delete(
        self,
        app_id: str,
        *,
        type: Literal["email"] | Literal["emailDomain"] | Literal["wallet"] | Literal["phone"],
        value: str | EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._delete(
            path_template("/v1/apps/{app_id}/allowlist", app_id=app_id),
            body=maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                allowlist_delete_params.AllowlistDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistDeletionResponse,
        )


class AsyncAllowlistResource(AsyncAPIResource):
    """Operations related to app settings and allowlist management"""

    @cached_property
    def with_raw_response(self) -> AsyncAllowlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAllowlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllowlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncAllowlistResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        app_id: str,
        *,
        type: Literal["email"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        app_id: str,
        *,
        type: Literal["emailDomain"],
        value: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          value: An email domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        app_id: str,
        *,
        type: Literal["wallet"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        app_id: str,
        *,
        type: Literal["phone"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        """Add a new entry to the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type", "value"])
    async def create(
        self,
        app_id: str,
        *,
        type: Literal["email"] | Literal["emailDomain"] | Literal["wallet"] | Literal["phone"],
        value: str | EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistEntry:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            path_template("/v1/apps/{app_id}/allowlist", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                allowlist_create_params.AllowlistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistEntry,
        )

    async def list(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistListResponse:
        """Get all allowlist entries for an app.

        Returns the list of users allowed to
        access the app when the allowlist is enabled.

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
            path_template("/v1/apps/{app_id}/allowlist", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistListResponse,
        )

    @overload
    async def delete(
        self,
        app_id: str,
        *,
        type: Literal["email"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete(
        self,
        app_id: str,
        *,
        type: Literal["emailDomain"],
        value: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          value: An email domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete(
        self,
        app_id: str,
        *,
        type: Literal["wallet"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete(
        self,
        app_id: str,
        *,
        type: Literal["phone"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        """Remove an entry from the allowlist for an app.

        The allowlist must be enabled.

        Args:
          app_id: The ID of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type", "value"])
    async def delete(
        self,
        app_id: str,
        *,
        type: Literal["email"] | Literal["emailDomain"] | Literal["wallet"] | Literal["phone"],
        value: str | EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AllowlistDeletionResponse:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._delete(
            path_template("/v1/apps/{app_id}/allowlist", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                allowlist_delete_params.AllowlistDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistDeletionResponse,
        )


class AllowlistResourceWithRawResponse:
    def __init__(self, allowlist: AllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = to_raw_response_wrapper(
            allowlist.create,
        )
        self.list = to_raw_response_wrapper(
            allowlist.list,
        )
        self.delete = to_raw_response_wrapper(
            allowlist.delete,
        )


class AsyncAllowlistResourceWithRawResponse:
    def __init__(self, allowlist: AsyncAllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = async_to_raw_response_wrapper(
            allowlist.create,
        )
        self.list = async_to_raw_response_wrapper(
            allowlist.list,
        )
        self.delete = async_to_raw_response_wrapper(
            allowlist.delete,
        )


class AllowlistResourceWithStreamingResponse:
    def __init__(self, allowlist: AllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = to_streamed_response_wrapper(
            allowlist.create,
        )
        self.list = to_streamed_response_wrapper(
            allowlist.list,
        )
        self.delete = to_streamed_response_wrapper(
            allowlist.delete,
        )


class AsyncAllowlistResourceWithStreamingResponse:
    def __init__(self, allowlist: AsyncAllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = async_to_streamed_response_wrapper(
            allowlist.create,
        )
        self.list = async_to_streamed_response_wrapper(
            allowlist.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            allowlist.delete,
        )
