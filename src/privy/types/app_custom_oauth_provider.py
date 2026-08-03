# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .custom_oauth_provider_id import CustomOAuthProviderID

__all__ = ["AppCustomOAuthProvider"]


class AppCustomOAuthProvider(BaseModel):
    """A custom OAuth provider configured for an app."""

    enabled: bool

    provider: CustomOAuthProviderID
    """The ID of a custom OAuth provider, set up for this app.

    Must start with "custom:".
    """

    provider_display_name: str

    provider_icon_url: str
