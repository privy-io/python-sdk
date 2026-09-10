"""HPKE sender and recipient helpers for encrypted Privy API payloads."""

from __future__ import annotations

import base64

from pyhpke import KDFId, KEMId, AEADId, KEMKey, CipherSuite
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


class HPKESender:
    """RFC 9180 base-mode sender for Privy's fixed HPKE cipher suite."""

    def __init__(self) -> None:
        self._suite = CipherSuite.new(
            KEMId.DHKEM_P256_HKDF_SHA256,
            KDFId.HKDF_SHA256,
            AEADId.CHACHA20_POLY1305,
        )

    def encrypt(self, recipient_public_key: bytes, plaintext: bytes) -> tuple[bytes, bytes]:
        public_key: object
        if len(recipient_public_key) == 65 and recipient_public_key[0] == 4:
            public_key = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), recipient_public_key)
        else:
            public_key = serialization.load_der_public_key(recipient_public_key)
        if not isinstance(public_key, ec.EllipticCurvePublicKey) or not isinstance(public_key.curve, ec.SECP256R1):
            raise ValueError("HPKE recipient public key must be a P-256 public key")

        recipient_key = KEMKey.from_pyca_cryptography_key(public_key)
        encapsulated_key, context = self._suite.create_sender_context(recipient_key)
        return encapsulated_key, context.seal(plaintext)


class HPKERecipient:
    """RFC 9180 base-mode recipient for Privy's fixed HPKE cipher suite."""

    def __init__(self) -> None:
        self._private_key = ec.generate_private_key(ec.SECP256R1())
        self._hpke_private_key = KEMKey.from_pyca_cryptography_key(self._private_key)
        self._suite = CipherSuite.new(
            KEMId.DHKEM_P256_HKDF_SHA256,
            KDFId.HKDF_SHA256,
            AEADId.CHACHA20_POLY1305,
        )

    @property
    def public_key_spki(self) -> bytes:
        return self._private_key.public_key().public_bytes(
            serialization.Encoding.DER,
            serialization.PublicFormat.SubjectPublicKeyInfo,
        )

    @property
    def public_key_spki_base64(self) -> str:
        """Return the recipient public key as base64-encoded DER SPKI."""

        return base64.b64encode(self.public_key_spki).decode("ascii")

    def decrypt(self, encapsulated_key: bytes, ciphertext: bytes) -> bytes:
        context = self._suite.create_recipient_context(encapsulated_key, self._hpke_private_key)
        return context.open(ciphertext)

    def decrypt_base64(self, encapsulated_key: str, ciphertext: str) -> bytes:
        """Decrypt base64-encoded HPKE response fields."""

        return self.decrypt(
            base64.b64decode(encapsulated_key, validate=True),
            base64.b64decode(ciphertext, validate=True),
        )
