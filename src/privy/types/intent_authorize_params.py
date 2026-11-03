# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntentAuthorizeParams"]


class IntentAuthorizeParams(TypedDict, total=False):
    signature: Required[str]
    """Signature authorizing the intent."""

    timestamp: Required[float]
    """Unix timestamp (in milliseconds) when the signature was created.

    Used to verify the signature was created when the signing key was valid.
    """
