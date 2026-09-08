# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import WalletAutomationReindexCaip2, wallet_automation_reindex_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.wallet_automation_reindex_caip_2 import WalletAutomationReindexCaip2
from ..types.wallet_automation_reindex_response import WalletAutomationReindexResponse

__all__ = ["WalletAutomationsResource", "AsyncWalletAutomationsResource"]


class WalletAutomationsResource(SyncAPIResource):
    """Operations related to wallet automations"""

    @cached_property
    def with_raw_response(self) -> WalletAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return WalletAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return WalletAutomationsResourceWithStreamingResponse(self)

    def reindex(
        self,
        *,
        asset_address: str,
        caip2: WalletAutomationReindexCaip2 | Omit = omit,
        chain: str | Omit = omit,
        deposit_address: str | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationReindexResponse:
        """
        Re-checks a wallet (identified by wallet_id or deposit_address) for funds
        matching its wallet automation configs and triggers an automation run if a match
        is found. Use this to recover a deposit whose automation trigger was missed or
        failed.

        Args:
          asset_address: Asset contract address to check; the native asset uses `native`.

          caip2: EVM CAIP-2 chain identifier (e.g. "eip155:4217" for Tempo, "eip155:1" for
              Ethereum).

          chain: Human-readable chain name to check. Specify exactly one of `caip2` or `chain`.

          deposit_address: On-chain deposit address of the wallet to reindex. Must match the resolved
              wallet's address if `wallet_id` is also provided.

          wallet_id: Privy wallet ID to reindex. Takes precedence over `deposit_address` when both
              are supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/wallet_automations/reindex",
            body=maybe_transform(
                {
                    "asset_address": asset_address,
                    "caip2": caip2,
                    "chain": chain,
                    "deposit_address": deposit_address,
                    "wallet_id": wallet_id,
                },
                wallet_automation_reindex_params.WalletAutomationReindexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationReindexResponse,
        )


class AsyncWalletAutomationsResource(AsyncAPIResource):
    """Operations related to wallet automations"""

    @cached_property
    def with_raw_response(self) -> AsyncWalletAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncWalletAutomationsResourceWithStreamingResponse(self)

    async def reindex(
        self,
        *,
        asset_address: str,
        caip2: WalletAutomationReindexCaip2 | Omit = omit,
        chain: str | Omit = omit,
        deposit_address: str | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationReindexResponse:
        """
        Re-checks a wallet (identified by wallet_id or deposit_address) for funds
        matching its wallet automation configs and triggers an automation run if a match
        is found. Use this to recover a deposit whose automation trigger was missed or
        failed.

        Args:
          asset_address: Asset contract address to check; the native asset uses `native`.

          caip2: EVM CAIP-2 chain identifier (e.g. "eip155:4217" for Tempo, "eip155:1" for
              Ethereum).

          chain: Human-readable chain name to check. Specify exactly one of `caip2` or `chain`.

          deposit_address: On-chain deposit address of the wallet to reindex. Must match the resolved
              wallet's address if `wallet_id` is also provided.

          wallet_id: Privy wallet ID to reindex. Takes precedence over `deposit_address` when both
              are supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/wallet_automations/reindex",
            body=await async_maybe_transform(
                {
                    "asset_address": asset_address,
                    "caip2": caip2,
                    "chain": chain,
                    "deposit_address": deposit_address,
                    "wallet_id": wallet_id,
                },
                wallet_automation_reindex_params.WalletAutomationReindexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationReindexResponse,
        )


class WalletAutomationsResourceWithRawResponse:
    def __init__(self, wallet_automations: WalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.reindex = to_raw_response_wrapper(
            wallet_automations.reindex,
        )


class AsyncWalletAutomationsResourceWithRawResponse:
    def __init__(self, wallet_automations: AsyncWalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.reindex = async_to_raw_response_wrapper(
            wallet_automations.reindex,
        )


class WalletAutomationsResourceWithStreamingResponse:
    def __init__(self, wallet_automations: WalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.reindex = to_streamed_response_wrapper(
            wallet_automations.reindex,
        )


class AsyncWalletAutomationsResourceWithStreamingResponse:
    def __init__(self, wallet_automations: AsyncWalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.reindex = async_to_streamed_response_wrapper(
            wallet_automations.reindex,
        )
