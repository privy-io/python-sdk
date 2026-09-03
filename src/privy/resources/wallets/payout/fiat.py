# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.wallets.payout import fiat_create_params
from ....types.payout_source_param import PayoutSourceParam
from ....types.wallets.payout_response import PayoutResponse
from ....types.payout_destination_param import PayoutDestinationParam

__all__ = ["FiatResource", "AsyncFiatResource"]


class FiatResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> FiatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FiatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return FiatResourceWithStreamingResponse(self)

    def _create(
        self,
        wallet_id: str,
        *,
        destination: PayoutDestinationParam,
        source: PayoutSourceParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutResponse:
        """
        Initiates a payout (crypto to fiat offramp) from a wallet to a previously
        registered external fiat account. Returns a pending wallet action; the crypto
        transfer and fiat settlement are processed asynchronously.

        Args:
          wallet_id: The ID of the wallet.

          destination: The destination bank account for a payout.

          source: The source crypto asset, chain, and amount for a payout.

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
            path_template("/v1/wallets/{wallet_id}/payout/fiat", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                fiat_create_params.FiatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutResponse,
        )


class AsyncFiatResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AsyncFiatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFiatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncFiatResourceWithStreamingResponse(self)

    async def _create(
        self,
        wallet_id: str,
        *,
        destination: PayoutDestinationParam,
        source: PayoutSourceParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutResponse:
        """
        Initiates a payout (crypto to fiat offramp) from a wallet to a previously
        registered external fiat account. Returns a pending wallet action; the crypto
        transfer and fiat settlement are processed asynchronously.

        Args:
          wallet_id: The ID of the wallet.

          destination: The destination bank account for a payout.

          source: The source crypto asset, chain, and amount for a payout.

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
            path_template("/v1/wallets/{wallet_id}/payout/fiat", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                fiat_create_params.FiatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutResponse,
        )


class FiatResourceWithRawResponse:
    def __init__(self, fiat: FiatResource) -> None:
        self._fiat = fiat

        self._create = to_raw_response_wrapper(
            fiat._create,
        )


class AsyncFiatResourceWithRawResponse:
    def __init__(self, fiat: AsyncFiatResource) -> None:
        self._fiat = fiat

        self._create = async_to_raw_response_wrapper(
            fiat._create,
        )


class FiatResourceWithStreamingResponse:
    def __init__(self, fiat: FiatResource) -> None:
        self._fiat = fiat

        self._create = to_streamed_response_wrapper(
            fiat._create,
        )


class AsyncFiatResourceWithStreamingResponse:
    def __init__(self, fiat: AsyncFiatResource) -> None:
        self._fiat = fiat

        self._create = async_to_streamed_response_wrapper(
            fiat._create,
        )
