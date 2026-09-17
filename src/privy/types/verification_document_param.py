# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerificationDocumentParam"]


class VerificationDocumentParam(TypedDict, total=False):
    """An identifying document for KYC or KYB verification.

    Also used for business identifiers such as tax and registration numbers, for which the image and expiration fields do not apply.
    """

    issuing_country: Required[str]
    """ISO 3166-1 alpha-3 issuing country code."""

    type: Required[str]
    """Document type identifier."""

    description: str
    """Document description."""

    expiration: str
    """Document expiration date."""

    image_back: str
    """Base64-encoded back image."""

    image_front: str
    """Base64-encoded front image."""

    number: str
    """Document number."""
