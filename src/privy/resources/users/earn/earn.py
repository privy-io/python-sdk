# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tmmf import (
    TmmfResource,
    AsyncTmmfResource,
    TmmfResourceWithRawResponse,
    AsyncTmmfResourceWithRawResponse,
    TmmfResourceWithStreamingResponse,
    AsyncTmmfResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EarnResource", "AsyncEarnResource"]


class EarnResource(SyncAPIResource):
    @cached_property
    def tmmf(self) -> TmmfResource:
        """Operations related to wallet actions"""
        return TmmfResource(self._client)

    @cached_property
    def with_raw_response(self) -> EarnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EarnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EarnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return EarnResourceWithStreamingResponse(self)


class AsyncEarnResource(AsyncAPIResource):
    @cached_property
    def tmmf(self) -> AsyncTmmfResource:
        """Operations related to wallet actions"""
        return AsyncTmmfResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEarnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEarnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEarnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncEarnResourceWithStreamingResponse(self)


class EarnResourceWithRawResponse:
    def __init__(self, earn: EarnResource) -> None:
        self._earn = earn

    @cached_property
    def tmmf(self) -> TmmfResourceWithRawResponse:
        """Operations related to wallet actions"""
        return TmmfResourceWithRawResponse(self._earn.tmmf)


class AsyncEarnResourceWithRawResponse:
    def __init__(self, earn: AsyncEarnResource) -> None:
        self._earn = earn

    @cached_property
    def tmmf(self) -> AsyncTmmfResourceWithRawResponse:
        """Operations related to wallet actions"""
        return AsyncTmmfResourceWithRawResponse(self._earn.tmmf)


class EarnResourceWithStreamingResponse:
    def __init__(self, earn: EarnResource) -> None:
        self._earn = earn

    @cached_property
    def tmmf(self) -> TmmfResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return TmmfResourceWithStreamingResponse(self._earn.tmmf)


class AsyncEarnResourceWithStreamingResponse:
    def __init__(self, earn: AsyncEarnResource) -> None:
        self._earn = earn

    @cached_property
    def tmmf(self) -> AsyncTmmfResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return AsyncTmmfResourceWithStreamingResponse(self._earn.tmmf)
