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
from ...types import fiat_get_status_params, fiat_get_kyc_link_params, fiat_configure_app_params
from .offramp import (
    OfframpResource,
    AsyncOfframpResource,
    OfframpResourceWithRawResponse,
    AsyncOfframpResourceWithRawResponse,
    OfframpResourceWithStreamingResponse,
    AsyncOfframpResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.fiat_get_status_response import FiatGetStatusResponse
from ...types.fiat_get_kyc_link_response import FiatGetKYCLinkResponse
from ...types.fiat_configure_app_response import FiatConfigureAppResponse

__all__ = ["FiatResource", "AsyncFiatResource"]


class FiatResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def kyc(self) -> KYCResource:
        return KYCResource(self._client)

    @cached_property
    def onramp(self) -> OnrampResource:
        return OnrampResource(self._client)

    @cached_property
    def offramp(self) -> OfframpResource:
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
        provider: Literal["bridge", "bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FiatConfigureAppResponse:
        """Updates the app configuration for the specified onramp provider.

        This is used to
        set up the app for fiat onramping and offramping.

        Args:
          app_id: The ID of the app that is being configured for fiat onramping and offramping

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            f"/v1/apps/{app_id}/fiat",
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
            cast_to=FiatConfigureAppResponse,
        )

    def get_kyc_link(
        self,
        user_id: str,
        *,
        email: str,
        provider: Literal["bridge", "bridge-sandbox"],
        endorsements: List[Literal["sepa"]] | NotGiven = NOT_GIVEN,
        full_name: str | NotGiven = NOT_GIVEN,
        redirect_uri: str | NotGiven = NOT_GIVEN,
        type: Literal["individual", "business"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FiatGetKYCLinkResponse:
        """
        Returns a KYC link for a user

        Args:
          user_id: The ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/users/{user_id}/fiat/kyc_link",
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
        provider: Literal["bridge", "bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FiatGetStatusResponse:
        """
        Returns a list of fiat transactions and their statuses

        Args:
          user_id: The ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/users/{user_id}/fiat/status",
            body=maybe_transform({"provider": provider}, fiat_get_status_params.FiatGetStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FiatGetStatusResponse,
        )


class AsyncFiatResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def kyc(self) -> AsyncKYCResource:
        return AsyncKYCResource(self._client)

    @cached_property
    def onramp(self) -> AsyncOnrampResource:
        return AsyncOnrampResource(self._client)

    @cached_property
    def offramp(self) -> AsyncOfframpResource:
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
        provider: Literal["bridge", "bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FiatConfigureAppResponse:
        """Updates the app configuration for the specified onramp provider.

        This is used to
        set up the app for fiat onramping and offramping.

        Args:
          app_id: The ID of the app that is being configured for fiat onramping and offramping

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            f"/v1/apps/{app_id}/fiat",
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
            cast_to=FiatConfigureAppResponse,
        )

    async def get_kyc_link(
        self,
        user_id: str,
        *,
        email: str,
        provider: Literal["bridge", "bridge-sandbox"],
        endorsements: List[Literal["sepa"]] | NotGiven = NOT_GIVEN,
        full_name: str | NotGiven = NOT_GIVEN,
        redirect_uri: str | NotGiven = NOT_GIVEN,
        type: Literal["individual", "business"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FiatGetKYCLinkResponse:
        """
        Returns a KYC link for a user

        Args:
          user_id: The ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/users/{user_id}/fiat/kyc_link",
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
        provider: Literal["bridge", "bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FiatGetStatusResponse:
        """
        Returns a list of fiat transactions and their statuses

        Args:
          user_id: The ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/users/{user_id}/fiat/status",
            body=await async_maybe_transform({"provider": provider}, fiat_get_status_params.FiatGetStatusParams),
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
        return AccountsResourceWithRawResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> KYCResourceWithRawResponse:
        return KYCResourceWithRawResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> OnrampResourceWithRawResponse:
        return OnrampResourceWithRawResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> OfframpResourceWithRawResponse:
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
        return AsyncAccountsResourceWithRawResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithRawResponse:
        return AsyncKYCResourceWithRawResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> AsyncOnrampResourceWithRawResponse:
        return AsyncOnrampResourceWithRawResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> AsyncOfframpResourceWithRawResponse:
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
        return AccountsResourceWithStreamingResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> KYCResourceWithStreamingResponse:
        return KYCResourceWithStreamingResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> OnrampResourceWithStreamingResponse:
        return OnrampResourceWithStreamingResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> OfframpResourceWithStreamingResponse:
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
        return AsyncAccountsResourceWithStreamingResponse(self._fiat.accounts)

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithStreamingResponse:
        return AsyncKYCResourceWithStreamingResponse(self._fiat.kyc)

    @cached_property
    def onramp(self) -> AsyncOnrampResourceWithStreamingResponse:
        return AsyncOnrampResourceWithStreamingResponse(self._fiat.onramp)

    @cached_property
    def offramp(self) -> AsyncOfframpResourceWithStreamingResponse:
        return AsyncOfframpResourceWithStreamingResponse(self._fiat.offramp)
