# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from .....types import (
    Bps,
    CryptoDepositAddressStrategy,
    DepositAccountCryptoQuoteAmount,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....types.bps import Bps
from .....pagination import SyncCursor, AsyncCursor
from ....._base_client import AsyncPaginator, make_request_options
from .....types.wallets.deposit_accounts import (
    crypto_list_params,
    crypto_quote_params,
    crypto_create_params,
    crypto_get_next_order_params,
)
from .....types.crypto_deposit_asset_param import CryptoDepositAssetParam
from .....types.crypto_deposit_address_route import CryptoDepositAddressRoute
from .....types.crypto_deposit_address_strategy import CryptoDepositAddressStrategy
from .....types.crypto_deposit_asset_filter_param import CryptoDepositAssetFilterParam
from .....types.deposit_account_crypto_quote_amount import DepositAccountCryptoQuoteAmount
from .....types.deposit_account_crypto_quote_response import DepositAccountCryptoQuoteResponse
from .....types.create_crypto_deposit_account_response import CreateCryptoDepositAccountResponse
from .....types.crypto_deposit_account_config_response import CryptoDepositAccountConfigResponse
from .....types.deposit_account_crypto_quote_asset_param import DepositAccountCryptoQuoteAssetParam
from .....types.get_crypto_deposit_account_next_order_response import GetCryptoDepositAccountNextOrderResponse

__all__ = ["CryptoResource", "AsyncCryptoResource"]


class CryptoResource(SyncAPIResource):
    """Operations related to wallets"""

    @cached_property
    def orders(self) -> OrdersResource:
        """Operations related to wallets"""
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> CryptoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return CryptoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CryptoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return CryptoResourceWithStreamingResponse(self)

    def list(
        self,
        wallet_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[CryptoDepositAddressRoute]:
        """Returns active crypto deposit accounts that sweep into the path wallet.

        Requires
        an app secret or a JWT for a wallet signer, plus `privy-app-id`.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get_api_list(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/crypto", wallet_id=wallet_id),
            page=SyncCursor[CryptoDepositAddressRoute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    crypto_list_params.CryptoListParams,
                ),
            ),
            model=CryptoDepositAddressRoute,
        )

    @overload
    def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str,
        type: Literal["deposit_config"],
        deposit_address_strategy: CryptoDepositAddressStrategy | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCryptoDepositAccountResponse:
        """
        Creates deposit source wallets that sweep into the path wallet.

        Args:
          wallet_id: ID of the wallet.

          deposit_address_strategy: How deposit source wallets are chosen. Omission uses `dedicated`. Destination
              reuse applies only to the destination's own chain type.

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
        ...

    @overload
    def _create(
        self,
        wallet_id: str,
        *,
        destination: CryptoDepositAssetParam,
        source: CryptoDepositAssetFilterParam,
        type: Literal["inline_route"],
        deposit_address_strategy: CryptoDepositAddressStrategy | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCryptoDepositAccountResponse:
        """
        Creates deposit source wallets that sweep into the path wallet.

        Args:
          wallet_id: ID of the wallet.

          destination: An asset on a chain. Uses a human-readable alias (usdc, tempo) when one is on
              file, otherwise the raw asset address and CAIP-2.

          source: Which assets a deposit address accepts. Asset and chain use human-readable
              aliases when known.

          deposit_address_strategy: How deposit source wallets are chosen. Omission uses `dedicated`. Destination
              reuse applies only to the destination's own chain type.

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
        ...

    @required_args(["deposit_config_id", "type"], ["destination", "source", "type"])
    def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str | Omit = omit,
        type: Literal["deposit_config"] | Literal["inline_route"],
        deposit_address_strategy: CryptoDepositAddressStrategy | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        destination: CryptoDepositAssetParam | Omit = omit,
        source: CryptoDepositAssetFilterParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCryptoDepositAccountResponse:
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
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/crypto", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "deposit_config_id": deposit_config_id,
                    "type": type,
                    "deposit_address_strategy": deposit_address_strategy,
                    "destination": destination,
                    "source": source,
                },
                crypto_create_params.CryptoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateCryptoDepositAccountResponse,
        )

    def get_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoDepositAccountConfigResponse:
        """
        Returns the tokens and chains a user can send from when creating a crypto
        deposit account.
        """
        return self._get(
            "/v1/deposit_accounts/crypto/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CryptoDepositAccountConfigResponse,
        )

    def get_next_order(
        self,
        wallet_id: str,
        *,
        after: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetCryptoDepositAccountNextOrderResponse:
        """
        Fetch the earliest crypto deposit-account sweep into the path wallet after
        `after`. Returns `{order: {id, status} | null}` — the same order object as GET
        order. The path wallet is the destination (same as create). Accepts an app
        secret or a user / wallet-signer JWT (`privy-app-id`).

        Args:
          wallet_id: ID of the wallet.

          after: Return the earliest sweep strictly after this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/crypto/next_order", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"after": after}, crypto_get_next_order_params.CryptoGetNextOrderParams),
            ),
            cast_to=GetCryptoDepositAccountNextOrderResponse,
        )

    def quote(
        self,
        *,
        destination: DepositAccountCryptoQuoteAssetParam,
        source: DepositAccountCryptoQuoteAssetParam,
        input_amount: DepositAccountCryptoQuoteAmount | Omit = omit,
        slippage_bps: Bps | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DepositAccountCryptoQuoteResponse:
        """Returns an indicative route quote without creating a wallet.

        Amounts use token
        standard units. Accepts an app secret or user token.

        Args:
          destination: An asset and chain for an indicative crypto deposit-account quote.

          source: An asset and chain for an indicative crypto deposit-account quote.

          input_amount: A positive decimal amount in the source token’s standard unit, not its smallest
              on-chain unit.

          slippage_bps: Value in basis points: integer from 0 to 10000 (0% to 100%).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/deposit_accounts/crypto/quote",
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                    "input_amount": input_amount,
                    "slippage_bps": slippage_bps,
                },
                crypto_quote_params.CryptoQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositAccountCryptoQuoteResponse,
        )


class AsyncCryptoResource(AsyncAPIResource):
    """Operations related to wallets"""

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        """Operations related to wallets"""
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCryptoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCryptoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCryptoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncCryptoResourceWithStreamingResponse(self)

    def list(
        self,
        wallet_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CryptoDepositAddressRoute, AsyncCursor[CryptoDepositAddressRoute]]:
        """Returns active crypto deposit accounts that sweep into the path wallet.

        Requires
        an app secret or a JWT for a wallet signer, plus `privy-app-id`.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get_api_list(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/crypto", wallet_id=wallet_id),
            page=AsyncCursor[CryptoDepositAddressRoute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    crypto_list_params.CryptoListParams,
                ),
            ),
            model=CryptoDepositAddressRoute,
        )

    @overload
    async def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str,
        type: Literal["deposit_config"],
        deposit_address_strategy: CryptoDepositAddressStrategy | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCryptoDepositAccountResponse:
        """
        Creates deposit source wallets that sweep into the path wallet.

        Args:
          wallet_id: ID of the wallet.

          deposit_address_strategy: How deposit source wallets are chosen. Omission uses `dedicated`. Destination
              reuse applies only to the destination's own chain type.

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
        ...

    @overload
    async def _create(
        self,
        wallet_id: str,
        *,
        destination: CryptoDepositAssetParam,
        source: CryptoDepositAssetFilterParam,
        type: Literal["inline_route"],
        deposit_address_strategy: CryptoDepositAddressStrategy | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCryptoDepositAccountResponse:
        """
        Creates deposit source wallets that sweep into the path wallet.

        Args:
          wallet_id: ID of the wallet.

          destination: An asset on a chain. Uses a human-readable alias (usdc, tempo) when one is on
              file, otherwise the raw asset address and CAIP-2.

          source: Which assets a deposit address accepts. Asset and chain use human-readable
              aliases when known.

          deposit_address_strategy: How deposit source wallets are chosen. Omission uses `dedicated`. Destination
              reuse applies only to the destination's own chain type.

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
        ...

    @required_args(["deposit_config_id", "type"], ["destination", "source", "type"])
    async def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str | Omit = omit,
        type: Literal["deposit_config"] | Literal["inline_route"],
        deposit_address_strategy: CryptoDepositAddressStrategy | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        destination: CryptoDepositAssetParam | Omit = omit,
        source: CryptoDepositAssetFilterParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCryptoDepositAccountResponse:
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
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/crypto", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "deposit_config_id": deposit_config_id,
                    "type": type,
                    "deposit_address_strategy": deposit_address_strategy,
                    "destination": destination,
                    "source": source,
                },
                crypto_create_params.CryptoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateCryptoDepositAccountResponse,
        )

    async def get_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoDepositAccountConfigResponse:
        """
        Returns the tokens and chains a user can send from when creating a crypto
        deposit account.
        """
        return await self._get(
            "/v1/deposit_accounts/crypto/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CryptoDepositAccountConfigResponse,
        )

    async def get_next_order(
        self,
        wallet_id: str,
        *,
        after: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetCryptoDepositAccountNextOrderResponse:
        """
        Fetch the earliest crypto deposit-account sweep into the path wallet after
        `after`. Returns `{order: {id, status} | null}` — the same order object as GET
        order. The path wallet is the destination (same as create). Accepts an app
        secret or a user / wallet-signer JWT (`privy-app-id`).

        Args:
          wallet_id: ID of the wallet.

          after: Return the earliest sweep strictly after this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}/deposit_accounts/crypto/next_order", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"after": after}, crypto_get_next_order_params.CryptoGetNextOrderParams
                ),
            ),
            cast_to=GetCryptoDepositAccountNextOrderResponse,
        )

    async def quote(
        self,
        *,
        destination: DepositAccountCryptoQuoteAssetParam,
        source: DepositAccountCryptoQuoteAssetParam,
        input_amount: DepositAccountCryptoQuoteAmount | Omit = omit,
        slippage_bps: Bps | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DepositAccountCryptoQuoteResponse:
        """Returns an indicative route quote without creating a wallet.

        Amounts use token
        standard units. Accepts an app secret or user token.

        Args:
          destination: An asset and chain for an indicative crypto deposit-account quote.

          source: An asset and chain for an indicative crypto deposit-account quote.

          input_amount: A positive decimal amount in the source token’s standard unit, not its smallest
              on-chain unit.

          slippage_bps: Value in basis points: integer from 0 to 10000 (0% to 100%).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/deposit_accounts/crypto/quote",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                    "input_amount": input_amount,
                    "slippage_bps": slippage_bps,
                },
                crypto_quote_params.CryptoQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositAccountCryptoQuoteResponse,
        )


class CryptoResourceWithRawResponse:
    def __init__(self, crypto: CryptoResource) -> None:
        self._crypto = crypto

        self.list = to_raw_response_wrapper(
            crypto.list,
        )
        self._create = to_raw_response_wrapper(
            crypto._create,
        )
        self.get_config = to_raw_response_wrapper(
            crypto.get_config,
        )
        self.get_next_order = to_raw_response_wrapper(
            crypto.get_next_order,
        )
        self.quote = to_raw_response_wrapper(
            crypto.quote,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        """Operations related to wallets"""
        return OrdersResourceWithRawResponse(self._crypto.orders)


class AsyncCryptoResourceWithRawResponse:
    def __init__(self, crypto: AsyncCryptoResource) -> None:
        self._crypto = crypto

        self.list = async_to_raw_response_wrapper(
            crypto.list,
        )
        self._create = async_to_raw_response_wrapper(
            crypto._create,
        )
        self.get_config = async_to_raw_response_wrapper(
            crypto.get_config,
        )
        self.get_next_order = async_to_raw_response_wrapper(
            crypto.get_next_order,
        )
        self.quote = async_to_raw_response_wrapper(
            crypto.quote,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        """Operations related to wallets"""
        return AsyncOrdersResourceWithRawResponse(self._crypto.orders)


class CryptoResourceWithStreamingResponse:
    def __init__(self, crypto: CryptoResource) -> None:
        self._crypto = crypto

        self.list = to_streamed_response_wrapper(
            crypto.list,
        )
        self._create = to_streamed_response_wrapper(
            crypto._create,
        )
        self.get_config = to_streamed_response_wrapper(
            crypto.get_config,
        )
        self.get_next_order = to_streamed_response_wrapper(
            crypto.get_next_order,
        )
        self.quote = to_streamed_response_wrapper(
            crypto.quote,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        """Operations related to wallets"""
        return OrdersResourceWithStreamingResponse(self._crypto.orders)


class AsyncCryptoResourceWithStreamingResponse:
    def __init__(self, crypto: AsyncCryptoResource) -> None:
        self._crypto = crypto

        self.list = async_to_streamed_response_wrapper(
            crypto.list,
        )
        self._create = async_to_streamed_response_wrapper(
            crypto._create,
        )
        self.get_config = async_to_streamed_response_wrapper(
            crypto.get_config,
        )
        self.get_next_order = async_to_streamed_response_wrapper(
            crypto.get_next_order,
        )
        self.quote = async_to_streamed_response_wrapper(
            crypto.quote,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        """Operations related to wallets"""
        return AsyncOrdersResourceWithStreamingResponse(self._crypto.orders)
