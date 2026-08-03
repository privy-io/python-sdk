# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...types import OnrampProvider
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.fiat import kyc_get_params, kyc_create_params, kyc_update_params
from ..._base_client import make_request_options
from ...types.onramp_provider import OnrampProvider
from ...types.onramp_kyc_response import OnrampKYCResponse
from ...types.fiat.kyc_get_response import KYCGetResponse

__all__ = ["KYCResource", "AsyncKYCResource"]


class KYCResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> KYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return KYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return KYCResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        user_id: str,
        *,
        data: kyc_create_params.Variant0Data,
        provider: Literal["bridge"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Initiates KYC verification process for a user with the configured provider

        Args:
          user_id: The ID of the user to initiate KYC for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        user_id: str,
        *,
        data: kyc_create_params.Variant1Data,
        provider: Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Initiates KYC verification process for a user with the configured provider

        Args:
          user_id: The ID of the user to initiate KYC for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["data", "provider"])
    def create(
        self,
        user_id: str,
        *,
        data: kyc_create_params.Variant0Data | kyc_create_params.Variant1Data,
        provider: Literal["bridge"] | Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/fiat/kyc", user_id=user_id),
            body=maybe_transform(
                {
                    "data": data,
                    "provider": provider,
                },
                kyc_create_params.KYCCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnrampKYCResponse,
        )

    @overload
    def update(
        self,
        user_id: str,
        *,
        data: kyc_update_params.Variant0Data,
        provider: Literal["bridge"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Update the KYC verification status for a user from the configured provider

        Args:
          user_id: The ID of the user to update KYC status for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        user_id: str,
        *,
        data: kyc_update_params.Variant1Data,
        provider: Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Update the KYC verification status for a user from the configured provider

        Args:
          user_id: The ID of the user to update KYC status for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["data", "provider"])
    def update(
        self,
        user_id: str,
        *,
        data: kyc_update_params.Variant0Data | kyc_update_params.Variant1Data,
        provider: Literal["bridge"] | Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            path_template("/v1/users/{user_id}/fiat/kyc", user_id=user_id),
            body=maybe_transform(
                {
                    "data": data,
                    "provider": provider,
                },
                kyc_update_params.KYCUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnrampKYCResponse,
        )

    def get(
        self,
        user_id: str,
        *,
        provider: OnrampProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCGetResponse:
        """
        Get the current KYC verification status for a user from the configured provider

        Args:
          user_id: The ID of the user to get KYC status for

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}/fiat/kyc", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"provider": provider}, kyc_get_params.KYCGetParams),
            ),
            cast_to=KYCGetResponse,
        )


class AsyncKYCResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AsyncKYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncKYCResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        user_id: str,
        *,
        data: kyc_create_params.Variant0Data,
        provider: Literal["bridge"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Initiates KYC verification process for a user with the configured provider

        Args:
          user_id: The ID of the user to initiate KYC for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        user_id: str,
        *,
        data: kyc_create_params.Variant1Data,
        provider: Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Initiates KYC verification process for a user with the configured provider

        Args:
          user_id: The ID of the user to initiate KYC for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["data", "provider"])
    async def create(
        self,
        user_id: str,
        *,
        data: kyc_create_params.Variant0Data | kyc_create_params.Variant1Data,
        provider: Literal["bridge"] | Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/fiat/kyc", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "provider": provider,
                },
                kyc_create_params.KYCCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnrampKYCResponse,
        )

    @overload
    async def update(
        self,
        user_id: str,
        *,
        data: kyc_update_params.Variant0Data,
        provider: Literal["bridge"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Update the KYC verification status for a user from the configured provider

        Args:
          user_id: The ID of the user to update KYC status for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        user_id: str,
        *,
        data: kyc_update_params.Variant1Data,
        provider: Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        """
        Update the KYC verification status for a user from the configured provider

        Args:
          user_id: The ID of the user to update KYC status for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["data", "provider"])
    async def update(
        self,
        user_id: str,
        *,
        data: kyc_update_params.Variant0Data | kyc_update_params.Variant1Data,
        provider: Literal["bridge"] | Literal["bridge-sandbox"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnrampKYCResponse:
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            path_template("/v1/users/{user_id}/fiat/kyc", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "provider": provider,
                },
                kyc_update_params.KYCUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnrampKYCResponse,
        )

    async def get(
        self,
        user_id: str,
        *,
        provider: OnrampProvider,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCGetResponse:
        """
        Get the current KYC verification status for a user from the configured provider

        Args:
          user_id: The ID of the user to get KYC status for

          provider: Valid set of onramp providers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/fiat/kyc", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"provider": provider}, kyc_get_params.KYCGetParams),
            ),
            cast_to=KYCGetResponse,
        )


class KYCResourceWithRawResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.create = to_raw_response_wrapper(
            kyc.create,
        )
        self.update = to_raw_response_wrapper(
            kyc.update,
        )
        self.get = to_raw_response_wrapper(
            kyc.get,
        )


class AsyncKYCResourceWithRawResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.create = async_to_raw_response_wrapper(
            kyc.create,
        )
        self.update = async_to_raw_response_wrapper(
            kyc.update,
        )
        self.get = async_to_raw_response_wrapper(
            kyc.get,
        )


class KYCResourceWithStreamingResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.create = to_streamed_response_wrapper(
            kyc.create,
        )
        self.update = to_streamed_response_wrapper(
            kyc.update,
        )
        self.get = to_streamed_response_wrapper(
            kyc.get,
        )


class AsyncKYCResourceWithStreamingResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.create = async_to_streamed_response_wrapper(
            kyc.create,
        )
        self.update = async_to_streamed_response_wrapper(
            kyc.update,
        )
        self.get = async_to_streamed_response_wrapper(
            kyc.get,
        )
