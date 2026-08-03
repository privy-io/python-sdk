# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BaseActionResult"]


class BaseActionResult(BaseModel):
    """Common fields for intent action execution results."""

    executed_at: float
    """Unix timestamp when the action was executed"""

    status_code: float
    """HTTP status code from the action execution"""

    authorized_by_display_name: Optional[str] = None
    """Display name of the key quorum that authorized execution"""

    authorized_by_id: Optional[str] = None
    """ID of the key quorum that authorized execution"""
