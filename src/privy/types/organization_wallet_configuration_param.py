# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .policy_input_param import PolicyInputParam
from .additional_signer_input_param import AdditionalSignerInputParam

__all__ = ["OrganizationWalletConfigurationParam"]


class OrganizationWalletConfigurationParam(TypedDict, total=False):
    """Default policies and additional signers for wallets of one chain type."""

    additional_signers: AdditionalSignerInputParam
    """Additional signers for the wallet."""

    policy_ids: PolicyInputParam
    """An optional list of up to one policy ID to enforce on the wallet."""
