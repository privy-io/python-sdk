# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .kyc import (
    KYCResource,
    AsyncKYCResource,
    KYCResourceWithRawResponse,
    AsyncKYCResourceWithRawResponse,
    KYCResourceWithStreamingResponse,
    AsyncKYCResourceWithStreamingResponse,
)
from .onramp import (
    OnrampResource,
    AsyncOnrampResource,
    OnrampResourceWithRawResponse,
    AsyncOnrampResourceWithRawResponse,
    OnrampResourceWithStreamingResponse,
    AsyncOnrampResourceWithStreamingResponse,
)
from ...types import OnrampProvider, fiat_get_status_params, fiat_get_kyc_link_params, fiat_configure_app_params
from .offramp import (
    OfframpResource,
    AsyncOfframpResource,
    OfframpResourceWithRawResponse,
    AsyncOfframpResourceWithRawResponse,
    OfframpResourceWithStreamingResponse,
    AsyncOfframpResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.onramp_provider import OnrampProvider
from ...types.success_response import SuccessResponse
from ...types.fiat_get_status_response import FiatGetStatusResponse
from ...types.fiat_get_kyc_link_response import FiatGetKYCLinkResponse

__all__ = ["FiatResource", "AsyncFiatResource"]


class FiatResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def accounts(self) -> AccountsResource:
        """Operations related to fiat onramping and offramping"""
        return AccountsResource(self._client)

    @cached_property
    def kyc(self) -> KYCResource:
        """Operations related to fiat onramping and offramping"""
        return KYCResource(self._client)

    @cached_property
    def onramp(self) -> OnrampResource:
        """Operations related to fiat onramping and offramping"""
        return OnrampResource(self._client)

    @cached_property
    def offramp(self) -> OfframpResource:
        """Operations related to fiat onramping and offramping"""
        return OfframpResource(self._client)

    @cached_property
    def with_raw_response(self) -> FiatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FiatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return FiatResourceWithStreamingResponse(self)

    def configure_app(
        self,
        app_id: str,
        *,
        api_key: str,
        provider: OnrampProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """Updates the app configuration for the specified onramp provider.

        This is used to
        set up the app for fiat onramping and offramping.

        Args:
          app_id: The ID of the app that is being configured for fiat onramping and offramping

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            path_template("/v1/apps/{app_id}/fiat", app_id=app_id),
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "provider": provider,
                },
                fiat_configure_app_params.FiatConfigureAppParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def get_kyc_link(
        self,
        user_id: str,
        *,
        email: str,
        provider: OnrampProvider,
        endorsements: List[Literal["sepa"]] | Omit = omit,
        full_name: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        type: Literal["individual", "business"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatGetKYCLinkResponse:
        """
        Returns a KYC link for a user

        Args:
          user_id: The ID of the user

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/fiat/kyc_link", user_id=user_id),
            body=maybe_transform(
                {
                    "email": email,
                    "provider": provider,
                    "endorsements": endorsements,
                    "full_name": full_name,
                    "redirect_uri": redirect_uri,
                    "type": type,
                },
                fiat_get_kyc_link_params.FiatGetKYCLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatGetKYCLinkResponse,
        )

    def get_status(
        self,
        user_id: str,
        *,
        provider: OnrampProvider,
        tx_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatGetStatusResponse:
        """
        Returns a list of fiat transactions and their statuses

        Args:
          user_id: The ID of the user

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/fiat/status", user_id=user_id),
            body=maybe_transform(
                {
                    "provider": provider,
                    "tx_hash": tx_hash,
                },
                fiat_get_status_params.FiatGetStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatGetStatusResponse,
        )


class AsyncFiatResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Operations related to fiat onramping and offramping"""
        return AsyncAccountsResource(self._client)

    @cached_property
    def kyc(self) -> AsyncKYCResource:
        """Operations related to fiat onramping and offramping"""
        return AsyncKYCResource(self._client)

    @cached_property
    def onramp(self) -> AsyncOnrampResource:
        """Operations related to fiat onramping and offramping"""
        return AsyncOnrampResource(self._client)

    @cached_property
    def offramp(self) -> AsyncOfframpResource:
        """Operations related to fiat onramping and offramping"""
        return AsyncOfframpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFiatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFiatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncFiatResourceWithStreamingResponse(self)

    async def configure_app(
        self,
        app_id: str,
        *,
        api_key: str,
        provider: OnrampProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """Updates the app configuration for the specified onramp provider.

        This is used to
        set up the app for fiat onramping and offramping.

        Args:
          app_id: The ID of the app that is being configured for fiat onramping and offramping

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            path_template("/v1/apps/{app_id}/fiat", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "provider": provider,
                },
                fiat_configure_app_params.FiatConfigureAppParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def get_kyc_link(
        self,
        user_id: str,
        *,
        email: str,
        provider: OnrampProvider,
        endorsements: List[Literal["sepa"]] | Omit = omit,
        full_name: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        type: Literal["individual", "business"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatGetKYCLinkResponse:
        """
        Returns a KYC link for a user

        Args:
          user_id: The ID of the user

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/fiat/kyc_link", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "provider": provider,
                    "endorsements": endorsements,
                    "full_name": full_name,
                    "redirect_uri": redirect_uri,
                    "type": type,
                },
                fiat_get_kyc_link_params.FiatGetKYCLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatGetKYCLinkResponse,
        )

    async def get_status(
        self,
        user_id: str,
        *,
        provider: OnrampProvider,
        tx_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiatGetStatusResponse:
        """
        Returns a list of fiat transactions and their statuses

        Args:
          user_id: The ID of the user

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/fiat/status", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "tx_hash": tx_hash,
                },
                fiat_get_status_params.FiatGetStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatGetStatusResponse,
        )


class FiatResourceWithRawResponse:
    def __init__(self, fiat: FiatResource) -> None:
        self._fiat = fiat

        self.configure_app = to_raw_response_wrapper(
            fiat.configure_app,
        )
        self.get_kyc_link = to_raw_response_wrapper(
            fiat.get_kyc_link,
        )
        self.get_status = to_raw_response_wrapper(
            fiat.get_status,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AccountsResourceWithRawResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> KYCResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return KYCResourceWithRawResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> OnrampResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return OnrampResourceWithRawResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> OfframpResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return OfframpResourceWithRawResponse(self._fiat.offramp)


class AsyncFiatResourceWithRawResponse:
    def __init__(self, fiat: AsyncFiatResource) -> None:
        self._fiat = fiat

        self.configure_app = async_to_raw_response_wrapper(
            fiat.configure_app,
        )
        self.get_kyc_link = async_to_raw_response_wrapper(
            fiat.get_kyc_link,
        )
        self.get_status = async_to_raw_response_wrapper(
            fiat.get_status,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncAccountsResourceWithRawResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncKYCResourceWithRawResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> AsyncOnrampResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncOnrampResourceWithRawResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> AsyncOfframpResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncOfframpResourceWithRawResponse(self._fiat.offramp)


class FiatResourceWithStreamingResponse:
    def __init__(self, fiat: FiatResource) -> None:
        self._fiat = fiat

        self.configure_app = to_streamed_response_wrapper(
            fiat.configure_app,
        )
        self.get_kyc_link = to_streamed_response_wrapper(
            fiat.get_kyc_link,
        )
        self.get_status = to_streamed_response_wrapper(
            fiat.get_status,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AccountsResourceWithStreamingResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> KYCResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return KYCResourceWithStreamingResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> OnrampResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return OnrampResourceWithStreamingResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> OfframpResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return OfframpResourceWithStreamingResponse(self._fiat.offramp)


class AsyncFiatResourceWithStreamingResponse:
    def __init__(self, fiat: AsyncFiatResource) -> None:
        self._fiat = fiat

        self.configure_app = async_to_streamed_response_wrapper(
            fiat.configure_app,
        )
        self.get_kyc_link = async_to_streamed_response_wrapper(
            fiat.get_kyc_link,
        )
        self.get_status = async_to_streamed_response_wrapper(
            fiat.get_status,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncAccountsResourceWithStreamingResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncKYCResourceWithStreamingResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> AsyncOnrampResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncOnrampResourceWithStreamingResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> AsyncOfframpResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncOfframpResourceWithStreamingResponse(self._fiat.offramp)
