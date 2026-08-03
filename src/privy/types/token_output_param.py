# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenOutputParam"]


class TokenOutputParam(TypedDict, total=False):
    """A Spark token output."""

    owner_public_key: Required[str]

    token_amount: Required[str]

    id: str

    revocation_commitment: str

    token_identifier: str

    token_public_key: str

    withdraw_bond_sats: float

    withdraw_relative_block_locktime: float
