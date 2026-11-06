# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .organization_wallet_configuration_param import OrganizationWalletConfigurationParam

__all__ = ["OrganizationDefaultWalletConfigurationsParam"]


class OrganizationDefaultWalletConfigurationsParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=OrganizationWalletConfigurationParam,  # pyright: ignore[reportGeneralTypeIssues]
):
    """
    Defaults applied to wallets created with the organization as their entity, keyed by chain type.
    """

    ethereum: OrganizationWalletConfigurationParam
    """Default policies and additional signers for wallets of one chain type."""

    solana: OrganizationWalletConfigurationParam
    """Default policies and additional signers for wallets of one chain type."""

    tron: OrganizationWalletConfigurationParam
    """Default policies and additional signers for wallets of one chain type."""
