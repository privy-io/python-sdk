# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .mfa_method import MfaMethod

__all__ = ["MfaDisabledWebhookPayload"]


class MfaDisabledWebhookPayload(BaseModel):
    """Payload for the mfa.disabled webhook event."""

    method: MfaMethod
    """A multi-factor authentication method supported by the app."""

    type: Literal["mfa.disabled"]
    """The type of webhook event."""

    user_id: str
    """The ID of the user who disabled MFA."""
