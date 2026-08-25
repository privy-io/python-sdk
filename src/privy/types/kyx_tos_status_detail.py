# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .kyx_tos_status import KyxTosStatus

__all__ = ["KyxTosStatusDetail"]


class KyxTosStatusDetail(BaseModel):
    """Terms of Service acceptance status for a KYC or KYB flow."""

    status: KyxTosStatus
    """Status of Terms of Service acceptance. Passthrough from the provider."""

    link: Optional[str] = None
    """ToS acceptance link, if pending."""
