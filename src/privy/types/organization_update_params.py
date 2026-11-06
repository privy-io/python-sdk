# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .key_quorum_id import KeyQuorumID
from .organization_default_wallet_configurations_update_param import OrganizationDefaultWalletConfigurationsUpdateParam

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    default_key_quorum_id: KeyQuorumID
    """A unique identifier for a key quorum."""

    default_wallet_configurations: OrganizationDefaultWalletConfigurationsUpdateParam
    """Changes to the defaults, keyed by chain type.

    Omitted chains and fields are unchanged, and `null` removes a chain.
    """

    display_name: str
