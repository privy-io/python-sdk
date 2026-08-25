# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import Environment, OrchestrationProvider
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.environment import Environment
from ...types.organizations import external_fiat_account_list_params, external_fiat_account_create_params
from ...types.success_response import SuccessResponse
from ...types.orchestration_provider import OrchestrationProvider
from ...types.external_fiat_account_data_param import ExternalFiatAccountDataParam
from ...types.external_fiat_account_address_param import ExternalFiatAccountAddressParam
from ...types.organization_external_fiat_account_response import OrganizationExternalFiatAccountResponse
from ...types.list_organization_external_fiat_accounts_response import ListOrganizationExternalFiatAccountsResponse

__all__ = ["ExternalFiatAccountsResource", "AsyncExternalFiatAccountsResource"]


class ExternalFiatAccountsResource(SyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> ExternalFiatAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExternalFiatAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalFiatAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return ExternalFiatAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        organization_id: str,
        *,
        account: ExternalFiatAccountDataParam,
        account_owner_name: str,
        currency: str,
        provider: Literal["bridge"],
        address: ExternalFiatAccountAddressParam | Omit = omit,
        bank_name: str | Omit = omit,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationExternalFiatAccountResponse:
        """
        Creates an external fiat account linked to an organization for use in offramp
        transfers.

        Args:
          organization_id: The ID of the organization to create the external fiat account for.

          account: Bank account details. The `type` field discriminates which shape applies.

          provider: Discriminator: the external fiat account is orchestrated via Bridge.

          address: Physical address associated with an external fiat account.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts", organization_id=organization_id
            ),
            body=maybe_transform(
                {
                    "account": account,
                    "account_owner_name": account_owner_name,
                    "currency": currency,
                    "provider": provider,
                    "address": address,
                    "bank_name": bank_name,
                    "environment": environment,
                },
                external_fiat_account_create_params.ExternalFiatAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationExternalFiatAccountResponse,
        )

    def list(
        self,
        organization_id: str,
        *,
        provider: OrchestrationProvider,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListOrganizationExternalFiatAccountsResponse:
        """
        Returns a list of external fiat accounts linked to an organization.

        Args:
          organization_id: The ID of the organization to list external fiat accounts for.

          provider: Supported fiat orchestration providers.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts", organization_id=organization_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "environment": environment,
                    },
                    external_fiat_account_list_params.ExternalFiatAccountListParams,
                ),
            ),
            cast_to=ListOrganizationExternalFiatAccountsResponse,
        )

    def delete(
        self,
        account_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Deletes an external fiat account linked to an organization.

        Args:
          organization_id: The ID of the organization.

          account_id: The ID of the external fiat account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts/{account_id}",
                organization_id=organization_id,
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def get(
        self,
        account_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationExternalFiatAccountResponse:
        """
        Returns a single external fiat account linked to an organization.

        Args:
          organization_id: The ID of the organization.

          account_id: The ID of the external fiat account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts/{account_id}",
                organization_id=organization_id,
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationExternalFiatAccountResponse,
        )


class AsyncExternalFiatAccountsResource(AsyncAPIResource):
    """Operations related to fiat onramping and offramping"""

    @cached_property
    def with_raw_response(self) -> AsyncExternalFiatAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalFiatAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalFiatAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncExternalFiatAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        organization_id: str,
        *,
        account: ExternalFiatAccountDataParam,
        account_owner_name: str,
        currency: str,
        provider: Literal["bridge"],
        address: ExternalFiatAccountAddressParam | Omit = omit,
        bank_name: str | Omit = omit,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationExternalFiatAccountResponse:
        """
        Creates an external fiat account linked to an organization for use in offramp
        transfers.

        Args:
          organization_id: The ID of the organization to create the external fiat account for.

          account: Bank account details. The `type` field discriminates which shape applies.

          provider: Discriminator: the external fiat account is orchestrated via Bridge.

          address: Physical address associated with an external fiat account.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts", organization_id=organization_id
            ),
            body=await async_maybe_transform(
                {
                    "account": account,
                    "account_owner_name": account_owner_name,
                    "currency": currency,
                    "provider": provider,
                    "address": address,
                    "bank_name": bank_name,
                    "environment": environment,
                },
                external_fiat_account_create_params.ExternalFiatAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationExternalFiatAccountResponse,
        )

    async def list(
        self,
        organization_id: str,
        *,
        provider: OrchestrationProvider,
        environment: Environment | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListOrganizationExternalFiatAccountsResponse:
        """
        Returns a list of external fiat accounts linked to an organization.

        Args:
          organization_id: The ID of the organization to list external fiat accounts for.

          provider: Supported fiat orchestration providers.

          environment: The Privy API environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts", organization_id=organization_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "environment": environment,
                    },
                    external_fiat_account_list_params.ExternalFiatAccountListParams,
                ),
            ),
            cast_to=ListOrganizationExternalFiatAccountsResponse,
        )

    async def delete(
        self,
        account_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Deletes an external fiat account linked to an organization.

        Args:
          organization_id: The ID of the organization.

          account_id: The ID of the external fiat account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts/{account_id}",
                organization_id=organization_id,
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def get(
        self,
        account_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationExternalFiatAccountResponse:
        """
        Returns a single external fiat account linked to an organization.

        Args:
          organization_id: The ID of the organization.

          account_id: The ID of the external fiat account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template(
                "/v1/organizations/{organization_id}/external_fiat_accounts/{account_id}",
                organization_id=organization_id,
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationExternalFiatAccountResponse,
        )


class ExternalFiatAccountsResourceWithRawResponse:
    def __init__(self, external_fiat_accounts: ExternalFiatAccountsResource) -> None:
        self._external_fiat_accounts = external_fiat_accounts

        self.create = to_raw_response_wrapper(
            external_fiat_accounts.create,
        )
        self.list = to_raw_response_wrapper(
            external_fiat_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            external_fiat_accounts.delete,
        )
        self.get = to_raw_response_wrapper(
            external_fiat_accounts.get,
        )


class AsyncExternalFiatAccountsResourceWithRawResponse:
    def __init__(self, external_fiat_accounts: AsyncExternalFiatAccountsResource) -> None:
        self._external_fiat_accounts = external_fiat_accounts

        self.create = async_to_raw_response_wrapper(
            external_fiat_accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            external_fiat_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            external_fiat_accounts.delete,
        )
        self.get = async_to_raw_response_wrapper(
            external_fiat_accounts.get,
        )


class ExternalFiatAccountsResourceWithStreamingResponse:
    def __init__(self, external_fiat_accounts: ExternalFiatAccountsResource) -> None:
        self._external_fiat_accounts = external_fiat_accounts

        self.create = to_streamed_response_wrapper(
            external_fiat_accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            external_fiat_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            external_fiat_accounts.delete,
        )
        self.get = to_streamed_response_wrapper(
            external_fiat_accounts.get,
        )


class AsyncExternalFiatAccountsResourceWithStreamingResponse:
    def __init__(self, external_fiat_accounts: AsyncExternalFiatAccountsResource) -> None:
        self._external_fiat_accounts = external_fiat_accounts

        self.create = async_to_streamed_response_wrapper(
            external_fiat_accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            external_fiat_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            external_fiat_accounts.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            external_fiat_accounts.get,
        )
