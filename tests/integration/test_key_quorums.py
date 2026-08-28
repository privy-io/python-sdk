from __future__ import annotations

import pytest

from privy import PrivyClient, NotFoundError, PrivyRequestOptions, AuthorizationContext, generate_p256_key_pair

pytestmark = pytest.mark.integration


def authorization_options(*private_keys: str) -> PrivyRequestOptions:
    return PrivyRequestOptions(
        authorization_context=AuthorizationContext(
            authorization_private_keys=private_keys,
        )
    )


def test_create_and_get(privy_client: PrivyClient) -> None:
    first_key_pair = generate_p256_key_pair()
    second_key_pair = generate_p256_key_pair()
    key_quorum = privy_client.key_quorums.create(
        authorization_threshold=2,
        display_name="Python SDK create test",
        public_keys=[first_key_pair.public_key, second_key_pair.public_key],
    )

    try:
        fetched = privy_client.key_quorums.get(key_quorum.id)

        assert fetched.id == key_quorum.id
        assert fetched.display_name == "Python SDK create test"
        assert fetched.authorization_threshold == 2
        assert {key.public_key for key in fetched.authorization_keys} == {
            first_key_pair.public_key,
            second_key_pair.public_key,
        }
    finally:
        privy_client.key_quorums.delete(
            key_quorum.id,
            request_options=authorization_options(first_key_pair.private_key, second_key_pair.private_key),
        )


def test_update_with_authorization_private_keys(privy_client: PrivyClient) -> None:
    first_key_pair = generate_p256_key_pair()
    second_key_pair = generate_p256_key_pair()
    key_quorum = privy_client.key_quorums.create(
        authorization_threshold=2,
        display_name="Python SDK update test",
        public_keys=[first_key_pair.public_key, second_key_pair.public_key],
    )

    try:
        updated = privy_client.key_quorums.update(
            key_quorum.id,
            key_quorum_update_params={"authorization_threshold": 1},
            request_options=authorization_options(first_key_pair.private_key, second_key_pair.private_key),
        )

        assert updated.id == key_quorum.id
        assert updated.authorization_threshold == 1

        restored = privy_client.key_quorums.update(
            key_quorum.id,
            key_quorum_update_params={"authorization_threshold": 2},
            request_options=authorization_options(first_key_pair.private_key),
        )

        assert restored.id == key_quorum.id
        assert restored.authorization_threshold == 2
    finally:
        privy_client.key_quorums.delete(
            key_quorum.id,
            request_options=authorization_options(first_key_pair.private_key, second_key_pair.private_key),
        )


def test_delete_with_authorization_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    key_quorum = privy_client.key_quorums.create(
        authorization_threshold=1,
        display_name="Python SDK delete test",
        public_keys=[key_pair.public_key],
    )

    deleted = privy_client.key_quorums.delete(
        key_quorum.id,
        request_options=authorization_options(key_pair.private_key),
    )

    assert deleted.success is True
    with pytest.raises(NotFoundError):
        privy_client.key_quorums.get(key_quorum.id)
