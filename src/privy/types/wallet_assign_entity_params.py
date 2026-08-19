# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .entity_id import EntityID
from .wallet_entity_type import WalletEntityType

__all__ = ["WalletAssignEntityParams"]


class WalletAssignEntityParams(TypedDict, total=False):
    id: Required[EntityID]
    """A Privy entity ID."""

    type: Required[WalletEntityType]
    """The type of entity a wallet is attributed to."""
