# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .organization_wallet_configuration_param import OrganizationWalletConfigurationParam

__all__ = ["OrganizationDefaultWalletConfigurationsUpdateParam"]


class OrganizationDefaultWalletConfigurationsUpdateParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=Optional[OrganizationWalletConfigurationParam],  # pyright: ignore[reportGeneralTypeIssues]
):
    """Changes to the defaults, keyed by chain type.

    Omitted chains and fields are unchanged, and `null` removes a chain.
    """

    ethereum: Optional[OrganizationWalletConfigurationParam]
    """Default policies and additional signers for wallets of one chain type."""

    solana: Optional[OrganizationWalletConfigurationParam]
    """Default policies and additional signers for wallets of one chain type."""

    tron: Optional[OrganizationWalletConfigurationParam]
    """Default policies and additional signers for wallets of one chain type."""
