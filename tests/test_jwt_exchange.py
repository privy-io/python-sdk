from __future__ import annotations

import hmac
import base64
import hashlib
from typing import Any

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

from privy import PrivyAPIError
from privy.lib.jwt_exchange import JWTExchangeService
from privy.types.encrypted_authorization_key import EncryptedAuthorizationKey
from privy.types.raw_wallet_authenticate_response import RawWalletAuthenticateResponse
from privy.types.encrypted_wallet_authenticate_response import EncryptedWalletAuthenticateResponse

_HPKE_VERSION = b"HPKE-v1"
_KEM_SUITE_ID = b"KEM\x00\x10"
_HPKE_SUITE_ID = b"HPKE\x00\x10\x00\x01\x00\x03"


def _extract(salt: bytes, ikm: bytes) -> bytes:
    return hmac.new(salt or bytes(32), ikm, hashlib.sha256).digest()


def _expand(prk: bytes, info: bytes, length: int) -> bytes:
    output = previous = b""
    for counter in range(1, 256):
        previous = hmac.new(prk, previous + info + bytes([counter]), hashlib.sha256).digest()
        output += previous
        if len(output) >= length:
            return output[:length]
    raise AssertionError("invalid test HKDF length")


def _labeled_extract(suite_id: bytes, salt: bytes, label: bytes, ikm: bytes) -> bytes:
    return _extract(salt, _HPKE_VERSION + suite_id + label + ikm)


def _labeled_expand(suite_id: bytes, prk: bytes, label: bytes, info: bytes, length: int) -> bytes:
    return _expand(prk, length.to_bytes(2, "big") + _HPKE_VERSION + suite_id + label + info, length)


def _encrypt_for_recipient(recipient_public_key_spki: str, plaintext: bytes) -> tuple[str, str]:
    recipient_key = serialization.load_der_public_key(base64.b64decode(recipient_public_key_spki))
    assert isinstance(recipient_key, ec.EllipticCurvePublicKey)
    ephemeral_key = ec.generate_private_key(ec.SECP256R1())
    encapsulated_key = ephemeral_key.public_key().public_bytes(
        serialization.Encoding.X962,
        serialization.PublicFormat.UncompressedPoint,
    )
    recipient_public_key = recipient_key.public_bytes(
        serialization.Encoding.X962,
        serialization.PublicFormat.UncompressedPoint,
    )
    dh = ephemeral_key.exchange(ec.ECDH(), recipient_key)
    eae_prk = _labeled_extract(_KEM_SUITE_ID, b"", b"eae_prk", dh)
    shared_secret = _labeled_expand(
        _KEM_SUITE_ID,
        eae_prk,
        b"shared_secret",
        encapsulated_key + recipient_public_key,
        32,
    )
    psk_id_hash = _labeled_extract(_HPKE_SUITE_ID, b"", b"psk_id_hash", b"")
    info_hash = _labeled_extract(_HPKE_SUITE_ID, b"", b"info_hash", b"")
    context = b"\x00" + psk_id_hash + info_hash
    secret = _labeled_extract(_HPKE_SUITE_ID, shared_secret, b"secret", b"")
    key = _labeled_expand(_HPKE_SUITE_ID, secret, b"key", context, 32)
    nonce = _labeled_expand(_HPKE_SUITE_ID, secret, b"base_nonce", context, 12)
    ciphertext = ChaCha20Poly1305(key).encrypt(nonce, plaintext, b"")
    return base64.b64encode(encapsulated_key).decode(), base64.b64encode(ciphertext).decode()


class _Wallets:
    def __init__(self, authorization_key: str, expires_at: float = 4_000_000_000_000) -> None:
        self.authorization_key = authorization_key
        self.expires_at = expires_at
        self.calls: list[dict[str, Any]] = []

    def authenticate_with_jwt(self, **kwargs: Any) -> EncryptedWalletAuthenticateResponse:
        self.calls.append(kwargs)
        encapsulated_key, ciphertext = _encrypt_for_recipient(
            kwargs["recipient_public_key"],
            self.authorization_key.encode(),
        )
        return EncryptedWalletAuthenticateResponse(
            encrypted_authorization_key=EncryptedAuthorizationKey(
                encryption_type="HPKE",
                encapsulated_key=encapsulated_key,
                ciphertext=ciphertext,
            ),
            expires_at=self.expires_at,
            wallets=[],
        )


def test_exchange_jwt_requests_hpke_and_decrypts_authorization_key() -> None:
    wallets = _Wallets("base64-private-key")
    service = JWTExchangeService(wallets)  # type: ignore[arg-type]

    assert service.exchange_jwt_for_authorization_key("user.jwt") == "base64-private-key"
    assert wallets.calls[0]["user_jwt"] == "user.jwt"
    assert wallets.calls[0]["encryption_type"] == "HPKE"
    public_key = serialization.load_der_public_key(base64.b64decode(wallets.calls[0]["recipient_public_key"]))
    assert isinstance(public_key, ec.EllipticCurvePublicKey)
    assert isinstance(public_key.curve, ec.SECP256R1)


def test_exchange_jwt_caches_authorization_key_until_expiry() -> None:
    wallets = _Wallets("base64-private-key")
    service = JWTExchangeService(wallets)  # type: ignore[arg-type]

    assert service.exchange_jwt_for_authorization_key("user.jwt") == "base64-private-key"
    assert service.exchange_jwt_for_authorization_key("user.jwt") == "base64-private-key"
    assert len(wallets.calls) == 1


def test_exchange_jwt_does_not_reuse_expired_authorization_key() -> None:
    wallets = _Wallets("base64-private-key", expires_at=0)
    service = JWTExchangeService(wallets)  # type: ignore[arg-type]

    service.exchange_jwt_for_authorization_key("user.jwt")
    service.exchange_jwt_for_authorization_key("user.jwt")
    assert len(wallets.calls) == 2


def test_exchange_jwt_does_not_cache_when_cache_is_disabled() -> None:
    wallets = _Wallets("base64-private-key")
    service = JWTExchangeService(wallets, cache_max_capacity=None)  # type: ignore[arg-type]

    service.exchange_jwt_for_authorization_key("user.jwt")
    service.exchange_jwt_for_authorization_key("user.jwt")
    assert len(wallets.calls) == 2


def test_exchange_jwt_rejects_unencrypted_response() -> None:
    class RawWallets:
        def authenticate_with_jwt(self, **_: Any) -> RawWalletAuthenticateResponse:
            return RawWalletAuthenticateResponse(authorization_key="private-key", expires_at=0, wallets=[])

    service = JWTExchangeService(RawWallets())  # type: ignore[arg-type]

    with pytest.raises(PrivyAPIError, match="unsupported encryption type"):
        service.exchange_jwt_for_authorization_key("user.jwt")


def test_exchange_jwt_requires_positive_cache_capacity() -> None:
    with pytest.raises(ValueError, match="must be greater than zero"):
        JWTExchangeService(_Wallets("key"), cache_max_capacity=0)  # type: ignore[arg-type]
