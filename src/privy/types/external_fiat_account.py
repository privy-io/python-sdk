# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .environment import Environment

__all__ = ["ExternalFiatAccount"]


class ExternalFiatAccount(BaseModel):
    """A Bridge external fiat account linked to a user."""

    id: str

    account_owner_name: str

    account_type: str

    created_at: str

    currency: str

    environment: Environment
    """The Privy API environment."""

    provider: Literal["bridge"]
    """Discriminator: the external fiat account is orchestrated via Bridge."""

    user_id: str

    bank_name: Optional[str] = None

    last_4: Optional[str] = None
