# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.wallets import WalletActionInclude, action_get_params
from ...types.wallets.wallet_action_include import WalletActionInclude
from ...types.wallets.wallet_action_response import WalletActionResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def get(
        self,
        action_id: str,
        *,
        wallet_id: str,
        include: WalletActionInclude | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletActionResponse:
        """Get the current status of a wallet action by its ID.

        Use `?include=steps` to
        include step-level details.

        Args:
          wallet_id: ID of the wallet.

          action_id: ID of the wallet action.

          include: Expandable relations to include on a wallet action response.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return cast(
            WalletActionResponse,
            self._get(
                path_template("/v1/wallets/{wallet_id}/actions/{action_id}", wallet_id=wallet_id, action_id=action_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"include": include}, action_get_params.ActionGetParams),
                ),
                cast_to=cast(
                    Any, WalletActionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncActionsResource(AsyncAPIResource):
    """Operations related to wallet actions"""

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def get(
        self,
        action_id: str,
        *,
        wallet_id: str,
        include: WalletActionInclude | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletActionResponse:
        """Get the current status of a wallet action by its ID.

        Use `?include=steps` to
        include step-level details.

        Args:
          wallet_id: ID of the wallet.

          action_id: ID of the wallet action.

          include: Expandable relations to include on a wallet action response.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return cast(
            WalletActionResponse,
            await self._get(
                path_template("/v1/wallets/{wallet_id}/actions/{action_id}", wallet_id=wallet_id, action_id=action_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"include": include}, action_get_params.ActionGetParams),
                ),
                cast_to=cast(
                    Any, WalletActionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.get = to_raw_response_wrapper(
            actions.get,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.get = async_to_raw_response_wrapper(
            actions.get,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.get = to_streamed_response_wrapper(
            actions.get,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.get = async_to_streamed_response_wrapper(
            actions.get,
        )
