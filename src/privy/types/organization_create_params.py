# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .key_quorum_id import KeyQuorumID

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    default_key_quorum_id: Required[KeyQuorumID]
    """A unique identifier for a key quorum."""

    display_name: Required[str]
