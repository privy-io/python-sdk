"""Public intent operations."""

# The generated resource uses flattened keyword arguments. This public layer
# intentionally follows the handwritten SDK convention of accepting generated
# request-body TypedDicts, so its overrides have a narrower ergonomic signature.
# pyright: reportIncompatibleMethodOverride=false, reportImplicitOverride=false
# mypy: disable-error-code="override"

from __future__ import annotations

from typing import Any, Callable, cast

from .._types import Omit, omit
from .._client import PrivyAPI
from .request_expiry import RequestExpiryProvider, resolve_request_expiry
from .request_options import PrivyRequestOptions
from ..resources.intents import IntentsResource
from ..types.intent_rpc_params import IntentRpcParams
from ..types.rpc_intent_response import RpcIntentResponse
from ..types.intent_transfer_params import IntentTransferParams
from ..types.policy_intent_response import PolicyIntentResponse
from ..types.wallet_intent_response import WalletIntentResponse
from ..types.transfer_intent_response import TransferIntentResponse
from ..types.key_quorum_intent_response import KeyQuorumIntentResponse
from ..types.intent_update_policy_params import IntentUpdatePolicyParams
from ..types.intent_update_wallet_params import IntentUpdateWalletParams
from ..types.rule_delete_intent_response import RuleDeleteIntentResponse
from ..types.rule_mutate_intent_response import RuleMutateIntentResponse
from ..types.intent_update_key_quorum_params import IntentUpdateKeyQuorumParams
from ..types.intent_create_policy_rule_params import IntentCreatePolicyRuleParams
from ..types.intent_update_policy_rule_params import IntentUpdatePolicyRuleParams

__all__ = ["PrivyIntentsService"]


class PrivyIntentsService(IntentsResource):
    """Intent operations with client-level request-expiry defaults."""

    def __init__(
        self,
        client: PrivyAPI,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._request_expiry_provider = request_expiry_provider

    def _expiry_header(
        self,
        request_options: PrivyRequestOptions | None,
        body: dict[str, object] | None = None,
    ) -> str | Omit:
        options = request_options or PrivyRequestOptions()
        raw_request_expiry = body.pop("privy_request_expiry", None) if body is not None else None
        if options.request_expiry is not None:
            return str(options.request_expiry)
        if raw_request_expiry is not None:
            return str(raw_request_expiry)
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        return str(request_expiry) if request_expiry is not None else omit

    def rpc(
        self,
        wallet_id: str,
        *,
        intent_rpc_request_body: IntentRpcParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> RpcIntentResponse:
        body = dict(intent_rpc_request_body)
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        rpc = cast(Callable[..., RpcIntentResponse], generated.rpc)
        return rpc(
            wallet_id,
            **body,
            privy_request_expiry=expiry_header,
        )

    def transfer(
        self,
        wallet_id: str,
        *,
        intent_transfer_params: IntentTransferParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> TransferIntentResponse:
        body = dict(intent_transfer_params)
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        transfer = cast(Callable[..., TransferIntentResponse], generated.transfer)
        return transfer(
            wallet_id,
            **body,
            privy_request_expiry=expiry_header,
        )

    def create_policy_rule(
        self,
        policy_id: str,
        *,
        intent_create_policy_rule_params: IntentCreatePolicyRuleParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> RuleMutateIntentResponse:
        body = dict(intent_create_policy_rule_params)
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        create_policy_rule = cast(Callable[..., RuleMutateIntentResponse], generated.create_policy_rule)
        return create_policy_rule(
            policy_id,
            **body,
            privy_request_expiry=expiry_header,
        )

    def delete_policy_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        request_options: PrivyRequestOptions | None = None,
    ) -> RuleDeleteIntentResponse:
        generated: Any = super()
        delete_policy_rule = cast(Callable[..., RuleDeleteIntentResponse], generated.delete_policy_rule)
        return delete_policy_rule(
            rule_id,
            policy_id=policy_id,
            privy_request_expiry=self._expiry_header(request_options),
        )

    def update_policy(
        self,
        policy_id: str,
        *,
        intent_update_policy_params: IntentUpdatePolicyParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> PolicyIntentResponse:
        body = dict(intent_update_policy_params)
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        update_policy = cast(Callable[..., PolicyIntentResponse], generated.update_policy)
        return update_policy(
            policy_id,
            **body,
            privy_request_expiry=expiry_header,
        )

    def update_policy_rule(
        self,
        rule_id: str,
        *,
        intent_update_policy_rule_params: IntentUpdatePolicyRuleParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> RuleMutateIntentResponse:
        body = dict(intent_update_policy_rule_params)
        policy_id = cast(str, body.pop("policy_id"))
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        update_policy_rule = cast(Callable[..., RuleMutateIntentResponse], generated.update_policy_rule)
        return update_policy_rule(
            rule_id,
            policy_id=policy_id,
            **body,
            privy_request_expiry=expiry_header,
        )

    def update_wallet(
        self,
        wallet_id: str,
        *,
        intent_update_wallet_params: IntentUpdateWalletParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> WalletIntentResponse:
        body = dict(intent_update_wallet_params)
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        update_wallet = cast(Callable[..., WalletIntentResponse], generated.update_wallet)
        return update_wallet(
            wallet_id,
            **body,
            privy_request_expiry=expiry_header,
        )

    def update_key_quorum(
        self,
        key_quorum_id: str,
        *,
        intent_update_key_quorum_params: IntentUpdateKeyQuorumParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> KeyQuorumIntentResponse:
        body = dict(intent_update_key_quorum_params)
        expiry_header = self._expiry_header(request_options, body)
        generated: Any = super()
        update_key_quorum = cast(Callable[..., KeyQuorumIntentResponse], generated.update_key_quorum)
        return update_key_quorum(
            key_quorum_id,
            **body,
            privy_request_expiry=expiry_header,
        )
