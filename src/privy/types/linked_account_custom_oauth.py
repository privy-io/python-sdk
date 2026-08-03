# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .custom_oauth_provider_id import CustomOAuthProviderID

__all__ = ["LinkedAccountCustomOAuth"]


class LinkedAccountCustomOAuth(BaseModel):
    """A custom OAuth account linked to the user."""

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: CustomOAuthProviderID
    """The ID of a custom OAuth provider, set up for this app.

    Must start with "custom:".
    """

    verified_at: float

    email: Optional[str] = None

    name: Optional[str] = None

    profile_picture_url: Optional[str] = None

    username: Optional[str] = None
