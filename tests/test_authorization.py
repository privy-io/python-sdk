from __future__ import annotations

import base64

import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

from privy import (
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    prepare_request,
    generate_p256_key_pair,
    generate_authorization_signature,
    generate_authorization_signatures,
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


def test_authorization_context_accepts_user_jwts() -> None:
    context = AuthorizationContext(user_jwts=["first.jwt", "second.jwt"])

    assert context.user_jwts == ["first.jwt", "second.jwt"]


def test_precomputed_signatures_are_forwarded_in_order() -> None:
    prepared = prepare_request(
        app_id="app-123",
        method="POST",
        url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
        body={"params": {"hash": "0x1234"}},
        authorization_context=AuthorizationContext(signatures=["first", "second"]),
    )

    assert prepared.headers == {"privy-authorization-signature": "first,second"}


def test_idempotency_key_is_signed_and_forwarded() -> None:
    payloads: list[bytes] = []
    prepared = prepare_request(
        app_id="app-123",
        method="POST",
        url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
        body={"params": {"hash": "0x1234"}},
        idempotency_key="request-123",
        authorization_context=AuthorizationContext(signers=[lambda payload: payloads.append(payload) or "signed"]),
    )

    assert prepared.headers == {
        "privy-authorization-signature": "signed",
        "privy-idempotency-key": "request-123",
    }
    assert b'"privy-idempotency-key":"request-123"' in payloads[0]


def test_empty_body_can_be_preserved_for_delete_signatures() -> None:
    payloads: list[bytes] = []
    prepare_request(
        app_id="app-123",
        method="DELETE",
        url="https://api.staging.privy.io/v1/policies/policy-1",
        body={},
        authorization_context=AuthorizationContext(signers=[lambda payload: payloads.append(payload) or "signed"]),
        preserve_empty_body=True,
    )

    assert payloads[0].startswith(b'{"body":{}')


def test_p256_key_pair_uses_spki_and_pkcs8_der_formats() -> None:
    key_pair = generate_p256_key_pair()

    public_key = serialization.load_der_public_key(base64.b64decode(key_pair.public_key, validate=True))
    private_key = serialization.load_der_private_key(
        base64.b64decode(key_pair.private_key, validate=True), password=None
    )

    assert isinstance(public_key, ec.EllipticCurvePublicKey)
    assert isinstance(public_key.curve, ec.SECP256R1)
    assert isinstance(private_key, ec.EllipticCurvePrivateKey)
    assert isinstance(private_key.curve, ec.SECP256R1)
    assert private_key.public_key().public_numbers() == public_key.public_numbers()


def test_authorization_private_keys_sign_after_precomputed_signatures() -> None:
    key_pair = generate_p256_key_pair()
    prepared = prepare_request(
        app_id="app-123",
        method="POST",
        url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
        body={"params": {"hash": "0x1234"}},
        authorization_context=AuthorizationContext(
            signatures=["precomputed"],
            authorization_private_keys=[key_pair.private_key],
        ),
    )

    precomputed, generated = prepared.headers["privy-authorization-signature"].split(",")
    assert precomputed == "precomputed"
    public_key = serialization.load_der_public_key(base64.b64decode(key_pair.public_key))
    assert isinstance(public_key, ec.EllipticCurvePublicKey)
    public_key.verify(
        base64.b64decode(generated),
        format_request_for_authorization_signature(
            WalletAPIRequestSignatureInput(
                method="POST",
                url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
                body={"params": {"hash": "0x1234"}},
                headers={"privy-app-id": "app-123"},
            )
        ),
        ec.ECDSA(hashes.SHA256()),
    )


@pytest.mark.parametrize(
    "invalid_key_kind",
    ["not-base64", "not-der", "wrong-curve"],
)
def test_generate_authorization_signature_rejects_invalid_keys(invalid_key_kind: str) -> None:
    if invalid_key_kind == "not-base64":
        private_key = "not base64"
    elif invalid_key_kind == "not-der":
        private_key = base64.b64encode(b"not DER").decode("ascii")
    else:
        private_key = base64.b64encode(
            ec.generate_private_key(ec.SECP384R1()).private_bytes(
                serialization.Encoding.DER,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            )
        ).decode("ascii")

    with pytest.raises(ValueError, match="authorization private key|P-256"):
        generate_authorization_signature(private_key, b"payload")


def test_signers_receive_payload_and_sign_after_private_keys() -> None:
    key_pair = generate_p256_key_pair()
    received_payloads: list[bytes] = []

    def signer(payload: bytes) -> str:
        received_payloads.append(payload)
        return "callback"

    prepared = prepare_request(
        app_id="app-123",
        method="POST",
        url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
        body={"params": {"hash": "0x1234"}},
        authorization_context=AuthorizationContext(
            signatures=["precomputed"],
            authorization_private_keys=[key_pair.private_key],
            signers=[signer],
        ),
    )

    signatures = prepared.headers["privy-authorization-signature"].split(",")
    assert signatures[0] == "precomputed"
    assert signatures[2] == "callback"
    assert received_payloads == [
        format_request_for_authorization_signature(
            WalletAPIRequestSignatureInput(
                method="POST",
                url="https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign",
                body={"params": {"hash": "0x1234"}},
                headers={"privy-app-id": "app-123"},
            )
        )
    ]


def test_user_jwts_are_exchanged_and_sign_after_explicit_private_keys() -> None:
    explicit_key = generate_p256_key_pair()
    jwt_key = generate_p256_key_pair()

    class Exchanger:
        def __init__(self) -> None:
            self.jwts: list[str] = []

        def exchange_jwt_for_authorization_key(self, jwt: str) -> str:
            self.jwts.append(jwt)
            return jwt_key.private_key

    exchanger = Exchanger()
    payload = b"payload"
    signatures = generate_authorization_signatures(
        AuthorizationContext(
            signatures=["precomputed"],
            authorization_private_keys=[explicit_key.private_key],
            user_jwts=["user.jwt"],
            signers=[lambda _: "callback"],
        ),
        payload,
        jwt_exchanger=exchanger,
    )

    assert exchanger.jwts == ["user.jwt"]
    assert signatures[0] == "precomputed"
    assert signatures[3] == "callback"
    for key_pair, signature in zip((explicit_key, jwt_key), signatures[1:3]):
        public_key = serialization.load_der_public_key(base64.b64decode(key_pair.public_key))
        assert isinstance(public_key, ec.EllipticCurvePublicKey)
        public_key.verify(base64.b64decode(signature), payload, ec.ECDSA(hashes.SHA256()))


def test_user_jwts_require_an_exchanger() -> None:
    with pytest.raises(ValueError, match="jwt_exchanger is required"):
        generate_authorization_signatures(AuthorizationContext(user_jwts=["user.jwt"]), b"payload")
