# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....types import WalletActionNonce
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
from ....types.wallets import TmmfFund, TmmfChain, TmmfCurrency, TmmfOrderType, TmmfDecimalAmount
from ....types.wallets.earn import (
    tmmf_deposit_params,
    tmmf_register_params,
    tmmf_withdraw_params,
    tmmf_list_positions_params,
)
from ....types.wallets.tmmf_fund import TmmfFund
from ....types.wallets.tmmf_chain import TmmfChain
from ....types.wallet_action_nonce import WalletActionNonce
from ....types.wallets.tmmf_currency import TmmfCurrency
from ....types.wallets.tmmf_order_type import TmmfOrderType
from ....types.wallets.tmmf_decimal_amount import TmmfDecimalAmount
from ....types.wallets.tmmf_provider_param import TmmfProviderParam
from ....types.wallets.tmmf_wallet_response import TmmfWalletResponse
from ....types.wallets.tmmf_position_response import TmmfPositionResponse
from ....types.wallets.tmmf_deposit_action_response import TmmfDepositActionResponse
from ....types.wallets.tmmf_withdraw_action_response import TmmfWithdrawActionResponse

__all__ = ["TmmfResource", "AsyncTmmfResource"]


class TmmfResource(SyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> TmmfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TmmfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TmmfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return TmmfResourceWithStreamingResponse(self)

    def _deposit(
        self,
        wallet_id: str,
        *,
        amount: TmmfDecimalAmount,
        chain: TmmfChain,
        deposit_asset: TmmfCurrency,
        fund: TmmfFund,
        order_type: TmmfOrderType,
        nonce: WalletActionNonce | Omit = omit,
        reference_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfDepositActionResponse:
        """
        Sends `deposit_asset` from the registered wallet to the fund provider and tracks
        delivery of the shares as a wallet action. The wallet owner or signers authorize
        the request.

        Args:
          wallet_id: ID of the wallet.

          amount: A positive decimal amount in the asset's standard unit, e.g. "1000.00".

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          deposit_asset: Currency symbol, e.g. "USDC". Case-insensitive.

          fund: Fund ticker, e.g. "WTGXX". Case-insensitive.

          order_type: How a tMMF order fills: `secondary` from the provider pool in minutes, or
              `primary` at the next NAV strike.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          reference_id: Developer-provided identifier for this request. Must be unique per app.

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
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/deposit", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "chain": chain,
                    "deposit_asset": deposit_asset,
                    "fund": fund,
                    "order_type": order_type,
                    "nonce": nonce,
                    "reference_id": reference_id,
                },
                tmmf_deposit_params.TmmfDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TmmfDepositActionResponse,
        )

    def _withdraw(
        self,
        wallet_id: str,
        *,
        chain: TmmfChain,
        fund: TmmfFund,
        order_type: TmmfOrderType,
        shares: TmmfDecimalAmount,
        withdraw_asset: TmmfCurrency,
        nonce: WalletActionNonce | Omit = omit,
        reference_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfWithdrawActionResponse:
        """
        Sends fund shares from the registered wallet to the fund provider and tracks
        delivery of `withdraw_asset` as a wallet action. The wallet owner or signers
        authorize the request.

        Args:
          wallet_id: ID of the wallet.

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          fund: Fund ticker, e.g. "WTGXX". Case-insensitive.

          order_type: How a tMMF order fills: `secondary` from the provider pool in minutes, or
              `primary` at the next NAV strike.

          shares: A positive decimal amount in the asset's standard unit, e.g. "1000.00".

          withdraw_asset: Currency symbol, e.g. "USDC". Case-insensitive.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          reference_id: Developer-provided identifier for this request. Must be unique per app.

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
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/withdraw", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "chain": chain,
                    "fund": fund,
                    "order_type": order_type,
                    "shares": shares,
                    "withdraw_asset": withdraw_asset,
                    "nonce": nonce,
                    "reference_id": reference_id,
                },
                tmmf_withdraw_params.TmmfWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TmmfWithdrawActionResponse,
        )

    def list_positions(
        self,
        wallet_id: str,
        *,
        chain: TmmfChain | Omit = omit,
        cursor: str | Omit = omit,
        fund: TmmfFund | Omit = omit,
        limit: int | Omit = omit,
        provider: TmmfProviderParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfPositionResponse:
        """
        Returns a page of the wallet's tMMF positions for all providers: shares, their
        USD value at the latest NAV, pending dividends, and pending orders.

        Args:
          wallet_id: ID of the wallet.

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          cursor: Cursor returned by the previous page.

          fund: Fund ticker, e.g. "WTGXX". Case-insensitive.

          provider: The fund provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/positions", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chain": chain,
                        "cursor": cursor,
                        "fund": fund,
                        "limit": limit,
                        "provider": provider,
                    },
                    tmmf_list_positions_params.TmmfListPositionsParams,
                ),
            ),
            cast_to=TmmfPositionResponse,
        )

    def register(
        self,
        wallet_id: str,
        *,
        chain: TmmfChain,
        provider: TmmfProviderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfWalletResponse:
        """Registers the wallet with a tMMF provider on one chain.

        The provider must have
        approved the wallet's user, e.g. an organization; the response reports whether
        it also approved the wallet.

        Args:
          wallet_id: ID of the wallet.

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          provider: The fund provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._post(
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/register", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "chain": chain,
                    "provider": provider,
                },
                tmmf_register_params.TmmfRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TmmfWalletResponse,
        )


class AsyncTmmfResource(AsyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> AsyncTmmfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTmmfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTmmfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncTmmfResourceWithStreamingResponse(self)

    async def _deposit(
        self,
        wallet_id: str,
        *,
        amount: TmmfDecimalAmount,
        chain: TmmfChain,
        deposit_asset: TmmfCurrency,
        fund: TmmfFund,
        order_type: TmmfOrderType,
        nonce: WalletActionNonce | Omit = omit,
        reference_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfDepositActionResponse:
        """
        Sends `deposit_asset` from the registered wallet to the fund provider and tracks
        delivery of the shares as a wallet action. The wallet owner or signers authorize
        the request.

        Args:
          wallet_id: ID of the wallet.

          amount: A positive decimal amount in the asset's standard unit, e.g. "1000.00".

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          deposit_asset: Currency symbol, e.g. "USDC". Case-insensitive.

          fund: Fund ticker, e.g. "WTGXX". Case-insensitive.

          order_type: How a tMMF order fills: `secondary` from the provider pool in minutes, or
              `primary` at the next NAV strike.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          reference_id: Developer-provided identifier for this request. Must be unique per app.

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
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/deposit", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "chain": chain,
                    "deposit_asset": deposit_asset,
                    "fund": fund,
                    "order_type": order_type,
                    "nonce": nonce,
                    "reference_id": reference_id,
                },
                tmmf_deposit_params.TmmfDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TmmfDepositActionResponse,
        )

    async def _withdraw(
        self,
        wallet_id: str,
        *,
        chain: TmmfChain,
        fund: TmmfFund,
        order_type: TmmfOrderType,
        shares: TmmfDecimalAmount,
        withdraw_asset: TmmfCurrency,
        nonce: WalletActionNonce | Omit = omit,
        reference_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfWithdrawActionResponse:
        """
        Sends fund shares from the registered wallet to the fund provider and tracks
        delivery of `withdraw_asset` as a wallet action. The wallet owner or signers
        authorize the request.

        Args:
          wallet_id: ID of the wallet.

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          fund: Fund ticker, e.g. "WTGXX". Case-insensitive.

          order_type: How a tMMF order fills: `secondary` from the provider pool in minutes, or
              `primary` at the next NAV strike.

          shares: A positive decimal amount in the asset's standard unit, e.g. "1000.00".

          withdraw_asset: Currency symbol, e.g. "USDC". Case-insensitive.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          reference_id: Developer-provided identifier for this request. Must be unique per app.

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
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/withdraw", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "chain": chain,
                    "fund": fund,
                    "order_type": order_type,
                    "shares": shares,
                    "withdraw_asset": withdraw_asset,
                    "nonce": nonce,
                    "reference_id": reference_id,
                },
                tmmf_withdraw_params.TmmfWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TmmfWithdrawActionResponse,
        )

    async def list_positions(
        self,
        wallet_id: str,
        *,
        chain: TmmfChain | Omit = omit,
        cursor: str | Omit = omit,
        fund: TmmfFund | Omit = omit,
        limit: int | Omit = omit,
        provider: TmmfProviderParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfPositionResponse:
        """
        Returns a page of the wallet's tMMF positions for all providers: shares, their
        USD value at the latest NAV, pending dividends, and pending orders.

        Args:
          wallet_id: ID of the wallet.

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          cursor: Cursor returned by the previous page.

          fund: Fund ticker, e.g. "WTGXX". Case-insensitive.

          provider: The fund provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/positions", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "chain": chain,
                        "cursor": cursor,
                        "fund": fund,
                        "limit": limit,
                        "provider": provider,
                    },
                    tmmf_list_positions_params.TmmfListPositionsParams,
                ),
            ),
            cast_to=TmmfPositionResponse,
        )

    async def register(
        self,
        wallet_id: str,
        *,
        chain: TmmfChain,
        provider: TmmfProviderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TmmfWalletResponse:
        """Registers the wallet with a tMMF provider on one chain.

        The provider must have
        approved the wallet's user, e.g. an organization; the response reports whether
        it also approved the wallet.

        Args:
          wallet_id: ID of the wallet.

          chain: Chain the fund is held on, e.g. "ethereum_sepolia".

          provider: The fund provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/earn/tmmf/register", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "chain": chain,
                    "provider": provider,
                },
                tmmf_register_params.TmmfRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TmmfWalletResponse,
        )


class TmmfResourceWithRawResponse:
    def __init__(self, tmmf: TmmfResource) -> None:
        self._tmmf = tmmf

        self._deposit = to_raw_response_wrapper(
            tmmf._deposit,
        )
        self._withdraw = to_raw_response_wrapper(
            tmmf._withdraw,
        )
        self.list_positions = to_raw_response_wrapper(
            tmmf.list_positions,
        )
        self.register = to_raw_response_wrapper(
            tmmf.register,
        )


class AsyncTmmfResourceWithRawResponse:
    def __init__(self, tmmf: AsyncTmmfResource) -> None:
        self._tmmf = tmmf

        self._deposit = async_to_raw_response_wrapper(
            tmmf._deposit,
        )
        self._withdraw = async_to_raw_response_wrapper(
            tmmf._withdraw,
        )
        self.list_positions = async_to_raw_response_wrapper(
            tmmf.list_positions,
        )
        self.register = async_to_raw_response_wrapper(
            tmmf.register,
        )


class TmmfResourceWithStreamingResponse:
    def __init__(self, tmmf: TmmfResource) -> None:
        self._tmmf = tmmf

        self._deposit = to_streamed_response_wrapper(
            tmmf._deposit,
        )
        self._withdraw = to_streamed_response_wrapper(
            tmmf._withdraw,
        )
        self.list_positions = to_streamed_response_wrapper(
            tmmf.list_positions,
        )
        self.register = to_streamed_response_wrapper(
            tmmf.register,
        )


class AsyncTmmfResourceWithStreamingResponse:
    def __init__(self, tmmf: AsyncTmmfResource) -> None:
        self._tmmf = tmmf

        self._deposit = async_to_streamed_response_wrapper(
            tmmf._deposit,
        )
        self._withdraw = async_to_streamed_response_wrapper(
            tmmf._withdraw,
        )
        self.list_positions = async_to_streamed_response_wrapper(
            tmmf.list_positions,
        )
        self.register = async_to_streamed_response_wrapper(
            tmmf.register,
        )
