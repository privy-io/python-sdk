from __future__ import annotations

import pytest

from privy import (
    PrivyClient,
    PrivyRequestOptions,
    AuthorizationContext,
    generate_p256_key_pair,
)
from privy.types import policy_create_params
from privy.lib.authorization import P256KeyPair
from privy.types.policy_create_rule_params import PolicyCreateRuleParams
from privy.types.policy_update_rule_params import PolicyUpdateRuleParams

pytestmark = pytest.mark.integration


def build_rule() -> PolicyCreateRuleParams:
    return {
        "name": "Allow transfers to a known address",
        "method": "eth_sendTransaction",
        "action": "ALLOW",
        "conditions": [
            {
                "field_source": "ethereum_transaction",
                "field": "to",
                "operator": "eq",
                "value": "0x0000000000000000000000000000000000000001",
            }
        ],
    }


def initial_rule() -> policy_create_params.Rule:
    return {
        "name": "Allow transfers to a known address",
        "method": "eth_sendTransaction",
        "action": "ALLOW",
        "conditions": [
            {
                "field_source": "ethereum_transaction",
                "field": "to",
                "operator": "eq",
                "value": "0x0000000000000000000000000000000000000001",
            }
        ],
    }


def build_updated_rule(policy_id: str) -> PolicyUpdateRuleParams:
    return {
        "policy_id": policy_id,
        **build_rule(),
        "name": "Updated transfer rule",
    }


def request_options(key_pair: P256KeyPair) -> PrivyRequestOptions:
    return PrivyRequestOptions(
        authorization_context=AuthorizationContext(
            authorization_private_keys=[key_pair.private_key],
        )
    )


def test_update_and_rule_mutations(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    options = request_options(key_pair)
    policy = privy_client.policies.create(
        chain_type="ethereum",
        name="Python SDK policy mutation test",
        rules=[],
        version="1.0",
        owner={"public_key": key_pair.public_key},
    )

    try:
        assert privy_client.policies.get(policy.id).id == policy.id
        updated = privy_client.policies.update(
            policy.id,
            policy_update_params={"name": "Python SDK updated policy"},
            request_options=options,
        )
        assert updated.name == "Python SDK updated policy"

        rule = privy_client.policies.create_rule(
            policy.id,
            policy_create_rule_params=build_rule(),
            request_options=options,
        )
        assert privy_client.policies.get_rule(rule.id, policy_id=policy.id).id == rule.id

        updated_rule = privy_client.policies.update_rule(
            rule.id,
            policy_update_rule_params=build_updated_rule(policy.id),
            request_options=options,
        )
        assert updated_rule.id == rule.id
        assert updated_rule.name == "Updated transfer rule"
    finally:
        privy_client.policies.update(
            policy.id,
            policy_update_params={"owner": None},
            request_options=options,
        )
        privy_client.policies.delete(policy.id)


def test_delete_rule(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    options = request_options(key_pair)
    policy = privy_client.policies.create(
        chain_type="ethereum",
        name="Python SDK delete rule test",
        rules=[initial_rule()],
        version="1.0",
        owner={"public_key": key_pair.public_key},
    )

    try:
        result = privy_client.policies.delete_rule(
            policy.rules[0].id,
            policy_id=policy.id,
            request_options=options,
        )
        assert result.success is True
        assert privy_client.policies.get(policy.id).rules == []
    finally:
        privy_client.policies.update(
            policy.id,
            policy_update_params={"owner": None},
            request_options=options,
        )
        privy_client.policies.delete(policy.id)


def test_delete_owned_policy(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    policy = privy_client.policies.create(
        chain_type="ethereum",
        name="Python SDK delete policy test",
        rules=[],
        version="1.0",
        owner={"public_key": key_pair.public_key},
    )

    result = privy_client.policies.delete(
        policy.id,
        request_options=request_options(key_pair),
    )
    assert result.success is True
