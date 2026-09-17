# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .kyb_individual_document_purpose import KYBIndividualDocumentPurpose

__all__ = ["KYBIndividualDocumentParam"]


class KYBIndividualDocumentParam(TypedDict, total=False):
    """A supporting document for an associated person."""

    file: Required[str]
    """Base64-encoded data URI of the document."""

    purposes: Required[SequenceNotStr[KYBIndividualDocumentPurpose]]
    """What this document evidences. Supports multiple purposes per file."""

    description: str
    """Document description. Required when "other" is one of the purposes."""
