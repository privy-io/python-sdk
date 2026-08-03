# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .p_256_public_key import P256PublicKey

__all__ = ["OwnerInputPublicKeyParam"]


class OwnerInputPublicKeyParam(TypedDict, total=False):
    """Owner input specifying a P-256 public key."""

    public_key: Required[P256PublicKey]
    """A P-256 (secp256r1) public key."""
