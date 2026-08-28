from __future__ import annotations

import pytest

from privy import PrivyClient, PrivyRequestOptions, AuthorizationContext, generate_p256_key_pair

pytestmark = pytest.mark.integration


def test_update_with_authorization_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    policy = privy_client.policies.create(
        chain_type="ethereum",
        name="Python SDK update test",
        rules=[],
        version="1.0",
        owner={"public_key": key_pair.public_key},
    )

    updated = privy_client.policies.update(
        policy.id,
        policy_update_params={"name": "Updated policy"},
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert updated.id == policy.id
    assert updated.name == "Updated policy"
