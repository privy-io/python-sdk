# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import policy_create_params, policy_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.policy import Policy
from ..types.policy_delete_response import PolicyDeleteResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        chain_type: Literal["ethereum", "solana"],
        name: str,
        rules: Iterable[policy_create_params.Rule],
        version: Literal["1.0"],
        owner: Optional[policy_create_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Policy:
        """
        Create a new policy.

        Args:
          chain_type: Chain type the policy applies to.

          name: Name to assign to policy.

          rules: The rules that apply to each method the policy covers.

          version: Version of the policy. Currently, 1.0 is the only version.

          owner: The pem-formatted, P-256 public key of the owner of the policy. If you provide
              this, do not specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the policy. If you provide this, do not
              specify an owner.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/policies",
            body=maybe_transform(
                {
                    "chain_type": chain_type,
                    "name": name,
                    "rules": rules,
                    "version": version,
                    "owner": owner,
                    "owner_id": owner_id,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def update(
        self,
        policy_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        owner: Optional[policy_update_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        rules: Iterable[policy_update_params.Rule] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Policy:
        """
        Update a policy by policy ID.

        Args:
          name: Name to assign to policy.

          owner: The P-256 public key of the owner of the policy. If you provide this, do not
              specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the policy. If you provide this, do not
              specify an owner.

          rules: The rules that apply to each method the policy covers.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return self._patch(
            f"/v1/policies/{policy_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "rules": rules,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def delete(
        self,
        policy_id: str,
        *,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyDeleteResponse:
        """
        Delete a policy by policy ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/v1/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyDeleteResponse,
        )

    def get(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Policy:
        """
        Get a policy by policy ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/v1/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        chain_type: Literal["ethereum", "solana"],
        name: str,
        rules: Iterable[policy_create_params.Rule],
        version: Literal["1.0"],
        owner: Optional[policy_create_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Policy:
        """
        Create a new policy.

        Args:
          chain_type: Chain type the policy applies to.

          name: Name to assign to policy.

          rules: The rules that apply to each method the policy covers.

          version: Version of the policy. Currently, 1.0 is the only version.

          owner: The pem-formatted, P-256 public key of the owner of the policy. If you provide
              this, do not specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the policy. If you provide this, do not
              specify an owner.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/policies",
            body=await async_maybe_transform(
                {
                    "chain_type": chain_type,
                    "name": name,
                    "rules": rules,
                    "version": version,
                    "owner": owner,
                    "owner_id": owner_id,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def update(
        self,
        policy_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        owner: Optional[policy_update_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        rules: Iterable[policy_update_params.Rule] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Policy:
        """
        Update a policy by policy ID.

        Args:
          name: Name to assign to policy.

          owner: The P-256 public key of the owner of the policy. If you provide this, do not
              specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the policy. If you provide this, do not
              specify an owner.

          rules: The rules that apply to each method the policy covers.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return await self._patch(
            f"/v1/policies/{policy_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "rules": rules,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def delete(
        self,
        policy_id: str,
        *,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyDeleteResponse:
        """
        Delete a policy by policy ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/v1/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyDeleteResponse,
        )

    async def get(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Policy:
        """
        Get a policy by policy ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/v1/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )
        self.get = to_raw_response_wrapper(
            policies.get,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policies.get,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = to_streamed_response_wrapper(
            policies.get,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policies.get,
        )
