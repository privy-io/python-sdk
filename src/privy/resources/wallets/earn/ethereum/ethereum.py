# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from .....types import WalletActionNonce
from .incentive import (
    IncentiveResource,
    AsyncIncentiveResource,
    IncentiveResourceWithRawResponse,
    AsyncIncentiveResourceWithRawResponse,
    IncentiveResourceWithStreamingResponse,
    AsyncIncentiveResourceWithStreamingResponse,
)
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
from .....types.wallets.earn import ethereum_deposit_params, ethereum_withdraw_params, ethereum_vault_position_params
from .....types.wallet_action_nonce import WalletActionNonce
from .....types.wallets.earn_deposit_action_response import EarnDepositActionResponse
from .....types.wallets.earn_withdraw_action_response import EarnWithdrawActionResponse
from .....types.wallets.ethereum_earn_position_response import EthereumEarnPositionResponse
from .....types.wallets.ethereum_earn_vault_details_response import EthereumEarnVaultDetailsResponse

__all__ = ["EthereumResource", "AsyncEthereumResource"]


class EthereumResource(SyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def incentive(self) -> IncentiveResource:
        """Operations related to wallet actions"""
        return IncentiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> EthereumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EthereumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EthereumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return EthereumResourceWithStreamingResponse(self)

    def _deposit(
        self,
        wallet_id: str,
        *,
        vault_id: str,
        amount: str | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        raw_amount: str | Omit = omit,
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
    ) -> EarnDepositActionResponse:
        """
        Deposit assets into an ERC-4626 vault.

        Args:
          wallet_id: ID of the wallet.

          vault_id: The ID of the vault to deposit into.

          amount: Human-readable decimal amount to deposit (e.g. "1.5" for 1.5 USDC). Exactly one
              of `amount` or `raw_amount` must be provided.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          raw_amount: Amount in smallest unit to deposit (e.g. "1500000" for 1.5 USDC with 6
              decimals). Exactly one of `amount` or `raw_amount` must be provided.

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
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/deposit", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "vault_id": vault_id,
                    "amount": amount,
                    "nonce": nonce,
                    "raw_amount": raw_amount,
                    "reference_id": reference_id,
                },
                ethereum_deposit_params.EthereumDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarnDepositActionResponse,
        )

    def _withdraw(
        self,
        wallet_id: str,
        *,
        vault_id: str,
        amount: str | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        raw_amount: str | Omit = omit,
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
    ) -> EarnWithdrawActionResponse:
        """
        Withdraw assets from an ERC-4626 vault.

        Args:
          wallet_id: ID of the wallet.

          vault_id: The ID of the vault to withdraw from.

          amount: Human-readable decimal amount to withdraw (e.g. "1.5" for 1.5 USDC). Exactly one
              of `amount` or `raw_amount` must be provided.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          raw_amount: Amount in smallest unit to withdraw (e.g. "1500000" for 1.5 USDC with 6
              decimals). Exactly one of `amount` or `raw_amount` must be provided.

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
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/withdraw", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "vault_id": vault_id,
                    "amount": amount,
                    "nonce": nonce,
                    "raw_amount": raw_amount,
                    "reference_id": reference_id,
                },
                ethereum_withdraw_params.EthereumWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarnWithdrawActionResponse,
        )

    def vault_details(
        self,
        vault_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EthereumEarnVaultDetailsResponse:
        """
        Retrieve detailed information about an earn vault, including current APY and
        liquidity.

        Args:
          vault_id: The Privy vault ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vault_id:
            raise ValueError(f"Expected a non-empty value for `vault_id` but received {vault_id!r}")
        return cast(
            EthereumEarnVaultDetailsResponse,
            self._get(
                path_template("/v1/earn/ethereum/vaults/{vault_id}", vault_id=vault_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EthereumEarnVaultDetailsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def vault_position(
        self,
        wallet_id: str,
        *,
        vault_id: str,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EthereumEarnPositionResponse:
        """
        Retrieve a wallet's current position in a specific earn vault, including
        deposit/withdraw totals and current onchain vault shares.

        Args:
          wallet_id: ID of the wallet.

          vault_id: The vault ID to get position for.

          include_archived: Include archived wallets in lookup. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/vaults", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "vault_id": vault_id,
                        "include_archived": include_archived,
                    },
                    ethereum_vault_position_params.EthereumVaultPositionParams,
                ),
            ),
            cast_to=EthereumEarnPositionResponse,
        )


class AsyncEthereumResource(AsyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def incentive(self) -> AsyncIncentiveResource:
        """Operations related to wallet actions"""
        return AsyncIncentiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEthereumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEthereumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEthereumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncEthereumResourceWithStreamingResponse(self)

    async def _deposit(
        self,
        wallet_id: str,
        *,
        vault_id: str,
        amount: str | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        raw_amount: str | Omit = omit,
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
    ) -> EarnDepositActionResponse:
        """
        Deposit assets into an ERC-4626 vault.

        Args:
          wallet_id: ID of the wallet.

          vault_id: The ID of the vault to deposit into.

          amount: Human-readable decimal amount to deposit (e.g. "1.5" for 1.5 USDC). Exactly one
              of `amount` or `raw_amount` must be provided.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          raw_amount: Amount in smallest unit to deposit (e.g. "1500000" for 1.5 USDC with 6
              decimals). Exactly one of `amount` or `raw_amount` must be provided.

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
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/deposit", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "vault_id": vault_id,
                    "amount": amount,
                    "nonce": nonce,
                    "raw_amount": raw_amount,
                    "reference_id": reference_id,
                },
                ethereum_deposit_params.EthereumDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarnDepositActionResponse,
        )

    async def _withdraw(
        self,
        wallet_id: str,
        *,
        vault_id: str,
        amount: str | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        raw_amount: str | Omit = omit,
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
    ) -> EarnWithdrawActionResponse:
        """
        Withdraw assets from an ERC-4626 vault.

        Args:
          wallet_id: ID of the wallet.

          vault_id: The ID of the vault to withdraw from.

          amount: Human-readable decimal amount to withdraw (e.g. "1.5" for 1.5 USDC). Exactly one
              of `amount` or `raw_amount` must be provided.

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          raw_amount: Amount in smallest unit to withdraw (e.g. "1500000" for 1.5 USDC with 6
              decimals). Exactly one of `amount` or `raw_amount` must be provided.

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
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/withdraw", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "vault_id": vault_id,
                    "amount": amount,
                    "nonce": nonce,
                    "raw_amount": raw_amount,
                    "reference_id": reference_id,
                },
                ethereum_withdraw_params.EthereumWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EarnWithdrawActionResponse,
        )

    async def vault_details(
        self,
        vault_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EthereumEarnVaultDetailsResponse:
        """
        Retrieve detailed information about an earn vault, including current APY and
        liquidity.

        Args:
          vault_id: The Privy vault ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vault_id:
            raise ValueError(f"Expected a non-empty value for `vault_id` but received {vault_id!r}")
        return cast(
            EthereumEarnVaultDetailsResponse,
            await self._get(
                path_template("/v1/earn/ethereum/vaults/{vault_id}", vault_id=vault_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EthereumEarnVaultDetailsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def vault_position(
        self,
        wallet_id: str,
        *,
        vault_id: str,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EthereumEarnPositionResponse:
        """
        Retrieve a wallet's current position in a specific earn vault, including
        deposit/withdraw totals and current onchain vault shares.

        Args:
          wallet_id: ID of the wallet.

          vault_id: The vault ID to get position for.

          include_archived: Include archived wallets in lookup. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}/earn/ethereum/vaults", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "vault_id": vault_id,
                        "include_archived": include_archived,
                    },
                    ethereum_vault_position_params.EthereumVaultPositionParams,
                ),
            ),
            cast_to=EthereumEarnPositionResponse,
        )


class EthereumResourceWithRawResponse:
    def __init__(self, ethereum: EthereumResource) -> None:
        self._ethereum = ethereum

        self._deposit = to_raw_response_wrapper(
            ethereum._deposit,
        )
        self._withdraw = to_raw_response_wrapper(
            ethereum._withdraw,
        )
        self.vault_details = to_raw_response_wrapper(
            ethereum.vault_details,
        )
        self.vault_position = to_raw_response_wrapper(
            ethereum.vault_position,
        )

    @cached_property
    def incentive(self) -> IncentiveResourceWithRawResponse:
        """Operations related to wallet actions"""
        return IncentiveResourceWithRawResponse(self._ethereum.incentive)


class AsyncEthereumResourceWithRawResponse:
    def __init__(self, ethereum: AsyncEthereumResource) -> None:
        self._ethereum = ethereum

        self._deposit = async_to_raw_response_wrapper(
            ethereum._deposit,
        )
        self._withdraw = async_to_raw_response_wrapper(
            ethereum._withdraw,
        )
        self.vault_details = async_to_raw_response_wrapper(
            ethereum.vault_details,
        )
        self.vault_position = async_to_raw_response_wrapper(
            ethereum.vault_position,
        )

    @cached_property
    def incentive(self) -> AsyncIncentiveResourceWithRawResponse:
        """Operations related to wallet actions"""
        return AsyncIncentiveResourceWithRawResponse(self._ethereum.incentive)


class EthereumResourceWithStreamingResponse:
    def __init__(self, ethereum: EthereumResource) -> None:
        self._ethereum = ethereum

        self._deposit = to_streamed_response_wrapper(
            ethereum._deposit,
        )
        self._withdraw = to_streamed_response_wrapper(
            ethereum._withdraw,
        )
        self.vault_details = to_streamed_response_wrapper(
            ethereum.vault_details,
        )
        self.vault_position = to_streamed_response_wrapper(
            ethereum.vault_position,
        )

    @cached_property
    def incentive(self) -> IncentiveResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return IncentiveResourceWithStreamingResponse(self._ethereum.incentive)


class AsyncEthereumResourceWithStreamingResponse:
    def __init__(self, ethereum: AsyncEthereumResource) -> None:
        self._ethereum = ethereum

        self._deposit = async_to_streamed_response_wrapper(
            ethereum._deposit,
        )
        self._withdraw = async_to_streamed_response_wrapper(
            ethereum._withdraw,
        )
        self.vault_details = async_to_streamed_response_wrapper(
            ethereum.vault_details,
        )
        self.vault_position = async_to_streamed_response_wrapper(
            ethereum.vault_position,
        )

    @cached_property
    def incentive(self) -> AsyncIncentiveResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return AsyncIncentiveResourceWithStreamingResponse(self._ethereum.incentive)
