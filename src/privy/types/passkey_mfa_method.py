# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PasskeyMfaMethod"]


class PasskeyMfaMethod(BaseModel):
    """A Passkey MFA method."""

    type: Literal["passkey"]

    verified_at: float
