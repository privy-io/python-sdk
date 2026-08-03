# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenOutput"]


class TokenOutput(BaseModel):
    """A Spark token output."""

    owner_public_key: str

    token_amount: str

    id: Optional[str] = None

    revocation_commitment: Optional[str] = None

    token_identifier: Optional[str] = None

    token_public_key: Optional[str] = None

    withdraw_bond_sats: Optional[float] = None

    withdraw_relative_block_locktime: Optional[float] = None
