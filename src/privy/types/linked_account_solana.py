# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountSolana"]


class LinkedAccountSolana(BaseModel):
    """A Solana wallet account linked to the user."""

    address: str

    chain_type: Literal["solana"]

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["wallet"]

    verified_at: float

    wallet_client: Literal["unknown"]

    connector_type: Optional[str] = None

    wallet_client_type: Optional[str] = None
