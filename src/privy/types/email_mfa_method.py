# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailMfaMethod"]


class EmailMfaMethod(BaseModel):
    """An Email MFA method."""

    type: Literal["email"]

    verified_at: float
