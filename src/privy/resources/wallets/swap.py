# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import AmountType, WalletActionNonce
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.wallets import swap_quote_params, swap_execute_params
from ...types.amount_type import AmountType
from ...types.swap_source_param import SwapSourceParam
from ...types.swap_quote_response import SwapQuoteResponse
from ...types.wallet_action_nonce import WalletActionNonce
from ...types.swap_destination_param import SwapDestinationParam
from ...types.fee_configuration_param import FeeConfigurationParam
from ...types.swap_quote_destination_param import SwapQuoteDestinationParam
from ...types.wallets.swap_action_response import SwapActionResponse

__all__ = ["SwapResource", "AsyncSwapResource"]


class SwapResource(SyncAPIResource):
    """Operations for swapping tokens within wallets"""

    @cached_property
    def with_raw_response(self) -> SwapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SwapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return SwapResourceWithStreamingResponse(self)

    def execute(
        self,
        wallet_id: str,
        *,
        base_amount: str,
        destination: SwapDestinationParam,
        source: SwapSourceParam,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        reference_id: str | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapActionResponse:
        """
        Execute a token swap within a wallet.

        Args:
          wallet_id: ID of the wallet.

          base_amount: Amount in base units (e.g., wei for ETH). Must be a non-negative integer string.

          destination: The output side of a swap execution request.

          source: The input side of a swap request, including token and chain.

          amount_type: Whether the amount refers to the input token or output token.

          fee_configuration: Total fees assessed on a transfer, in BPS

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          reference_id: Developer-provided identifier for this request. Must be unique per app.

          slippage_bps: Maximum slippage tolerance in basis points (e.g., 50 for 0.5%).

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/wallets/{wallet_id}/swap", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "base_amount": base_amount,
                    "destination": destination,
                    "source": source,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "nonce": nonce,
                    "reference_id": reference_id,
                    "slippage_bps": slippage_bps,
                },
                swap_execute_params.SwapExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapActionResponse,
        )

    def quote(
        self,
        wallet_id: str,
        *,
        base_amount: str,
        destination: SwapQuoteDestinationParam,
        source: SwapSourceParam,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapQuoteResponse:
        """
        Get a price quote for swapping tokens within a wallet.

        Args:
          wallet_id: ID of the wallet.

          base_amount: Amount in base units (e.g., wei for ETH). Must be a non-negative integer string.

          destination: The output side of a swap quote request.

          source: The input side of a swap request, including token and chain.

          amount_type: Whether the amount refers to the input token or output token.

          fee_configuration: Total fees assessed on a transfer, in BPS

          slippage_bps: Maximum slippage tolerance in basis points (e.g., 50 for 0.5%). If omitted,
              auto-slippage is used.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/wallets/{wallet_id}/swap/quote", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "base_amount": base_amount,
                    "destination": destination,
                    "source": source,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "slippage_bps": slippage_bps,
                },
                swap_quote_params.SwapQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapQuoteResponse,
        )


class AsyncSwapResource(AsyncAPIResource):
    """Operations for swapping tokens within wallets"""

    @cached_property
    def with_raw_response(self) -> AsyncSwapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSwapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncSwapResourceWithStreamingResponse(self)

    async def execute(
        self,
        wallet_id: str,
        *,
        base_amount: str,
        destination: SwapDestinationParam,
        source: SwapSourceParam,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        reference_id: str | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapActionResponse:
        """
        Execute a token swap within a wallet.

        Args:
          wallet_id: ID of the wallet.

          base_amount: Amount in base units (e.g., wei for ETH). Must be a non-negative integer string.

          destination: The output side of a swap execution request.

          source: The input side of a swap request, including token and chain.

          amount_type: Whether the amount refers to the input token or output token.

          fee_configuration: Total fees assessed on a transfer, in BPS

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          reference_id: Developer-provided identifier for this request. Must be unique per app.

          slippage_bps: Maximum slippage tolerance in basis points (e.g., 50 for 0.5%).

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/swap", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "base_amount": base_amount,
                    "destination": destination,
                    "source": source,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "nonce": nonce,
                    "reference_id": reference_id,
                    "slippage_bps": slippage_bps,
                },
                swap_execute_params.SwapExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapActionResponse,
        )

    async def quote(
        self,
        wallet_id: str,
        *,
        base_amount: str,
        destination: SwapQuoteDestinationParam,
        source: SwapSourceParam,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapQuoteResponse:
        """
        Get a price quote for swapping tokens within a wallet.

        Args:
          wallet_id: ID of the wallet.

          base_amount: Amount in base units (e.g., wei for ETH). Must be a non-negative integer string.

          destination: The output side of a swap quote request.

          source: The input side of a swap request, including token and chain.

          amount_type: Whether the amount refers to the input token or output token.

          fee_configuration: Total fees assessed on a transfer, in BPS

          slippage_bps: Maximum slippage tolerance in basis points (e.g., 50 for 0.5%). If omitted,
              auto-slippage is used.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/swap/quote", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "base_amount": base_amount,
                    "destination": destination,
                    "source": source,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "slippage_bps": slippage_bps,
                },
                swap_quote_params.SwapQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapQuoteResponse,
        )


class SwapResourceWithRawResponse:
    def __init__(self, swap: SwapResource) -> None:
        self._swap = swap

        self.execute = to_raw_response_wrapper(
            swap.execute,
        )
        self.quote = to_raw_response_wrapper(
            swap.quote,
        )


class AsyncSwapResourceWithRawResponse:
    def __init__(self, swap: AsyncSwapResource) -> None:
        self._swap = swap

        self.execute = async_to_raw_response_wrapper(
            swap.execute,
        )
        self.quote = async_to_raw_response_wrapper(
            swap.quote,
        )


class SwapResourceWithStreamingResponse:
    def __init__(self, swap: SwapResource) -> None:
        self._swap = swap

        self.execute = to_streamed_response_wrapper(
            swap.execute,
        )
        self.quote = to_streamed_response_wrapper(
            swap.quote,
        )


class AsyncSwapResourceWithStreamingResponse:
    def __init__(self, swap: AsyncSwapResource) -> None:
        self._swap = swap

        self.execute = async_to_streamed_response_wrapper(
            swap.execute,
        )
        self.quote = async_to_streamed_response_wrapper(
            swap.quote,
        )
