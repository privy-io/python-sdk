# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .p_256_public_key import P256PublicKey

__all__ = ["OwnerInputPublicKey"]


class OwnerInputPublicKey(BaseModel):
    """Owner input specifying a P-256 public key."""

    public_key: P256PublicKey
    """A P-256 (secp256r1) public key."""
