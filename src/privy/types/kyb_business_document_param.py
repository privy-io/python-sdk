# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .kyb_document_purpose import KYBDocumentPurpose

__all__ = ["KYBBusinessDocumentParam"]


class KYBBusinessDocumentParam(TypedDict, total=False):
    """A supporting document for business verification."""

    file: Required[str]
    """Base64-encoded data URI of the document."""

    purposes: Required[SequenceNotStr[KYBDocumentPurpose]]
    """What this document evidences. Supports multiple purposes per file."""

    description: str
    """Document description. Required when "other" is one of the purposes."""
