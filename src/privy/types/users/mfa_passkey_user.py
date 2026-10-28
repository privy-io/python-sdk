# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MfaPasskeyUser"]


class MfaPasskeyUser(BaseModel):
    """User entity for a WebAuthn registration ceremony."""

    id: str

    display_name: str

    name: str
