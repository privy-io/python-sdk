# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.wallets.deposit_accounts import crypto_create_params
from ....types.automation_asset_filter_input_param import AutomationAssetFilterInputParam
from ....types.create_crypto_deposit_account_response import CreateCryptoDepositAccountResponse
from ....types.automation_destination_asset_input_param import AutomationDestinationAssetInputParam

__all__ = ["CryptoResource", "AsyncCryptoResource"]


class CryptoResource(SyncAPIResource):
    """Operations related to wallets"""

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

    @overload
    def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str,
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
        """Creates deposit source wallets and attaches them to a sweep into the path
        wallet.

        Requires a dest-owner privy-authorization-signature. Accepts a
        dest-owner user JWT or an app secret (app-secret callers use the dest owner).
        JWT-only requests 401 when the app requires an app secret for wallet actions.

        Args:
          wallet_id: ID of the wallet.

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
        destination: AutomationDestinationAssetInputParam,
        source: AutomationAssetFilterInputParam,
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
        """Creates deposit source wallets and attaches them to a sweep into the path
        wallet.

        Requires a dest-owner privy-authorization-signature. Accepts a
        dest-owner user JWT or an app secret (app-secret callers use the dest owner).
        JWT-only requests 401 when the app requires an app secret for wallet actions.

        Args:
          wallet_id: ID of the wallet.

          destination: A destination asset spec accepting either raw identifiers (asset_address, caip2)
              or human-readable aliases (asset, chain). Exactly one of asset_address or asset
              must be provided; exactly one of caip2 or chain must be provided.

          source: Which assets to include/exclude for an automation trigger (input form with alias
              support).

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

    @required_args(["deposit_config_id"], ["destination", "source"])
    def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        destination: AutomationDestinationAssetInputParam | Omit = omit,
        source: AutomationAssetFilterInputParam | Omit = omit,
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


class AsyncCryptoResource(AsyncAPIResource):
    """Operations related to wallets"""

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

    @overload
    async def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str,
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
        """Creates deposit source wallets and attaches them to a sweep into the path
        wallet.

        Requires a dest-owner privy-authorization-signature. Accepts a
        dest-owner user JWT or an app secret (app-secret callers use the dest owner).
        JWT-only requests 401 when the app requires an app secret for wallet actions.

        Args:
          wallet_id: ID of the wallet.

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
        destination: AutomationDestinationAssetInputParam,
        source: AutomationAssetFilterInputParam,
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
        """Creates deposit source wallets and attaches them to a sweep into the path
        wallet.

        Requires a dest-owner privy-authorization-signature. Accepts a
        dest-owner user JWT or an app secret (app-secret callers use the dest owner).
        JWT-only requests 401 when the app requires an app secret for wallet actions.

        Args:
          wallet_id: ID of the wallet.

          destination: A destination asset spec accepting either raw identifiers (asset_address, caip2)
              or human-readable aliases (asset, chain). Exactly one of asset_address or asset
              must be provided; exactly one of caip2 or chain must be provided.

          source: Which assets to include/exclude for an automation trigger (input form with alias
              support).

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

    @required_args(["deposit_config_id"], ["destination", "source"])
    async def _create(
        self,
        wallet_id: str,
        *,
        deposit_config_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        destination: AutomationDestinationAssetInputParam | Omit = omit,
        source: AutomationAssetFilterInputParam | Omit = omit,
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


class CryptoResourceWithRawResponse:
    def __init__(self, crypto: CryptoResource) -> None:
        self._crypto = crypto

        self._create = to_raw_response_wrapper(
            crypto._create,
        )


class AsyncCryptoResourceWithRawResponse:
    def __init__(self, crypto: AsyncCryptoResource) -> None:
        self._crypto = crypto

        self._create = async_to_raw_response_wrapper(
            crypto._create,
        )


class CryptoResourceWithStreamingResponse:
    def __init__(self, crypto: CryptoResource) -> None:
        self._crypto = crypto

        self._create = to_streamed_response_wrapper(
            crypto._create,
        )


class AsyncCryptoResourceWithStreamingResponse:
    def __init__(self, crypto: AsyncCryptoResource) -> None:
        self._crypto = crypto

        self._create = async_to_streamed_response_wrapper(
            crypto._create,
        )
