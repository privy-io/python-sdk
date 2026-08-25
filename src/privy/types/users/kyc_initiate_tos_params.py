# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..kyx_provider import KyxProvider
from ..kyx_environment import KyxEnvironment

__all__ = ["KYCInitiateTosParams"]


class KYCInitiateTosParams(TypedDict, total=False):
    provider: Required[KyxProvider]
    """KYC/KYB provider identifier."""

    email: str
    """Email for the user. If not provided, falls back to the user's linked email."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""
