# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .ethereum.ethereum import (
    EthereumResource,
    AsyncEthereumResource,
    EthereumResourceWithRawResponse,
    AsyncEthereumResourceWithRawResponse,
    EthereumResourceWithStreamingResponse,
    AsyncEthereumResourceWithStreamingResponse,
)

__all__ = ["EarnResource", "AsyncEarnResource"]


class EarnResource(SyncAPIResource):
    @cached_property
    def ethereum(self) -> EthereumResource:
        """Operations related to wallet actions"""
        return EthereumResource(self._client)

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
    def ethereum(self) -> AsyncEthereumResource:
        """Operations related to wallet actions"""
        return AsyncEthereumResource(self._client)

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
    def ethereum(self) -> EthereumResourceWithRawResponse:
        """Operations related to wallet actions"""
        return EthereumResourceWithRawResponse(self._earn.ethereum)


class AsyncEarnResourceWithRawResponse:
    def __init__(self, earn: AsyncEarnResource) -> None:
        self._earn = earn

    @cached_property
    def ethereum(self) -> AsyncEthereumResourceWithRawResponse:
        """Operations related to wallet actions"""
        return AsyncEthereumResourceWithRawResponse(self._earn.ethereum)


class EarnResourceWithStreamingResponse:
    def __init__(self, earn: EarnResource) -> None:
        self._earn = earn

    @cached_property
    def ethereum(self) -> EthereumResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return EthereumResourceWithStreamingResponse(self._earn.ethereum)


class AsyncEarnResourceWithStreamingResponse:
    def __init__(self, earn: AsyncEarnResource) -> None:
        self._earn = earn

    @cached_property
    def ethereum(self) -> AsyncEthereumResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return AsyncEthereumResourceWithStreamingResponse(self._earn.ethereum)
