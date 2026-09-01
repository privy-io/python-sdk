from __future__ import annotations

from typing import Any, Callable, cast
from unittest.mock import patch

from privy import PrivyClient, IntentsService, PrivyRequestOptions, PrivyRequestExpiryOptions, omit
from privy.resources.intents import IntentsResource

BASE_URL = "https://api.example.com"
NOW_MS = 1_000_000
SEVENTY_TWO_HOURS_MS = 72 * 60 * 60 * 1000


def make_client(request_expiry: PrivyRequestExpiryOptions | None = None) -> PrivyClient:
    return PrivyClient(
        app_id="app-id",
        app_secret="app-secret",
        base_url=BASE_URL,
        request_expiry=request_expiry,
    )


def rpc(service: IntentsService, request_options: PrivyRequestOptions | None = None) -> object:
    return service.rpc(
        "wallet-id",
        intent_rpc_request_body={
            "method": "personal_sign",
            "params": {"message": "hello", "encoding": "utf-8"},
        },
        request_options=request_options,
    )


def test_intents_use_seventy_two_hour_default() -> None:
    client = make_client()
    try:
        with patch("privy.lib.client.time.time_ns", return_value=NOW_MS * 1_000_000):
            with patch.object(IntentsResource, "rpc", return_value=object()) as rpc_mock:
                rpc(client.intents)

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] == str(NOW_MS + SEVENTY_TWO_HOURS_MS)
    finally:
        client.close()


def test_intents_use_custom_client_default() -> None:
    client = make_client(PrivyRequestExpiryOptions(default_ms=1234, default_intent_ms=5678))
    try:
        with patch("privy.lib.client.time.time_ns", return_value=NOW_MS * 1_000_000):
            with patch.object(IntentsResource, "rpc", return_value=object()) as rpc_mock:
                rpc(client.intents)

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] == str(NOW_MS + 5678)
    finally:
        client.close()


def test_per_call_expiry_wins_when_automatic_expiry_is_disabled() -> None:
    client = make_client(PrivyRequestExpiryOptions(disabled=True))
    try:
        with patch.object(IntentsResource, "rpc", return_value=object()) as rpc_mock:
            rpc(client.intents, PrivyRequestOptions(request_expiry=1234))

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] == "1234"
    finally:
        client.close()


def test_disabled_intent_expiry_is_omitted() -> None:
    client = make_client(PrivyRequestExpiryOptions(disabled=True))
    try:
        with patch.object(IntentsResource, "rpc", return_value=object()) as rpc_mock:
            rpc(client.intents)

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] is omit
    finally:
        client.close()


def test_raw_expiry_param_is_forwarded_without_entering_the_body() -> None:
    client = make_client()
    try:
        with patch.object(IntentsResource, "rpc", return_value=object()) as rpc_mock:
            client.intents.rpc(
                "wallet-id",
                intent_rpc_request_body={
                    "method": "personal_sign",
                    "params": {"message": "hello", "encoding": "utf-8"},
                    "privy_request_expiry": "4321",
                },
            )

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] == "4321"
    finally:
        client.close()


def test_all_intent_mutations_apply_the_intent_expiry() -> None:
    client = make_client(PrivyRequestExpiryOptions(default_intent_ms=5678))
    service = client.intents
    any_params = cast(Any, {})
    operations: list[tuple[str, Callable[[], object]]] = [
        ("rpc", lambda: rpc(service)),
        (
            "transfer",
            lambda: service.transfer("wallet-id", intent_transfer_params=any_params),
        ),
        (
            "create_policy_rule",
            lambda: service.create_policy_rule("policy-id", intent_create_policy_rule_params=any_params),
        ),
        (
            "delete_policy_rule",
            lambda: service.delete_policy_rule("rule-id", policy_id="policy-id"),
        ),
        (
            "update_policy",
            lambda: service.update_policy("policy-id", intent_update_policy_params=any_params),
        ),
        (
            "update_policy_rule",
            lambda: service.update_policy_rule(
                "rule-id",
                intent_update_policy_rule_params=cast(Any, {"policy_id": "policy-id"}),
            ),
        ),
        (
            "update_wallet",
            lambda: service.update_wallet("wallet-id", intent_update_wallet_params=any_params),
        ),
        (
            "update_key_quorum",
            lambda: service.update_key_quorum("key-quorum-id", intent_update_key_quorum_params=any_params),
        ),
    ]

    try:
        with patch("privy.lib.client.time.time_ns", return_value=NOW_MS * 1_000_000):
            for method_name, operation in operations:
                with patch.object(IntentsResource, method_name, return_value=object()) as method_mock:
                    operation()
                    assert method_mock.call_args.kwargs["privy_request_expiry"] == str(NOW_MS + 5678)
    finally:
        client.close()
