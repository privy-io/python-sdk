# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.wallets import balance_get_params
from ...types.wallets.balance_get_response import BalanceGetResponse

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return BalanceResourceWithStreamingResponse(self)

    def get(
        self,
        wallet_id: str,
        *,
        asset: Union[Literal["usdc", "eth", "pol", "sol"], List[Literal["usdc", "eth", "pol", "sol"]]],
        chain: Union[
            Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"],
            List[Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"]],
        ],
        include_currency: Literal["usd"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceGetResponse:
        """
        Get the balance of a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            f"/v1/wallets/{wallet_id}/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset": asset,
                        "chain": chain,
                        "include_currency": include_currency,
                    },
                    balance_get_params.BalanceGetParams,
                ),
            ),
            cast_to=BalanceGetResponse,
        )


class AsyncBalanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncBalanceResourceWithStreamingResponse(self)

    async def get(
        self,
        wallet_id: str,
        *,
        asset: Union[Literal["usdc", "eth", "pol", "sol"], List[Literal["usdc", "eth", "pol", "sol"]]],
        chain: Union[
            Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"],
            List[Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"]],
        ],
        include_currency: Literal["usd"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceGetResponse:
        """
        Get the balance of a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            f"/v1/wallets/{wallet_id}/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset": asset,
                        "chain": chain,
                        "include_currency": include_currency,
                    },
                    balance_get_params.BalanceGetParams,
                ),
            ),
            cast_to=BalanceGetResponse,
        )


class BalanceResourceWithRawResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.get = to_raw_response_wrapper(
            balance.get,
        )


class AsyncBalanceResourceWithRawResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.get = async_to_raw_response_wrapper(
            balance.get,
        )


class BalanceResourceWithStreamingResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.get = to_streamed_response_wrapper(
            balance.get,
        )


class AsyncBalanceResourceWithStreamingResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.get = async_to_streamed_response_wrapper(
            balance.get,
        )
