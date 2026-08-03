# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OwnerInputUser"]


class OwnerInputUser(BaseModel):
    """Owner input specifying a Privy user ID."""

    user_id: str
