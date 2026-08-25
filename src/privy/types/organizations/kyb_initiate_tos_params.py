# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..kyx_provider import KyxProvider
from ..kyx_environment import KyxEnvironment

__all__ = ["KYBInitiateTosParams"]


class KYBInitiateTosParams(TypedDict, total=False):
    email: Required[str]
    """Email address for the organization."""

    provider: Required[KyxProvider]
    """KYC/KYB provider identifier."""

    business_name: str
    """Legal name of the business."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""
