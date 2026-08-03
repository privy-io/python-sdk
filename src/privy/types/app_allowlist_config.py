# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AppAllowlistConfig"]


class AppAllowlistConfig(BaseModel):
    """Configuration for the allowlist error page shown to users not on the allowlist."""

    cta_link: Optional[str] = None

    cta_text: Optional[str] = None

    error_detail: Optional[str] = None

    error_title: Optional[str] = None
