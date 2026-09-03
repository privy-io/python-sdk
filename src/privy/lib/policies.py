"""Public policy operations."""

from __future__ import annotations

from typing import Any, Callable, cast

from .._types import omit
from .._client import PrivyAPI
from .request_url import build_request_url
from .jwt_exchange import JWTExchangeService
from ..types.policy import Policy
from .authorization import prepare_request
from .request_expiry import RequestExpiryProvider, resolve_request_expiry
from .request_options import PrivyRequestOptions
from ..resources.policies import PoliciesResource
from ..types.success_response import SuccessResponse
from ..types.policy_rule_response import PolicyRuleResponse
from ..types.policy_update_params import PolicyUpdateParams
from ..types.policy_create_rule_params import PolicyCreateRuleParams
from ..types.policy_update_rule_params import PolicyUpdateRuleParams

__all__ = ["PrivyPoliciesService"]


class PrivyPoliciesService(PoliciesResource):
    def __init__(
        self,
        client: PrivyAPI,
        request_expiry_provider: RequestExpiryProvider | None = None,
        jwt_exchanger: JWTExchangeService | None = None,
    ) -> None:
        super().__init__(client)
        self._request_expiry_provider = request_expiry_provider
        self._jwt_exchanger = jwt_exchanger

    def create_rule(
        self,
        policy_id: str,
        *,
        policy_create_rule_params: PolicyCreateRuleParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> PolicyRuleResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        body = dict(policy_create_rule_params)
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=build_request_url(client, f"/v1/policies/{policy_id}/rules"),
            body=body,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        create_rule = cast(Callable[..., PolicyRuleResponse], generated._create_rule)
        return create_rule(
            policy_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def update(
        self,
        policy_id: str,
        *,
        policy_update_params: PolicyUpdateParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> Policy:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        body = dict(policy_update_params)
        prepared = prepare_request(
            app_id=client.app_id,
            method="PATCH",
            url=build_request_url(client, f"/v1/policies/{policy_id}"),
            body=body,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        update = cast(Callable[..., Policy], generated._update)
        return update(
            policy_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def update_rule(
        self,
        rule_id: str,
        *,
        policy_update_rule_params: PolicyUpdateRuleParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> PolicyRuleResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        params = dict(policy_update_rule_params)
        policy_id = cast(str, params.pop("policy_id"))
        prepared = prepare_request(
            app_id=client.app_id,
            method="PATCH",
            url=build_request_url(client, f"/v1/policies/{policy_id}/rules/{rule_id}"),
            body=params,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        update_rule = cast(Callable[..., PolicyRuleResponse], generated._update_rule)
        return update_rule(
            rule_id,
            policy_id=policy_id,
            **params,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def delete(
        self,
        policy_id: str,
        *,
        request_options: PrivyRequestOptions | None = None,
    ) -> SuccessResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="DELETE",
            url=build_request_url(client, f"/v1/policies/{policy_id}"),
            body={},
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
            preserve_empty_body=True,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        delete_policy = cast(Callable[..., SuccessResponse], generated._delete_policy)
        return delete_policy(
            policy_id,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def delete_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        request_options: PrivyRequestOptions | None = None,
    ) -> SuccessResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="DELETE",
            url=build_request_url(client, f"/v1/policies/{policy_id}/rules/{rule_id}"),
            body={},
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
            preserve_empty_body=True,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        delete_rule = cast(Callable[..., SuccessResponse], generated._delete_rule)
        return delete_rule(
            rule_id,
            policy_id=policy_id,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )
