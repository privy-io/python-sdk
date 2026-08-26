from __future__ import annotations

import pytest

from privy import (
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    prepare_request,
    format_request_for_authorization_signature,
)


def _format_body(body: object) -> bytes:
    return format_request_for_authorization_signature(
        WalletAPIRequestSignatureInput(
            method="POST",
            url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
            body=body,
            headers={"privy-app-id": "app-123"},
        )
    )


def test_canonical_request_matches_cross_sdk_shape() -> None:
    payload = _format_body({"params": {"hash": "0x1234"}})

    assert payload == (
        b'{"body":{"params":{"hash":"0x1234"}},"headers":{"privy-app-id":"app-123"},'
        b'"method":"POST","url":"https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign","version":1}'
    )


@pytest.mark.parametrize("empty_body", [{}, []])
def test_empty_objects_and_arrays_are_formatted_as_empty_strings(empty_body: object) -> None:
    assert _format_body(empty_body).startswith(b'{"body":""')


def test_none_body_is_formatted_as_json_null() -> None:
    assert _format_body(None).startswith(b'{"body":null')


def test_authorization_context_accepts_precomputed_signatures() -> None:
    context = AuthorizationContext(signatures=["first", "second"])

    assert context.signatures == ["first", "second"]


def test_precomputed_signatures_are_forwarded_in_order() -> None:
    prepared = prepare_request(
        app_id="app-123",
        method="POST",
        url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
        body={"params": {"hash": "0x1234"}},
        authorization_context=AuthorizationContext(signatures=["first", "second"]),
    )

    assert prepared.headers == {"privy-authorization-signature": "first,second"}
