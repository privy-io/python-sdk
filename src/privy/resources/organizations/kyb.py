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
from ..._base_client import make_request_options
from ...types.kyx_provider import KyxProvider
from ...types.organizations import kyb_initiate_tos_params, kyb_initiate_links_params
from ...types.kyx_environment import KyxEnvironment
from ...types.kyx_tos_response import KyxTosResponse
from ...types.kyb_status_response import KYBStatusResponse
from ...types.kyx_endorsement_name import KyxEndorsementName
from ...types.kyb_status_list_response import KYBStatusListResponse

__all__ = ["KYBResource", "AsyncKYBResource"]


class KYBResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> KYBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return KYBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KYBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return KYBResourceWithStreamingResponse(self)

    def list(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYBStatusListResponse:
        """
        Returns KYB status for all providers the organization has initiated KYB with.

        Args:
          organization_id: The ID of the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/v1/organizations/{organization_id}/kyb", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYBStatusListResponse,
        )

    def initiate_links(
        self,
        organization_id: str,
        *,
        email: str,
        provider: KyxProvider,
        business_name: str | Omit = omit,
        client_agreement_id: str | Omit = omit,
        endorsements: SequenceNotStr[KyxEndorsementName] | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYBStatusResponse:
        """
        Generates a hosted KYB link for the organization and returns the current KYB
        status snapshot.

        Args:
          organization_id: The ID of the organization.

          email: Email address for the organization.

          provider: KYC/KYB provider identifier.

          business_name: Legal name of the business.

          client_agreement_id: Client-side agreement ID for ToS acceptance.

          endorsements: Endorsements to request during KYB.

          environment: Provider environment (production or sandbox).

          redirect_uri: URI to redirect after completing KYB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template("/v1/organizations/{organization_id}/kyb/links", organization_id=organization_id),
            body=maybe_transform(
                {
                    "email": email,
                    "provider": provider,
                    "business_name": business_name,
                    "client_agreement_id": client_agreement_id,
                    "endorsements": endorsements,
                    "environment": environment,
                    "redirect_uri": redirect_uri,
                },
                kyb_initiate_links_params.KYBInitiateLinksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYBStatusResponse,
        )

    def initiate_tos(
        self,
        organization_id: str,
        *,
        email: str,
        provider: KyxProvider,
        business_name: str | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KyxTosResponse:
        """
        Generates a Bridge terms-of-service acceptance link for the organization.

        Args:
          organization_id: The ID of the organization.

          email: Email address for the organization.

          provider: KYC/KYB provider identifier.

          business_name: Legal name of the business.

          environment: Provider environment (production or sandbox).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template("/v1/organizations/{organization_id}/kyb/tos", organization_id=organization_id),
            body=maybe_transform(
                {
                    "email": email,
                    "provider": provider,
                    "business_name": business_name,
                    "environment": environment,
                },
                kyb_initiate_tos_params.KYBInitiateTosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KyxTosResponse,
        )


class AsyncKYBResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AsyncKYBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKYBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKYBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncKYBResourceWithStreamingResponse(self)

    async def list(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYBStatusListResponse:
        """
        Returns KYB status for all providers the organization has initiated KYB with.

        Args:
          organization_id: The ID of the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/v1/organizations/{organization_id}/kyb", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYBStatusListResponse,
        )

    async def initiate_links(
        self,
        organization_id: str,
        *,
        email: str,
        provider: KyxProvider,
        business_name: str | Omit = omit,
        client_agreement_id: str | Omit = omit,
        endorsements: SequenceNotStr[KyxEndorsementName] | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYBStatusResponse:
        """
        Generates a hosted KYB link for the organization and returns the current KYB
        status snapshot.

        Args:
          organization_id: The ID of the organization.

          email: Email address for the organization.

          provider: KYC/KYB provider identifier.

          business_name: Legal name of the business.

          client_agreement_id: Client-side agreement ID for ToS acceptance.

          endorsements: Endorsements to request during KYB.

          environment: Provider environment (production or sandbox).

          redirect_uri: URI to redirect after completing KYB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template("/v1/organizations/{organization_id}/kyb/links", organization_id=organization_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "provider": provider,
                    "business_name": business_name,
                    "client_agreement_id": client_agreement_id,
                    "endorsements": endorsements,
                    "environment": environment,
                    "redirect_uri": redirect_uri,
                },
                kyb_initiate_links_params.KYBInitiateLinksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYBStatusResponse,
        )

    async def initiate_tos(
        self,
        organization_id: str,
        *,
        email: str,
        provider: KyxProvider,
        business_name: str | Omit = omit,
        environment: KyxEnvironment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KyxTosResponse:
        """
        Generates a Bridge terms-of-service acceptance link for the organization.

        Args:
          organization_id: The ID of the organization.

          email: Email address for the organization.

          provider: KYC/KYB provider identifier.

          business_name: Legal name of the business.

          environment: Provider environment (production or sandbox).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template("/v1/organizations/{organization_id}/kyb/tos", organization_id=organization_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "provider": provider,
                    "business_name": business_name,
                    "environment": environment,
                },
                kyb_initiate_tos_params.KYBInitiateTosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KyxTosResponse,
        )


class KYBResourceWithRawResponse:
    def __init__(self, kyb: KYBResource) -> None:
        self._kyb = kyb

        self.list = to_raw_response_wrapper(
            kyb.list,
        )
        self.initiate_links = to_raw_response_wrapper(
            kyb.initiate_links,
        )
        self.initiate_tos = to_raw_response_wrapper(
            kyb.initiate_tos,
        )


class AsyncKYBResourceWithRawResponse:
    def __init__(self, kyb: AsyncKYBResource) -> None:
        self._kyb = kyb

        self.list = async_to_raw_response_wrapper(
            kyb.list,
        )
        self.initiate_links = async_to_raw_response_wrapper(
            kyb.initiate_links,
        )
        self.initiate_tos = async_to_raw_response_wrapper(
            kyb.initiate_tos,
        )


class KYBResourceWithStreamingResponse:
    def __init__(self, kyb: KYBResource) -> None:
        self._kyb = kyb

        self.list = to_streamed_response_wrapper(
            kyb.list,
        )
        self.initiate_links = to_streamed_response_wrapper(
            kyb.initiate_links,
        )
        self.initiate_tos = to_streamed_response_wrapper(
            kyb.initiate_tos,
        )


class AsyncKYBResourceWithStreamingResponse:
    def __init__(self, kyb: AsyncKYBResource) -> None:
        self._kyb = kyb

        self.list = async_to_streamed_response_wrapper(
            kyb.list,
        )
        self.initiate_links = async_to_streamed_response_wrapper(
            kyb.initiate_links,
        )
        self.initiate_tos = async_to_streamed_response_wrapper(
            kyb.initiate_tos,
        )
