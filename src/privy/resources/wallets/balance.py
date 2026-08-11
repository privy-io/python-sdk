# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.wallet_asset import WalletAsset
from ...types.wallets.balance_get_response import BalanceGetResponse
from ...types.wallet_asset_chain_name_input_param import WalletAssetChainNameInputParam

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    """Operations related to wallets"""

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
        token: Union[str, SequenceNotStr[str]] | Omit = omit,
        asset: Union[
            Literal["usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "pathusd", "sol", "trx"],
            List[WalletAsset],
        ]
        | Omit = omit,
        chain: Union[
            Literal[
                "ethereum",
                "arbitrum",
                "avalanche",
                "base",
                "tempo",
                "linea",
                "optimism",
                "polygon",
                "bsc",
                "solana",
                "tron",
                "zksync_era",
                "hoodi",
                "sepolia",
                "arbitrum_sepolia",
                "avalanche_fuji",
                "base_sepolia",
                "linea_testnet",
                "optimism_sepolia",
                "polygon_amoy",
                "solana_devnet",
                "solana_testnet",
                "tron_nile",
            ],
            str,
            List[WalletAssetChainNameInputParam],
        ]
        | Omit = omit,
        include_archived: bool | Omit = omit,
        include_currency: Literal["usd", "eur"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetResponse:
        """
        Get the balance of a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          token: The token contract address(es) to query in format "chain:address" (e.g.,
              "tempo:0x20c000000000000000000000b9537d11c60e8b50" or
              "solana:EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"). Cannot be used together
              with `asset`/`chain` or with `include_currency`.

          asset: Named asset(s) to query (e.g. `eth`, `usdc`). Use together with `chain` to scope
              the query. Cannot be used with `token`.

          chain: Chain(s) to query named assets on (e.g. `tempo`, `base`). Use together with
              `asset`. Cannot be used with `token`.

          include_archived: Include archived wallets in lookup. Defaults to false.

          include_currency: If set, balances are converted to the specified fiat currency. Not supported
              when `token` is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}/balance", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "asset": asset,
                        "chain": chain,
                        "include_archived": include_archived,
                        "include_currency": include_currency,
                    },
                    balance_get_params.BalanceGetParams,
                ),
            ),
            cast_to=BalanceGetResponse,
        )


class AsyncBalanceResource(AsyncAPIResource):
    """Operations related to wallets"""

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
        token: Union[str, SequenceNotStr[str]] | Omit = omit,
        asset: Union[
            Literal["usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "pathusd", "sol", "trx"],
            List[WalletAsset],
        ]
        | Omit = omit,
        chain: Union[
            Literal[
                "ethereum",
                "arbitrum",
                "avalanche",
                "base",
                "tempo",
                "linea",
                "optimism",
                "polygon",
                "bsc",
                "solana",
                "tron",
                "zksync_era",
                "hoodi",
                "sepolia",
                "arbitrum_sepolia",
                "avalanche_fuji",
                "base_sepolia",
                "linea_testnet",
                "optimism_sepolia",
                "polygon_amoy",
                "solana_devnet",
                "solana_testnet",
                "tron_nile",
            ],
            str,
            List[WalletAssetChainNameInputParam],
        ]
        | Omit = omit,
        include_archived: bool | Omit = omit,
        include_currency: Literal["usd", "eur"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetResponse:
        """
        Get the balance of a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          token: The token contract address(es) to query in format "chain:address" (e.g.,
              "tempo:0x20c000000000000000000000b9537d11c60e8b50" or
              "solana:EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"). Cannot be used together
              with `asset`/`chain` or with `include_currency`.

          asset: Named asset(s) to query (e.g. `eth`, `usdc`). Use together with `chain` to scope
              the query. Cannot be used with `token`.

          chain: Chain(s) to query named assets on (e.g. `tempo`, `base`). Use together with
              `asset`. Cannot be used with `token`.

          include_archived: Include archived wallets in lookup. Defaults to false.

          include_currency: If set, balances are converted to the specified fiat currency. Not supported
              when `token` is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}/balance", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "asset": asset,
                        "chain": chain,
                        "include_archived": include_archived,
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
