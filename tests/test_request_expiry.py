from __future__ import annotations

import json
from unittest.mock import patch

from privy import (
    PrivyClient,
    PrivyRequestOptions,
    AuthorizationContext,
    PrivyRequestExpiryOptions,
    omit,
    prepare_request,
)

BASE_URL = "https://api.example.com"
NOW_MS = 1_000_000
FIFTEEN_MINUTES_MS = 15 * 60 * 1000


def make_client(request_expiry: PrivyRequestExpiryOptions | None = None) -> PrivyClient:
    return PrivyClient(
        app_id="app-id",
        app_secret="app-secret",
        base_url=BASE_URL,
        request_expiry=request_expiry,
    )


def test_get_request_expiry_uses_default_and_custom_durations() -> None:
    client = make_client()
    try:
        with patch("privy.lib.client.time.time_ns", return_value=NOW_MS * 1_000_000):
            assert client.get_request_expiry() == NOW_MS + FIFTEEN_MINUTES_MS
            assert client.get_request_expiry(1234) == NOW_MS + 1234
    finally:
        client.close()


def test_get_request_expiry_uses_client_configuration() -> None:
    client = make_client(PrivyRequestExpiryOptions(default_ms=1234))
    try:
        with patch("privy.lib.client.time.time_ns", return_value=NOW_MS * 1_000_000):
            assert client.get_request_expiry() == NOW_MS + 1234
    finally:
        client.close()


def test_get_request_expiry_can_be_disabled() -> None:
    client = make_client(PrivyRequestExpiryOptions(disabled=True))
    try:
        assert client.get_request_expiry() is None
        assert client.get_request_expiry(1234) is None
    finally:
        client.close()


def test_prepare_request_signs_and_returns_the_same_expiry() -> None:
    payloads: list[bytes] = []
    prepared = prepare_request(
        app_id="app-id",
        method="POST",
        url=f"{BASE_URL}/v1/wallets/wallet-id/rpc",
        body={"method": "personal_sign"},
        authorization_context=AuthorizationContext(signers=[lambda payload: payloads.append(payload) or "signature"]),
        request_expiry=1234,
    )

    assert prepared.headers == {
        "privy-authorization-signature": "signature",
        "privy-request-expiry": "1234",
    }
    assert json.loads(payloads[0])["headers"] == {
        "privy-app-id": "app-id",
        "privy-request-expiry": "1234",
    }


def test_prepare_request_returns_expiry_without_authorization_signatures() -> None:
    prepared = prepare_request(
        app_id="app-id",
        method="PATCH",
        url=f"{BASE_URL}/v1/wallets/wallet-id",
        body={},
        request_expiry=0,
    )

    assert prepared.headers == {"privy-request-expiry": "0"}


def test_wallet_rpc_uses_client_default_expiry() -> None:
    client = make_client(PrivyRequestExpiryOptions(default_ms=1234))
    try:
        with patch("privy.lib.client.time.time_ns", return_value=NOW_MS * 1_000_000):
            with patch.object(client.wallets, "_rpc", return_value=object()) as rpc_mock:
                client.wallets.rpc(
                    "wallet-id",
                    wallet_rpc_request_body={
                        "method": "personal_sign",
                        "chain_type": "ethereum",
                        "params": {"message": "hello", "encoding": "utf-8"},
                    },
                )

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] == str(NOW_MS + 1234)
    finally:
        client.close()


def test_explicit_expiry_wins_when_automatic_expiry_is_disabled() -> None:
    client = make_client(PrivyRequestExpiryOptions(disabled=True))
    try:
        with patch.object(client.wallets, "_rpc", return_value=object()) as rpc_mock:
            client.wallets.rpc(
                "wallet-id",
                wallet_rpc_request_body={
                    "method": "personal_sign",
                    "chain_type": "ethereum",
                    "params": {"message": "hello", "encoding": "utf-8"},
                },
                request_options=PrivyRequestOptions(request_expiry=4321),
            )

        assert rpc_mock.call_args.kwargs["privy_request_expiry"] == "4321"
    finally:
        client.close()


def test_disabled_expiry_is_omitted_from_non_wallet_services() -> None:
    client = make_client(PrivyRequestExpiryOptions(disabled=True))
    try:
        with patch.object(client.policies, "_delete_policy", return_value=object()) as policy_mock:
            with patch.object(client.key_quorums, "_delete_key_quorum", return_value=object()) as quorum_mock:
                client.policies.delete("policy-id")
                client.key_quorums.delete("key-quorum-id")

        assert policy_mock.call_args.kwargs["privy_request_expiry"] is omit
        assert quorum_mock.call_args.kwargs["privy_request_expiry"] is omit
    finally:
        client.close()
