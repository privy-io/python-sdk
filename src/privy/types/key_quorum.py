# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["KeyQuorum", "AuthorizationKey"]


class AuthorizationKey(BaseModel):
    display_name: Optional[str] = None

    public_key: str


class KeyQuorum(BaseModel):
    id: str

    authorization_keys: List[AuthorizationKey]

    authorization_threshold: Optional[float] = None

    display_name: Optional[str] = None

    user_ids: Optional[List[str]] = None
