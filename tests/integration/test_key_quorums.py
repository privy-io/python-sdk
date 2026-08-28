from __future__ import annotations

import pytest

from privy import PrivyClient, PrivyRequestOptions, AuthorizationContext, generate_p256_key_pair

pytestmark = pytest.mark.integration


def test_update_with_authorization_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    key_quorum = privy_client.key_quorums.create(
        authorization_threshold=1,
        public_keys=[key_pair.public_key],
    )

    updated = privy_client.key_quorums.update(
        key_quorum.id,
        key_quorum_update_params={"display_name": "Updated key quorum"},
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert updated.id == key_quorum.id
    assert updated.display_name == "Updated key quorum"
