# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
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
from ...types.wallets import transaction_get_params
from ...types.wallet_asset import WalletAsset
from ...types.transaction_token_address_input import TransactionTokenAddressInput
from ...types.wallets.transaction_get_response import TransactionGetResponse
from ...types.transaction_chain_name_input_param import TransactionChainNameInputParam

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    """Operations related to wallets"""

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
        wallet_id: str,
        *,
        chain: TransactionChainNameInputParam,
        token: Union[TransactionTokenAddressInput, SequenceNotStr[TransactionTokenAddressInput]] | Omit = omit,
        asset: Union[
            Literal[
                "usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "ousd", "pathusd", "sol", "trx"
            ],
            List[WalletAsset],
        ]
        | Omit = omit,
        cursor: str | Omit = omit,
        include_archived: bool | Omit = omit,
        limit: Optional[float] | Omit = omit,
        tx_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionGetResponse:
        """
        Get incoming and outgoing transactions of a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          chain: Chains supported for transaction history queries.

          token: Exactly one of `token` or `asset` is required. Cannot be used together with
              `asset`.

          asset: Exactly one of `asset` or `token` is required. Cannot be used together with
              `token`.

          include_archived: Include archived wallets in lookup. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}/transactions", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chain": chain,
                        "token": token,
                        "asset": asset,
                        "cursor": cursor,
                        "include_archived": include_archived,
                        "limit": limit,
                        "tx_hash": tx_hash,
                    },
                    transaction_get_params.TransactionGetParams,
                ),
            ),
            cast_to=TransactionGetResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    """Operations related to wallets"""

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
        wallet_id: str,
        *,
        chain: TransactionChainNameInputParam,
        token: Union[TransactionTokenAddressInput, SequenceNotStr[TransactionTokenAddressInput]] | Omit = omit,
        asset: Union[
            Literal[
                "usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "ousd", "pathusd", "sol", "trx"
            ],
            List[WalletAsset],
        ]
        | Omit = omit,
        cursor: str | Omit = omit,
        include_archived: bool | Omit = omit,
        limit: Optional[float] | Omit = omit,
        tx_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionGetResponse:
        """
        Get incoming and outgoing transactions of a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          chain: Chains supported for transaction history queries.

          token: Exactly one of `token` or `asset` is required. Cannot be used together with
              `asset`.

          asset: Exactly one of `asset` or `token` is required. Cannot be used together with
              `token`.

          include_archived: Include archived wallets in lookup. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}/transactions", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "chain": chain,
                        "token": token,
                        "asset": asset,
                        "cursor": cursor,
                        "include_archived": include_archived,
                        "limit": limit,
                        "tx_hash": tx_hash,
                    },
                    transaction_get_params.TransactionGetParams,
                ),
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
