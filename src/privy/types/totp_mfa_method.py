# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TotpMfaMethod"]


class TotpMfaMethod(BaseModel):
    """A TOTP MFA method."""

    type: Literal["totp"]

    verified_at: float
