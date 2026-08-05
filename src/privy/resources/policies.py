# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    OwnerIDInput,
    PolicyAction,
    PolicyMethod,
    WalletChainType,
    policy_create_params,
    policy_update_params,
    policy_create_rule_params,
    policy_update_rule_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.policy_action import PolicyAction
from ..types.policy_method import PolicyMethod
from ..types.owner_id_input import OwnerIDInput
from ..types.success_response import SuccessResponse
from ..types.owner_input_param import OwnerInputParam
from ..types.wallet_chain_type import WalletChainType
from ..types.policy_rule_response import PolicyRuleResponse
from ..types.policy_condition_param import PolicyConditionParam
from ..types.policy_rule_request_body_param import PolicyRuleRequestBodyParam

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    """Operations related to policies"""

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
        chain_type: WalletChainType,
        name: str,
        rules: Iterable[policy_create_params.Rule],
        version: Literal["1.0"],
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Create a new policy.

        Args:
          chain_type: The wallet chain types.

          name: Name to assign to policy.

          version: Version of the policy. Currently, 1.0 is the only version.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"privy-idempotency-key": privy_idempotency_key}), **(extra_headers or {})}
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

    def _create_rule(
        self,
        policy_id: str,
        *,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRuleResponse:
        """
        Create a new rule for a policy.

        Args:
          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/policies/{policy_id}/rules", policy_id=policy_id),
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                policy_create_rule_params.PolicyCreateRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRuleResponse,
        )

    def _delete_policy(
        self,
        policy_id: str,
        *,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Delete a policy by policy ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/v1/policies/{policy_id}", policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def _delete_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Delete a rule by policy ID and rule ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/v1/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def _update(
        self,
        policy_id: str,
        *,
        name: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        rules: Iterable[PolicyRuleRequestBodyParam] | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Update a policy by policy ID.

        Args:
          name: Name to assign to policy.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v1/policies/{policy_id}", policy_id=policy_id),
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

    def _update_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRuleResponse:
        """
        Update a rule by policy ID and rule ID.

        Args:
          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v1/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                policy_update_rule_params.PolicyUpdateRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRuleResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/policies/{policy_id}", policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def get_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRuleResponse:
        """
        Get a rule by policy ID and rule ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            path_template("/v1/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRuleResponse,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    """Operations related to policies"""

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
        chain_type: WalletChainType,
        name: str,
        rules: Iterable[policy_create_params.Rule],
        version: Literal["1.0"],
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Create a new policy.

        Args:
          chain_type: The wallet chain types.

          name: Name to assign to policy.

          version: Version of the policy. Currently, 1.0 is the only version.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"privy-idempotency-key": privy_idempotency_key}), **(extra_headers or {})}
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

    async def _create_rule(
        self,
        policy_id: str,
        *,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRuleResponse:
        """
        Create a new rule for a policy.

        Args:
          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/policies/{policy_id}/rules", policy_id=policy_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                policy_create_rule_params.PolicyCreateRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRuleResponse,
        )

    async def _delete_policy(
        self,
        policy_id: str,
        *,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Delete a policy by policy ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/v1/policies/{policy_id}", policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def _delete_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Delete a rule by policy ID and rule ID.

        Args:
          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/v1/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def _update(
        self,
        policy_id: str,
        *,
        name: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        rules: Iterable[PolicyRuleRequestBodyParam] | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Update a policy by policy ID.

        Args:
          name: Name to assign to policy.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v1/policies/{policy_id}", policy_id=policy_id),
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

    async def _update_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRuleResponse:
        """
        Update a rule by policy ID and rule ID.

        Args:
          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v1/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                policy_update_rule_params.PolicyUpdateRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRuleResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/policies/{policy_id}", policy_id=policy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def get_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRuleResponse:
        """
        Get a rule by policy ID and rule ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            path_template("/v1/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRuleResponse,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self._create_rule = to_raw_response_wrapper(
            policies._create_rule,
        )
        self._delete_policy = to_raw_response_wrapper(
            policies._delete_policy,
        )
        self._delete_rule = to_raw_response_wrapper(
            policies._delete_rule,
        )
        self._update = to_raw_response_wrapper(
            policies._update,
        )
        self._update_rule = to_raw_response_wrapper(
            policies._update_rule,
        )
        self.get = to_raw_response_wrapper(
            policies.get,
        )
        self.get_rule = to_raw_response_wrapper(
            policies.get_rule,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self._create_rule = async_to_raw_response_wrapper(
            policies._create_rule,
        )
        self._delete_policy = async_to_raw_response_wrapper(
            policies._delete_policy,
        )
        self._delete_rule = async_to_raw_response_wrapper(
            policies._delete_rule,
        )
        self._update = async_to_raw_response_wrapper(
            policies._update,
        )
        self._update_rule = async_to_raw_response_wrapper(
            policies._update_rule,
        )
        self.get = async_to_raw_response_wrapper(
            policies.get,
        )
        self.get_rule = async_to_raw_response_wrapper(
            policies.get_rule,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self._create_rule = to_streamed_response_wrapper(
            policies._create_rule,
        )
        self._delete_policy = to_streamed_response_wrapper(
            policies._delete_policy,
        )
        self._delete_rule = to_streamed_response_wrapper(
            policies._delete_rule,
        )
        self._update = to_streamed_response_wrapper(
            policies._update,
        )
        self._update_rule = to_streamed_response_wrapper(
            policies._update_rule,
        )
        self.get = to_streamed_response_wrapper(
            policies.get,
        )
        self.get_rule = to_streamed_response_wrapper(
            policies.get_rule,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self._create_rule = async_to_streamed_response_wrapper(
            policies._create_rule,
        )
        self._delete_policy = async_to_streamed_response_wrapper(
            policies._delete_policy,
        )
        self._delete_rule = async_to_streamed_response_wrapper(
            policies._delete_rule,
        )
        self._update = async_to_streamed_response_wrapper(
            policies._update,
        )
        self._update_rule = async_to_streamed_response_wrapper(
            policies._update_rule,
        )
        self.get = async_to_streamed_response_wrapper(
            policies.get,
        )
        self.get_rule = async_to_streamed_response_wrapper(
            policies.get_rule,
        )
