"""Request authorization primitives."""

from __future__ import annotations

import base64
from typing import Literal, Mapping, Callable, Protocol, Sequence, cast
from dataclasses import field, dataclass

import canonicaljson
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

__all__ = [
    "AuthorizationContext",
    "P256KeyPair",
    "PreparedRequest",
    "WalletAPIRequestSignatureInput",
    "format_request_for_authorization_signature",
    "generate_authorization_signature",
    "generate_authorization_signatures",
    "generate_p256_key_pair",
    "prepare_request",
]

MutationMethod = Literal["POST", "PUT", "PATCH", "DELETE"]
Signer = Callable[[bytes], str]


class JWTExchanger(Protocol):
    """Exchanges a user JWT for a short-lived authorization private key."""

    def exchange_jwt_for_authorization_key(self, jwt: str) -> str: ...


@dataclass(frozen=True)
class AuthorizationContext:
    """Credentials that contribute signatures to an authorized request.

    User JWTs are exchanged for short-lived authorization private keys before
    the request is signed.
    """

    signatures: Sequence[str] = field(default_factory=tuple)
    authorization_private_keys: Sequence[str] = field(default_factory=tuple)
    signers: Sequence[Signer] = field(default_factory=tuple)
    user_jwts: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class P256KeyPair:
    """A P-256 key pair encoded for Privy authorization."""

    public_key: str
    private_key: str


def generate_p256_key_pair() -> P256KeyPair:
    """Generate base64 DER SPKI/PKCS#8 P-256 keys without PEM headers."""

    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key_der = private_key.public_key().public_bytes(
        serialization.Encoding.DER,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    private_key_der = private_key.private_bytes(
        serialization.Encoding.DER,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    return P256KeyPair(
        public_key=base64.b64encode(public_key_der).decode("ascii"),
        private_key=base64.b64encode(private_key_der).decode("ascii"),
    )


def generate_authorization_signature(authorization_private_key: str, payload: bytes) -> str:
    """Sign payload bytes with a base64 DER PKCS#8 P-256 private key."""

    try:
        private_key_der = base64.b64decode(authorization_private_key, validate=True)
        private_key = serialization.load_der_private_key(private_key_der, password=None)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid authorization private key") from exc

    if not isinstance(private_key, ec.EllipticCurvePrivateKey) or not isinstance(private_key.curve, ec.SECP256R1):
        raise ValueError("Authorization private key must be a P-256 PKCS#8 private key")

    signature = private_key.sign(payload, ec.ECDSA(hashes.SHA256()))
    return base64.b64encode(signature).decode("ascii")


def generate_authorization_signatures(
    authorization_context: AuthorizationContext,
    payload: bytes,
    *,
    jwt_exchanger: JWTExchanger | None = None,
) -> list[str]:
    """Generate signatures for every credential in an authorization context."""

    if authorization_context.user_jwts and jwt_exchanger is None:
        raise ValueError("jwt_exchanger is required when user_jwts are provided")

    signatures = list(authorization_context.signatures)
    private_keys = list(authorization_context.authorization_private_keys)
    if jwt_exchanger is not None:
        private_keys.extend(
            jwt_exchanger.exchange_jwt_for_authorization_key(jwt) for jwt in authorization_context.user_jwts
        )
    signatures.extend(generate_authorization_signature(private_key, payload) for private_key in private_keys)
    signatures.extend(signer(payload) for signer in authorization_context.signers)
    return signatures


@dataclass(frozen=True)
class PreparedRequest:
    headers: Mapping[str, str]


@dataclass(frozen=True)
class WalletAPIRequestSignatureInput:
    """The canonical request facts covered by an authorization signature."""

    method: MutationMethod
    url: str
    body: object
    headers: Mapping[str, str]
    version: Literal[1] = 1

    def __post_init__(self) -> None:
        method = self.method.upper()
        if method not in {"POST", "PUT", "PATCH", "DELETE"}:
            raise ValueError(f"Unsupported authorization method: {self.method!r}")
        if not self.url.startswith(("https://", "http://")):
            raise ValueError("Authorization request URL must be absolute")
        if self.url.endswith("/"):
            raise ValueError("Authorization request URL must not have a trailing slash")
        if "privy-app-id" not in self.headers:
            raise ValueError("Authorization request headers must include privy-app-id")
        object.__setattr__(self, "method", cast("MutationMethod", method))


def format_request_for_authorization_signature(
    input: WalletAPIRequestSignatureInput, *, preserve_empty_body: bool = False
) -> bytes:
    """Return deterministic UTF-8 JSON bytes for an authorization request."""

    body = input.body
    if not preserve_empty_body and (
        (isinstance(body, Mapping) and not body) or (isinstance(body, (list, tuple)) and not body)
    ):
        body = ""
    payload: dict[str, object] = {
        "version": input.version,
        "method": input.method,
        "url": input.url,
        "body": body,
        "headers": dict(input.headers),
    }
    return canonicaljson.encode_canonical_json(payload)


def prepare_request(
    *,
    app_id: str,
    method: MutationMethod,
    url: str,
    body: object,
    authorization_context: AuthorizationContext | None = None,
    request_expiry: int | None = None,
    jwt_exchanger: JWTExchanger | None = None,
    preserve_empty_body: bool = False,
) -> PreparedRequest:
    """Prepare authorization headers for a generated API request."""

    context = authorization_context or AuthorizationContext()
    request_headers = {"privy-app-id": app_id}
    if request_expiry is not None:
        request_headers["privy-request-expiry"] = str(request_expiry)
    # Formatting is intentionally performed even for precomputed signatures so
    # every authorization-context path covers the same request representation.
    payload = format_request_for_authorization_signature(
        WalletAPIRequestSignatureInput(
            method=method,
            url=url,
            body=body,
            headers=request_headers,
        ),
        preserve_empty_body=preserve_empty_body,
    )
    signatures = generate_authorization_signatures(
        context,
        payload,
        jwt_exchanger=jwt_exchanger,
    )
    headers: dict[str, str] = {}
    if signatures:
        headers["privy-authorization-signature"] = ",".join(signatures)
    if request_expiry is not None:
        headers["privy-request-expiry"] = str(request_expiry)
    return PreparedRequest(headers=headers)
