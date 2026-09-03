# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .fiat import (
    FiatResource,
    AsyncFiatResource,
    FiatResourceWithRawResponse,
    AsyncFiatResourceWithRawResponse,
    FiatResourceWithStreamingResponse,
    AsyncFiatResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PayoutResource", "AsyncPayoutResource"]


class PayoutResource(SyncAPIResource):
    @cached_property
    def fiat(self) -> FiatResource:
        """Operations related to fiat onramping and offramping"""
        return FiatResource(self._client)

    @cached_property
    def with_raw_response(self) -> PayoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return PayoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return PayoutResourceWithStreamingResponse(self)


class AsyncPayoutResource(AsyncAPIResource):
    @cached_property
    def fiat(self) -> AsyncFiatResource:
        """Operations related to fiat onramping and offramping"""
        return AsyncFiatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPayoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncPayoutResourceWithStreamingResponse(self)


class PayoutResourceWithRawResponse:
    def __init__(self, payout: PayoutResource) -> None:
        self._payout = payout

    @cached_property
    def fiat(self) -> FiatResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return FiatResourceWithRawResponse(self._payout.fiat)


class AsyncPayoutResourceWithRawResponse:
    def __init__(self, payout: AsyncPayoutResource) -> None:
        self._payout = payout

    @cached_property
    def fiat(self) -> AsyncFiatResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncFiatResourceWithRawResponse(self._payout.fiat)


class PayoutResourceWithStreamingResponse:
    def __init__(self, payout: PayoutResource) -> None:
        self._payout = payout

    @cached_property
    def fiat(self) -> FiatResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return FiatResourceWithStreamingResponse(self._payout.fiat)


class AsyncPayoutResourceWithStreamingResponse:
    def __init__(self, payout: AsyncPayoutResource) -> None:
        self._payout = payout

    @cached_property
    def fiat(self) -> AsyncFiatResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncFiatResourceWithStreamingResponse(self._payout.fiat)
