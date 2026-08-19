# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .key_quorum_id import KeyQuorumID

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    default_key_quorum_id: KeyQuorumID
    """A unique identifier for a key quorum."""

    display_name: str
