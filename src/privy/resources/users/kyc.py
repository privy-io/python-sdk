# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import KyxProvider, KyxEnvironment
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
from ...types.users import kyc_initiate_tos_params, kyc_initiate_links_params
from ..._base_client import make_request_options
from ...types.kyx_provider import KyxProvider
from ...types.kyx_environment import KyxEnvironment
from ...types.kyx_tos_response import KyxTosResponse
from ...types.kyc_status_response import KYCStatusResponse
from ...types.kyx_endorsement_name import KyxEndorsementName
from ...types.kyc_status_list_response import KYCStatusListResponse

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

    def list(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatusListResponse:
        """
        Returns KYC status for all providers the user has initiated KYC with.

        Args:
          user_id: The ID of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}/kyc", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatusListResponse,
        )

    def initiate_links(
        self,
        user_id: str,
        *,
        provider: KyxProvider,
        client_agreement_id: str | Omit = omit,
        email: str | Omit = omit,
        endorsements: SequenceNotStr[KyxEndorsementName] | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatusResponse:
        """
        Generates a hosted KYC link for the user and returns the current KYC status
        snapshot.

        Args:
          user_id: The ID of the user.

          provider: KYC/KYB provider identifier.

          client_agreement_id: Client-side agreement ID for ToS acceptance.

          email: Email address for the KYC session.

          endorsements: Endorsements to request during KYC.

          environment: Provider environment (production or sandbox).

          redirect_uri: URI to redirect the user after completing KYC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/kyc/links", user_id=user_id),
            body=maybe_transform(
                {
                    "provider": provider,
                    "client_agreement_id": client_agreement_id,
                    "email": email,
                    "endorsements": endorsements,
                    "environment": environment,
                    "redirect_uri": redirect_uri,
                },
                kyc_initiate_links_params.KYCInitiateLinksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatusResponse,
        )

    def initiate_tos(
        self,
        user_id: str,
        *,
        provider: KyxProvider,
        email: str | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KyxTosResponse:
        """
        Generates a Bridge terms-of-service acceptance link for the user.

        Args:
          user_id: The ID of the user.

          provider: KYC/KYB provider identifier.

          email: Email for the user. If not provided, falls back to the user's linked email.

          environment: Provider environment (production or sandbox).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/kyc/tos", user_id=user_id),
            body=maybe_transform(
                {
                    "provider": provider,
                    "email": email,
                    "environment": environment,
                },
                kyc_initiate_tos_params.KYCInitiateTosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KyxTosResponse,
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

    async def list(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatusListResponse:
        """
        Returns KYC status for all providers the user has initiated KYC with.

        Args:
          user_id: The ID of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/kyc", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatusListResponse,
        )

    async def initiate_links(
        self,
        user_id: str,
        *,
        provider: KyxProvider,
        client_agreement_id: str | Omit = omit,
        email: str | Omit = omit,
        endorsements: SequenceNotStr[KyxEndorsementName] | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatusResponse:
        """
        Generates a hosted KYC link for the user and returns the current KYC status
        snapshot.

        Args:
          user_id: The ID of the user.

          provider: KYC/KYB provider identifier.

          client_agreement_id: Client-side agreement ID for ToS acceptance.

          email: Email address for the KYC session.

          endorsements: Endorsements to request during KYC.

          environment: Provider environment (production or sandbox).

          redirect_uri: URI to redirect the user after completing KYC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/kyc/links", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "client_agreement_id": client_agreement_id,
                    "email": email,
                    "endorsements": endorsements,
                    "environment": environment,
                    "redirect_uri": redirect_uri,
                },
                kyc_initiate_links_params.KYCInitiateLinksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatusResponse,
        )

    async def initiate_tos(
        self,
        user_id: str,
        *,
        provider: KyxProvider,
        email: str | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KyxTosResponse:
        """
        Generates a Bridge terms-of-service acceptance link for the user.

        Args:
          user_id: The ID of the user.

          provider: KYC/KYB provider identifier.

          email: Email for the user. If not provided, falls back to the user's linked email.

          environment: Provider environment (production or sandbox).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/kyc/tos", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "email": email,
                    "environment": environment,
                },
                kyc_initiate_tos_params.KYCInitiateTosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KyxTosResponse,
        )


class KYCResourceWithRawResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.list = to_raw_response_wrapper(
            kyc.list,
        )
        self.initiate_links = to_raw_response_wrapper(
            kyc.initiate_links,
        )
        self.initiate_tos = to_raw_response_wrapper(
            kyc.initiate_tos,
        )


class AsyncKYCResourceWithRawResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.list = async_to_raw_response_wrapper(
            kyc.list,
        )
        self.initiate_links = async_to_raw_response_wrapper(
            kyc.initiate_links,
        )
        self.initiate_tos = async_to_raw_response_wrapper(
            kyc.initiate_tos,
        )


class KYCResourceWithStreamingResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.list = to_streamed_response_wrapper(
            kyc.list,
        )
        self.initiate_links = to_streamed_response_wrapper(
            kyc.initiate_links,
        )
        self.initiate_tos = to_streamed_response_wrapper(
            kyc.initiate_tos,
        )


class AsyncKYCResourceWithStreamingResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.list = async_to_streamed_response_wrapper(
            kyc.list,
        )
        self.initiate_links = async_to_streamed_response_wrapper(
            kyc.initiate_links,
        )
        self.initiate_tos = async_to_streamed_response_wrapper(
            kyc.initiate_tos,
        )
