# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletEntity"]


class WalletEntity(BaseModel):
    """The entity a wallet is attributed to."""

    id: str
    """The Privy entity ID."""

    type: Literal["user", "organization"]
