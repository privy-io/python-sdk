"""The HPKE recipient used by the JWT authorization-key exchange."""

from __future__ import annotations

from pyhpke import KDFId, KEMId, AEADId, KEMKey, CipherSuite
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


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

    def decrypt(self, encapsulated_key: bytes, ciphertext: bytes) -> bytes:
        context = self._suite.create_recipient_context(encapsulated_key, self._hpke_private_key)
        return context.open(ciphertext)
