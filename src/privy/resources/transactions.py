# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.transaction_get_response import TransactionGetResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def get(
        self,
        transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionGetResponse:
        """
        Get a transaction by transaction ID.

        Args:
          transaction_id: ID of the transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        return self._get(
            f"/v1/transactions/{transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionGetResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def get(
        self,
        transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionGetResponse:
        """
        Get a transaction by transaction ID.

        Args:
          transaction_id: ID of the transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        return await self._get(
            f"/v1/transactions/{transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionGetResponse,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.get = to_raw_response_wrapper(
            transactions.get,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.get = async_to_raw_response_wrapper(
            transactions.get,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.get = to_streamed_response_wrapper(
            transactions.get,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.get = async_to_streamed_response_wrapper(
            transactions.get,
        )
