"""Request authorization primitives."""

from __future__ import annotations

from typing import Literal, Mapping, Sequence, cast
from dataclasses import field, dataclass

import canonicaljson

__all__ = [
    "AuthorizationContext",
    "WalletAPIRequestSignatureInput",
    "format_request_for_authorization_signature",
]

MutationMethod = Literal["POST", "PUT", "PATCH", "DELETE"]


@dataclass(frozen=True)
class AuthorizationContext:
    """Credentials that contribute signatures to an authorized request."""

    signatures: Sequence[str] = field(default_factory=tuple)


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


def format_request_for_authorization_signature(input: WalletAPIRequestSignatureInput) -> bytes:
    """Return deterministic UTF-8 JSON bytes for an authorization request."""

    body = input.body
    if (isinstance(body, Mapping) and not body) or (isinstance(body, (list, tuple)) and not body):
        body = ""
    payload: dict[str, object] = {
        "version": input.version,
        "method": input.method,
        "url": input.url,
        "body": body,
        "headers": dict(input.headers),
    }
    return canonicaljson.encode_canonical_json(payload)
