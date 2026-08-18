# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .....types import WalletActionNonce
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.wallet_action_nonce import WalletActionNonce
from .....types.wallets.earn.ethereum import incentive_claim_params
from .....types.wallets.earn_incentive_claim_action_response import EarnIncentiveClaimActionResponse

__all__ = ["IncentiveResource", "AsyncIncentiveResource"]


class IncentiveResource(SyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> IncentiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return IncentiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncentiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return IncentiveResourceWithStreamingResponse(self)

    def _claim(
        self,
        wallet_id: str,
        *,
        chain: str,
        nonce: WalletActionNonce | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarnIncentiveClaimActionResponse:
        """
        Claim incentive rewards for a wallet.

        Args:
          wallet_id: ID of the wallet.

          chain: The blockchain network on which to perform the incentive claim. Supported chains
              include: 'tempo', 'ethereum', 'base', 'arbitrum', 'polygon', 'solana', and more,
              along with their respective testnets.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

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
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/incentive/claim", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "chain": chain,
                    "nonce": nonce,
                },
                incentive_claim_params.IncentiveClaimParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarnIncentiveClaimActionResponse,
        )


class AsyncIncentiveResource(AsyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> AsyncIncentiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIncentiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncentiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncIncentiveResourceWithStreamingResponse(self)

    async def _claim(
        self,
        wallet_id: str,
        *,
        chain: str,
        nonce: WalletActionNonce | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EarnIncentiveClaimActionResponse:
        """
        Claim incentive rewards for a wallet.

        Args:
          wallet_id: ID of the wallet.

          chain: The blockchain network on which to perform the incentive claim. Supported chains
              include: 'tempo', 'ethereum', 'base', 'arbitrum', 'polygon', 'solana', and more,
              along with their respective testnets.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

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
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/incentive/claim", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "chain": chain,
                    "nonce": nonce,
                },
                incentive_claim_params.IncentiveClaimParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarnIncentiveClaimActionResponse,
        )


class IncentiveResourceWithRawResponse:
    def __init__(self, incentive: IncentiveResource) -> None:
        self._incentive = incentive

        self._claim = to_raw_response_wrapper(
            incentive._claim,
        )


class AsyncIncentiveResourceWithRawResponse:
    def __init__(self, incentive: AsyncIncentiveResource) -> None:
        self._incentive = incentive

        self._claim = async_to_raw_response_wrapper(
            incentive._claim,
        )


class IncentiveResourceWithStreamingResponse:
    def __init__(self, incentive: IncentiveResource) -> None:
        self._incentive = incentive

        self._claim = to_streamed_response_wrapper(
            incentive._claim,
        )


class AsyncIncentiveResourceWithStreamingResponse:
    def __init__(self, incentive: AsyncIncentiveResource) -> None:
        self._incentive = incentive

        self._claim = async_to_streamed_response_wrapper(
            incentive._claim,
        )
