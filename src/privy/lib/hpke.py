import base64
from typing import TypedDict, cast

from pyhpke import KDFId, KEMId, AEADId, KEMKey, CipherSuite
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey


class SealOutput(TypedDict):
    encapsulated_key: str
    ciphertext: str


def seal(public_key: str, message: str) -> SealOutput:
    """Encrypts a UTF-8 message using HPKE with P-256 and ChaCha20-Poly1305.

    Args:
        public_key: Base64-encoded DER-formatted P-256 public key
        message: UTF-8 string to encrypt

    Returns:
        SealOutput: A dictionary containing:
            - encapsulated_key: Base64-encoded encapsulated key
            - ciphertext: Base64-encoded encrypted message
    """
    # The sender side:
    suite = CipherSuite.new(KEMId.DHKEM_P256_HKDF_SHA256, KDFId.HKDF_SHA256, AEADId.CHACHA20_POLY1305)

    decoded_public_key = base64.b64decode(public_key)
    kem_key = KEMKey.from_pem(decoded_public_key)

    enc, sender = suite.create_sender_context(kem_key)
    ct = sender.seal(message.encode("utf-8"))

    return {
        "encapsulated_key": base64.b64encode(enc).decode("utf-8"),
        "ciphertext": base64.b64encode(ct).decode("utf-8"),
    }


class OpenOutput(TypedDict):
    message: str


def open(private_key: str, encapsulated_key: str, ciphertext: str) -> OpenOutput:
    """Decrypts a message using HPKE with P-256 and ChaCha20-Poly1305.

    Args:
        private_key: Base64-encoded DER-formatted P-256 private key
        encapsulated_key: Base64-encoded encapsulated key from seal()
        ciphertext: Base64-encoded encrypted message from seal()

    Returns:
        OpenOutput: A dictionary containing:
            - message: Decrypted UTF-8 string

    Note:
        The private key must be the corresponding key pair to the public key used in seal()
    """
    # Initialize the cipher suite
    suite = CipherSuite.new(KEMId.DHKEM_P256_HKDF_SHA256, KDFId.HKDF_SHA256, AEADId.CHACHA20_POLY1305)

    # Convert base64 to bytes
    raw_public_key = base64.b64decode(encapsulated_key)
    private_key_bytes = base64.b64decode(private_key)
    ciphertext_bytes = base64.b64decode(ciphertext)

    # Import private key
    loaded_private_key = cast(
        EllipticCurvePrivateKey, serialization.load_der_private_key(private_key_bytes, password=None)
    )
    private_number = loaded_private_key.private_numbers().private_value
    private_bytes = private_number.to_bytes(32, byteorder="big")
    private_kem_key = suite.kem.deserialize_private_key(private_bytes)

    # Create recipient context and decrypt
    encapsulated_kem_key = suite.kem.deserialize_public_key(raw_public_key)
    recipient_context = suite.create_recipient_context(encapsulated_kem_key.to_public_bytes(), private_kem_key)

    # Decrypt and return as UTF-8 string
    return {
        "message": recipient_context.open(ciphertext_bytes).decode("utf-8"),
    }


class KeyPair(TypedDict):
    public_key: str
    private_key: str


def generate_keypair() -> KeyPair:
    """Generates a new P-256 key pair for HPKE.

    Returns:
        KeyPair: A dictionary containing:
            - public_key: Base64-encoded DER-formatted P-256 public key
            - private_key: Base64-encoded DER-formatted P-256 private key
    """
    # Generate the key pair
    private_key_obj = ec.generate_private_key(ec.SECP256R1(), backend=default_backend())
    public_key_obj = private_key_obj.public_key()

    # Convert to base64 format
    public_key = base64.b64encode(
        public_key_obj.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    ).decode("utf-8")
    private_key = base64.b64encode(
        private_key_obj.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    ).decode("utf-8")

    return {
        "public_key": public_key,
        "private_key": private_key,
    }
