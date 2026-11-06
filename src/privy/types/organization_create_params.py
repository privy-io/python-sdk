# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .key_quorum_id import KeyQuorumID
from .organization_default_wallet_configurations_param import OrganizationDefaultWalletConfigurationsParam

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    default_key_quorum_id: Required[KeyQuorumID]
    """A unique identifier for a key quorum."""

    display_name: Required[str]

    default_wallet_configurations: OrganizationDefaultWalletConfigurationsParam
    """
    Defaults applied to wallets created with the organization as their entity, keyed
    by chain type.
    """
