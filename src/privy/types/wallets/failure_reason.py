# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FailureReason"]


class FailureReason(BaseModel):
    """A description of why a wallet action (or a step within a wallet action) failed."""

    message: str
    """Human-readable failure message."""

    details: Optional[object] = None
    """Additional error details, if available."""
