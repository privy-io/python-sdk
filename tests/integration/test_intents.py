from __future__ import annotations

import time

import pytest

from privy import (
    DEFAULT_INTENT_REQUEST_EXPIRY_MS,
    PrivyClient,
    PrivyRequestOptions,
    AuthorizationContext,
    PrivyRequestExpiryOptions,
    generate_p256_key_pair,
)
from privy.types.policy import Policy
from privy.lib.authorization import P256KeyPair
from privy.types.base_intent_response import BaseIntentResponse
from privy.types.intent_transfer_params import IntentTransferParams
from privy.types.condition_set_items_request_body_param import ConditionSetItemsRequestBodyParam

from .conftest import staging_client

pytestmark = pytest.mark.integration

RAW_SIGN_HASH = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
TRANSFER_PARAMS: IntentTransferParams = {
    "source": {"asset": "usdc", "amount": "0.01", "chain": "base"},
    "destination": {"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
}
ONE_HOUR_MS = 60 * 60 * 1000
TOLERANCE_MS = 5 * 60 * 1000


def now_ms() -> int:
    return time.time_ns() // 1_000_000


def expires_at_ms(intent: BaseIntentResponse) -> float:
    """``expires_at`` is a Unix timestamp; accept seconds or milliseconds."""

    return intent.expires_at * 1000 if intent.expires_at < 1e12 else intent.expires_at


def assert_default_expiry(
    intent: BaseIntentResponse, before: int, after: int, default_ms: int = DEFAULT_INTENT_REQUEST_EXPIRY_MS
) -> None:
    # custom_expiry shows the client sent the expiry, so the server default cannot satisfy this.
    assert intent.custom_expiry is True
    assert before + default_ms - TOLERANCE_MS <= expires_at_ms(intent)
    assert expires_at_ms(intent) <= after + default_ms + TOLERANCE_MS


def assert_custom_expiry(intent: BaseIntentResponse, expiry: int) -> None:
    assert intent.custom_expiry is True
    assert abs(expires_at_ms(intent) - expiry) <= TOLERANCE_MS


def authorization_options(key_pair: P256KeyPair) -> PrivyRequestOptions:
    return PrivyRequestOptions(
        authorization_context=AuthorizationContext(authorization_private_keys=[key_pair.private_key])
    )


def create_owned_policy(privy_client: PrivyClient, key_pair: P256KeyPair) -> Policy:
    return privy_client.policies.create(
        chain_type="ethereum",
        name="Python SDK delete policy intent test",
        rules=[],
        version="1.0",
        owner={"public_key": key_pair.public_key},
    )


def delete_owned_policy(privy_client: PrivyClient, policy_id: str, key_pair: P256KeyPair) -> None:
    privy_client.policies.update(
        policy_id,
        policy_update_params={"owner": None},
        request_options=authorization_options(key_pair),
    )
    privy_client.policies.delete(policy_id)


@pytest.fixture(scope="module")
def wallet_id(privy_client: PrivyClient) -> str:
    # raw_sign does not support ethereum or solana wallets, so use tron (as in test_wallets.py).
    wallet = privy_client.wallets.create(chain_type="tron", owner={"public_key": generate_p256_key_pair().public_key})
    return wallet.id


def test_raw_sign_defaults_to_the_72_hour_intent_expiry(privy_client: PrivyClient, wallet_id: str) -> None:
    before = now_ms()
    intent = privy_client.intents.raw_sign(wallet_id, params={"hash": RAW_SIGN_HASH})
    after = now_ms()

    assert intent.intent_type == "RAW_SIGN"
    assert_default_expiry(intent, before, after)


def test_raw_sign_uses_the_configured_intent_expiry_default(wallet_id: str) -> None:
    default_intent_ms = 2 * ONE_HOUR_MS
    with staging_client(request_expiry=PrivyRequestExpiryOptions(default_intent_ms=default_intent_ms)) as client:
        before = now_ms()
        intent = client.intents.raw_sign(wallet_id, params={"hash": RAW_SIGN_HASH})
        after = now_ms()

    assert_default_expiry(intent, before, after, default_ms=default_intent_ms)


def test_raw_sign_uses_a_per_call_request_expiry(privy_client: PrivyClient, wallet_id: str) -> None:
    expiry = privy_client.get_intent_request_expiry(ONE_HOUR_MS)
    assert expiry is not None

    intent = privy_client.intents.raw_sign(
        wallet_id,
        params={"hash": RAW_SIGN_HASH},
        request_options=PrivyRequestOptions(request_expiry=expiry),
    )

    assert_custom_expiry(intent, expiry)


def test_delete_policy_defaults_to_the_72_hour_intent_expiry(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    policy = create_owned_policy(privy_client, key_pair)

    try:
        before = now_ms()
        intent = privy_client.intents.delete_policy(policy.id)
        after = now_ms()

        assert intent.intent_type == "POLICY"
        assert_default_expiry(intent, before, after)
    finally:
        delete_owned_policy(privy_client, policy.id, key_pair)


def test_delete_policy_uses_a_per_call_request_expiry(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    policy = create_owned_policy(privy_client, key_pair)
    expiry = privy_client.get_intent_request_expiry(ONE_HOUR_MS)
    assert expiry is not None

    try:
        intent = privy_client.intents.delete_policy(
            policy.id,
            request_options=PrivyRequestOptions(request_expiry=expiry),
        )

        assert_custom_expiry(intent, expiry)
    finally:
        delete_owned_policy(privy_client, policy.id, key_pair)


def test_delete_key_quorum_defaults_to_the_72_hour_intent_expiry(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    key_quorum = privy_client.key_quorums.create(
        authorization_threshold=1,
        display_name="Python SDK delete key quorum intent test",
        public_keys=[key_pair.public_key],
    )

    try:
        before = now_ms()
        intent = privy_client.intents.delete_key_quorum(key_quorum.id)
        after = now_ms()

        assert intent.intent_type == "KEY_QUORUM"
        assert_default_expiry(intent, before, after)
    finally:
        privy_client.key_quorums.delete(key_quorum.id, request_options=authorization_options(key_pair))


@pytest.mark.skip(reason="The staging wallet is unfunded, so transfer intents fail with insufficient balance")
def test_transfer_defaults_to_the_72_hour_intent_expiry(privy_client: PrivyClient, wallet_id: str) -> None:
    before = now_ms()
    intent = privy_client.intents.transfer(wallet_id, intent_transfer_params=TRANSFER_PARAMS)
    after = now_ms()

    assert intent.intent_type == "TRANSFER"
    assert_default_expiry(intent, before, after)


@pytest.mark.skip(reason="Requires an existing condition set, and PrivyClient cannot create one")
def test_condition_set_intents_use_the_intent_expiry(privy_client: PrivyClient) -> None:
    condition_set_id = "condition-set-id"
    items: ConditionSetItemsRequestBodyParam = [{"value": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"}]

    before = now_ms()
    created = privy_client.intents.create_condition_set_items(condition_set_id, condition_set_items_request_body=items)
    deleted = privy_client.intents.delete_condition_set(condition_set_id)
    after = now_ms()
    assert_default_expiry(created, before, after)
    assert_default_expiry(deleted, before, after)

    expiry = privy_client.get_intent_request_expiry(ONE_HOUR_MS)
    assert expiry is not None
    updated = privy_client.intents.update_condition_set_items(
        condition_set_id,
        condition_set_items_request_body=items,
        request_options=PrivyRequestOptions(request_expiry=expiry),
    )
    deleted_item = privy_client.intents.delete_condition_set_item(
        "condition-set-item-id",
        condition_set_id=condition_set_id,
        request_options=PrivyRequestOptions(request_expiry=expiry),
    )
    assert_custom_expiry(updated, expiry)
    assert_custom_expiry(deleted_item, expiry)
