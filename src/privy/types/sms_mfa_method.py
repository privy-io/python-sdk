# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SMSMfaMethod"]


class SMSMfaMethod(BaseModel):
    """A SMS MFA method."""

    type: Literal["sms"]

    verified_at: float
