# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    KeyQuorumID,
    wallet_automation_list_params,
    wallet_automation_create_params,
    wallet_automation_update_params,
    wallet_automation_reindex_params,
    wallet_automation_list_executions_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.key_quorum_id import KeyQuorumID
from ..types.wallet_automation_response import WalletAutomationResponse
from ..types.automation_config_input_param import AutomationConfigInputParam
from ..types.wallet_automation_reindex_response import WalletAutomationReindexResponse
from ..types.wallet_automation_success_response import WalletAutomationSuccessResponse
from ..types.wallet_automation_execution_response import WalletAutomationExecutionResponse
from ..types.wallet_automation_reindex_caip_2_param import WalletAutomationReindexCaip2Param

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

    def create(
        self,
        *,
        config: AutomationConfigInputParam,
        owner_id: Optional[str],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationResponse:
        """
        Create a new wallet automation that triggers actions on deposit events.

        Args:
          config: Full configuration for a wallet automation (trigger + action) accepting
              human-readable aliases.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/wallet_automations",
            body=maybe_transform(
                {
                    "config": config,
                    "owner_id": owner_id,
                    "name": name,
                },
                wallet_automation_create_params.WalletAutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationResponse,
        )

    def update(
        self,
        automation_id: str,
        *,
        config: AutomationConfigInputParam | Omit = omit,
        enabled: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        owner_id: Optional[KeyQuorumID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationResponse:
        """
        Update a wallet automation by ID.

        Args:
          automation_id: ID of the wallet automation.

          config: Full configuration for a wallet automation (trigger + action) accepting
              human-readable aliases.

          owner_id: A unique identifier for a key quorum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return self._patch(
            path_template("/v1/wallet_automations/{automation_id}", automation_id=automation_id),
            body=maybe_transform(
                {
                    "config": config,
                    "enabled": enabled,
                    "name": name,
                    "owner_id": owner_id,
                },
                wallet_automation_update_params.WalletAutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[WalletAutomationResponse]:
        """
        List all wallet automations for your app, with optional filtering by wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/wallet_automations",
            page=SyncCursor[WalletAutomationResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "wallet_id": wallet_id,
                    },
                    wallet_automation_list_params.WalletAutomationListParams,
                ),
            ),
            model=WalletAutomationResponse,
        )

    def delete(
        self,
        automation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationSuccessResponse:
        """
        Delete a wallet automation by ID.

        Args:
          automation_id: ID of the wallet automation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return self._delete(
            path_template("/v1/wallet_automations/{automation_id}", automation_id=automation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationSuccessResponse,
        )

    def get(
        self,
        automation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationResponse:
        """
        Get a wallet automation by ID.

        Args:
          automation_id: ID of the wallet automation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return self._get(
            path_template("/v1/wallet_automations/{automation_id}", automation_id=automation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationResponse,
        )

    def list_executions(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[WalletAutomationExecutionResponse]:
        """
        List all wallet automation execution records, with optional filtering by wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/wallet_automations/executions",
            page=SyncCursor[WalletAutomationExecutionResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "wallet_id": wallet_id,
                    },
                    wallet_automation_list_executions_params.WalletAutomationListExecutionsParams,
                ),
            ),
            model=WalletAutomationExecutionResponse,
        )

    def reindex(
        self,
        *,
        asset_address: str,
        caip2: WalletAutomationReindexCaip2Param | Omit = omit,
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

          caip2: An EVM, Solana, or Tron CAIP-2 chain identifier supported by wallet automation
              reindex.

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

    async def create(
        self,
        *,
        config: AutomationConfigInputParam,
        owner_id: Optional[str],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationResponse:
        """
        Create a new wallet automation that triggers actions on deposit events.

        Args:
          config: Full configuration for a wallet automation (trigger + action) accepting
              human-readable aliases.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/wallet_automations",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "owner_id": owner_id,
                    "name": name,
                },
                wallet_automation_create_params.WalletAutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationResponse,
        )

    async def update(
        self,
        automation_id: str,
        *,
        config: AutomationConfigInputParam | Omit = omit,
        enabled: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        owner_id: Optional[KeyQuorumID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationResponse:
        """
        Update a wallet automation by ID.

        Args:
          automation_id: ID of the wallet automation.

          config: Full configuration for a wallet automation (trigger + action) accepting
              human-readable aliases.

          owner_id: A unique identifier for a key quorum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return await self._patch(
            path_template("/v1/wallet_automations/{automation_id}", automation_id=automation_id),
            body=await async_maybe_transform(
                {
                    "config": config,
                    "enabled": enabled,
                    "name": name,
                    "owner_id": owner_id,
                },
                wallet_automation_update_params.WalletAutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WalletAutomationResponse, AsyncCursor[WalletAutomationResponse]]:
        """
        List all wallet automations for your app, with optional filtering by wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/wallet_automations",
            page=AsyncCursor[WalletAutomationResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "wallet_id": wallet_id,
                    },
                    wallet_automation_list_params.WalletAutomationListParams,
                ),
            ),
            model=WalletAutomationResponse,
        )

    async def delete(
        self,
        automation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationSuccessResponse:
        """
        Delete a wallet automation by ID.

        Args:
          automation_id: ID of the wallet automation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return await self._delete(
            path_template("/v1/wallet_automations/{automation_id}", automation_id=automation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationSuccessResponse,
        )

    async def get(
        self,
        automation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAutomationResponse:
        """
        Get a wallet automation by ID.

        Args:
          automation_id: ID of the wallet automation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return await self._get(
            path_template("/v1/wallet_automations/{automation_id}", automation_id=automation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletAutomationResponse,
        )

    def list_executions(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WalletAutomationExecutionResponse, AsyncCursor[WalletAutomationExecutionResponse]]:
        """
        List all wallet automation execution records, with optional filtering by wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/wallet_automations/executions",
            page=AsyncCursor[WalletAutomationExecutionResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "wallet_id": wallet_id,
                    },
                    wallet_automation_list_executions_params.WalletAutomationListExecutionsParams,
                ),
            ),
            model=WalletAutomationExecutionResponse,
        )

    async def reindex(
        self,
        *,
        asset_address: str,
        caip2: WalletAutomationReindexCaip2Param | Omit = omit,
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

          caip2: An EVM, Solana, or Tron CAIP-2 chain identifier supported by wallet automation
              reindex.

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

        self.create = to_raw_response_wrapper(
            wallet_automations.create,
        )
        self.update = to_raw_response_wrapper(
            wallet_automations.update,
        )
        self.list = to_raw_response_wrapper(
            wallet_automations.list,
        )
        self.delete = to_raw_response_wrapper(
            wallet_automations.delete,
        )
        self.get = to_raw_response_wrapper(
            wallet_automations.get,
        )
        self.list_executions = to_raw_response_wrapper(
            wallet_automations.list_executions,
        )
        self.reindex = to_raw_response_wrapper(
            wallet_automations.reindex,
        )


class AsyncWalletAutomationsResourceWithRawResponse:
    def __init__(self, wallet_automations: AsyncWalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.create = async_to_raw_response_wrapper(
            wallet_automations.create,
        )
        self.update = async_to_raw_response_wrapper(
            wallet_automations.update,
        )
        self.list = async_to_raw_response_wrapper(
            wallet_automations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            wallet_automations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            wallet_automations.get,
        )
        self.list_executions = async_to_raw_response_wrapper(
            wallet_automations.list_executions,
        )
        self.reindex = async_to_raw_response_wrapper(
            wallet_automations.reindex,
        )


class WalletAutomationsResourceWithStreamingResponse:
    def __init__(self, wallet_automations: WalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.create = to_streamed_response_wrapper(
            wallet_automations.create,
        )
        self.update = to_streamed_response_wrapper(
            wallet_automations.update,
        )
        self.list = to_streamed_response_wrapper(
            wallet_automations.list,
        )
        self.delete = to_streamed_response_wrapper(
            wallet_automations.delete,
        )
        self.get = to_streamed_response_wrapper(
            wallet_automations.get,
        )
        self.list_executions = to_streamed_response_wrapper(
            wallet_automations.list_executions,
        )
        self.reindex = to_streamed_response_wrapper(
            wallet_automations.reindex,
        )


class AsyncWalletAutomationsResourceWithStreamingResponse:
    def __init__(self, wallet_automations: AsyncWalletAutomationsResource) -> None:
        self._wallet_automations = wallet_automations

        self.create = async_to_streamed_response_wrapper(
            wallet_automations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            wallet_automations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            wallet_automations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            wallet_automations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            wallet_automations.get,
        )
        self.list_executions = async_to_streamed_response_wrapper(
            wallet_automations.list_executions,
        )
        self.reindex = async_to_streamed_response_wrapper(
            wallet_automations.reindex,
        )
