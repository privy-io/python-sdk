# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .mfa_method import MfaMethod

__all__ = ["MfaEnabledWebhookPayload"]


class MfaEnabledWebhookPayload(BaseModel):
    """Payload for the mfa.enabled webhook event."""

    method: MfaMethod
    """A multi-factor authentication method supported by the app."""

    type: Literal["mfa.enabled"]
    """The type of webhook event."""

    user_id: str
    """The ID of the user who enabled MFA."""
