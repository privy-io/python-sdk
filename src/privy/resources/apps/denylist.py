# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ...types import EmailDomain
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursor, AsyncCursor
from ...types.apps import denylist_list_params, denylist_create_params, denylist_delete_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_domain import EmailDomain
from ...types.denylist_entry import DenylistEntry

__all__ = ["DenylistResource", "AsyncDenylistResource"]


class DenylistResource(SyncAPIResource):
    """Operations related to app settings and allowlist management"""

    @cached_property
    def with_raw_response(self) -> DenylistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return DenylistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DenylistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return DenylistResourceWithStreamingResponse(self)

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
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["phone"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["ethereumAddress"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["solanaAddress"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["email"]
        | Literal["emailDomain"]
        | Literal["phone"]
        | Literal["ethereumAddress"]
        | Literal["solanaAddress"],
        value: str | EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            path_template("/v1/apps/{app_id}/denylist", app_id=app_id),
            body=maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                denylist_create_params.DenylistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DenylistEntry,
        )

    def list(
        self,
        app_id: str,
        *,
        cursor: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[DenylistEntry]:
        """
        Get a page of denylist entries for an app, which block matching users from
        logging in or linking the account.

        Args:
          app_id: The ID of the app.

          cursor: Cursor returned by the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get_api_list(
            path_template("/v1/apps/{app_id}/denylist", app_id=app_id),
            page=SyncCursor[DenylistEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    denylist_list_params.DenylistListParams,
                ),
            ),
            model=DenylistEntry,
        )

    def delete(
        self,
        app_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove an entry from the denylist for an app by its ID.

        Get entry IDs from the
        list denylist entries endpoint.

        Args:
          app_id: The ID of the app.

          id: The ID of the denylist entry to remove.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/apps/{app_id}/denylist", app_id=app_id),
            body=maybe_transform({"id": id}, denylist_delete_params.DenylistDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDenylistResource(AsyncAPIResource):
    """Operations related to app settings and allowlist management"""

    @cached_property
    def with_raw_response(self) -> AsyncDenylistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDenylistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDenylistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncDenylistResourceWithStreamingResponse(self)

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
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["phone"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["ethereumAddress"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["solanaAddress"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        """Add a new entry to the denylist for an app.

        Adding an entry that already exists
        returns the existing entry.

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
        type: Literal["email"]
        | Literal["emailDomain"]
        | Literal["phone"]
        | Literal["ethereumAddress"]
        | Literal["solanaAddress"],
        value: str | EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DenylistEntry:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            path_template("/v1/apps/{app_id}/denylist", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                denylist_create_params.DenylistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DenylistEntry,
        )

    def list(
        self,
        app_id: str,
        *,
        cursor: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DenylistEntry, AsyncCursor[DenylistEntry]]:
        """
        Get a page of denylist entries for an app, which block matching users from
        logging in or linking the account.

        Args:
          app_id: The ID of the app.

          cursor: Cursor returned by the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get_api_list(
            path_template("/v1/apps/{app_id}/denylist", app_id=app_id),
            page=AsyncCursor[DenylistEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    denylist_list_params.DenylistListParams,
                ),
            ),
            model=DenylistEntry,
        )

    async def delete(
        self,
        app_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove an entry from the denylist for an app by its ID.

        Get entry IDs from the
        list denylist entries endpoint.

        Args:
          app_id: The ID of the app.

          id: The ID of the denylist entry to remove.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/apps/{app_id}/denylist", app_id=app_id),
            body=await async_maybe_transform({"id": id}, denylist_delete_params.DenylistDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DenylistResourceWithRawResponse:
    def __init__(self, denylist: DenylistResource) -> None:
        self._denylist = denylist

        self.create = to_raw_response_wrapper(
            denylist.create,
        )
        self.list = to_raw_response_wrapper(
            denylist.list,
        )
        self.delete = to_raw_response_wrapper(
            denylist.delete,
        )


class AsyncDenylistResourceWithRawResponse:
    def __init__(self, denylist: AsyncDenylistResource) -> None:
        self._denylist = denylist

        self.create = async_to_raw_response_wrapper(
            denylist.create,
        )
        self.list = async_to_raw_response_wrapper(
            denylist.list,
        )
        self.delete = async_to_raw_response_wrapper(
            denylist.delete,
        )


class DenylistResourceWithStreamingResponse:
    def __init__(self, denylist: DenylistResource) -> None:
        self._denylist = denylist

        self.create = to_streamed_response_wrapper(
            denylist.create,
        )
        self.list = to_streamed_response_wrapper(
            denylist.list,
        )
        self.delete = to_streamed_response_wrapper(
            denylist.delete,
        )


class AsyncDenylistResourceWithStreamingResponse:
    def __init__(self, denylist: AsyncDenylistResource) -> None:
        self._denylist = denylist

        self.create = async_to_streamed_response_wrapper(
            denylist.create,
        )
        self.list = async_to_streamed_response_wrapper(
            denylist.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            denylist.delete,
        )
